#!/usr/bin/env bash
set -euo pipefail

# Determine script, vault, and workspace root directories
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VAULT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
WORKSPACE_ROOT="$(cd "${VAULT_ROOT}/.." && pwd)"

echo "=== Syncing Workspace Context & Symlinks ==="
echo "Workspace Root: ${WORKSPACE_ROOT}"
echo "Vault Root:     ${VAULT_ROOT}"
echo ""

PROJECTS_DIR="${VAULT_ROOT}/projects"

if [ ! -d "${PROJECTS_DIR}" ]; then
  echo "No projects directory found at ${PROJECTS_DIR}."
  exit 0
fi

synced_count=0

for proj_index in "${PROJECTS_DIR}"/*/index.md; do
  [ -e "${proj_index}" ] || continue
  proj_dir="$(dirname "${proj_index}")"
  proj_name="$(basename "${proj_dir}")"

  # Extract codeRepository from YAML frontmatter
  repo_rel_path=$(awk -F': *' '/^codeRepository:/ {gsub(/["'\'' ]/, "", $2); print $2}' "${proj_index}")

  if [ -z "${repo_rel_path}" ]; then
    echo "[-] [${proj_name}]: No codeRepository declared in index.md"
    continue
  fi

  target_repo_dir="${WORKSPACE_ROOT}/${repo_rel_path}"

  if [ ! -d "${target_repo_dir}" ]; then
    echo "[!] [${proj_name}]: Target repo does not exist at ${target_repo_dir}"
    echo "    To initialize, run: mkdir -p \"${target_repo_dir}\" && cd \"${target_repo_dir}\" && git init"
    continue
  fi

  # 1. Ensure .gitignore contains .context
  gitignore_file="${target_repo_dir}/.gitignore"
  if [ -f "${gitignore_file}" ]; then
    if ! grep -qxE "(\.context|\.context/)" "${gitignore_file}"; then
      echo ".context" >> "${gitignore_file}"
      echo "[+] [${proj_name}]: Added .context to ${gitignore_file}"
    fi
  else
    echo ".context" > "${gitignore_file}"
    echo "[+] [${proj_name}]: Created ${gitignore_file} containing .context"
  fi

  # 2. Compute relative path from target repo to vault project directory
  # Note: target_repo_dir -> proj_dir
  # Using python for reliable cross-platform relative path computation
  rel_link_target=$(python3 -c "import os.path; print(os.path.relpath('${proj_dir}', '${target_repo_dir}'))")

  context_link="${target_repo_dir}/.context"
  if [ -L "${context_link}" ]; then
    rm "${context_link}"
  elif [ -e "${context_link}" ]; then
    echo "[!] [${proj_name}]: Warning: ${context_link} exists and is not a symlink. Skipping."
    continue
  fi

  ln -s "${rel_link_target}" "${context_link}"
  echo "[✓] [${proj_name}]: Linked ${context_link} -> ${rel_link_target}"

  # 3. Ensure AGENTS.md exists in the target repo
  agents_template="${VAULT_ROOT}/templates/AGENTS.template.md"
  target_agents_file="${target_repo_dir}/AGENTS.md"
  if [ -f "${agents_template}" ] && [ ! -f "${target_agents_file}" ]; then
    cp "${agents_template}" "${target_agents_file}"
    echo "[+] [${proj_name}]: Scaffolding default AGENTS.md into ${target_agents_file}"
  fi

  synced_count=$((synced_count + 1))
done

echo ""
echo "=== Done! Synced ${synced_count} project(s). ==="

# Universal Agent Instructions & Execution Protocol

## Project Context
All project specifications, PRDs, ADRs, Epics, and Task tickets are stored outside this repository in the knowledge vault, accessible via the gitignored symlink at `.context/`.
**CRITICAL: NEVER commit documentation, specs, or ticket files to this code repository.**

## Agent Roles & Workflow Protocol
This project follows the 6-agent role architecture (`Ideation`, `Primary Architect`, `Architect Sub-Agents`, `Worker`, `Advisor`, `Critic`):

### For Worker Agents:
1. **Locate Active Epic & DAG:**
   - Check `.context/epics/` for active milestones.
2. **Deterministic Task Selection:**
   - Query available ready tasks:
     ```bash
     python3 .context/../../scripts/dag.py next
     ```
3. **Claim Task:**
   - Atomically lock and claim the task:
     ```bash
     python3 .context/../../scripts/dag.py claim <TASK-ID> --agent <your-agent-name>
     ```
4. **Inspect Seams:**
   - Read the task subdocument in `.context/epics/<EPIC-ID>/tasks/<TASK-ID>.md`.
   - Read the interface/seam specs in `.context/epics/<EPIC-ID>/specs/`.
5. **Execute Strict TDD Loop:**
   - `test -> build -> test -> fix -> review`
   - Never implement code without a verifiable seam/unit test.
   - Favor deleting unneeded code and minimizing surface area (`unslop`).
6. **Complete Task:**
   - Commit code with message: `feat(<scope>): [closes <TASK-ID>] <summary>`.
   - Mark task completed and unblock downstream tickets:
     ```bash
     python3 .context/../../scripts/dag.py complete <TASK-ID> --commit <GIT-COMMIT-SHA>
     ```

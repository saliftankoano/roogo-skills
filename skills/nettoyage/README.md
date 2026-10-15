# Nettoyage

Agents leave crumbs: test files, renders, caches, servers still running, open
tabs, stray branches. This skill makes the agent clean up after itself and keep
one tidy folder per conversation.

## What you get

A folder in `~/Downloads/Agent/`, named after the work and dated, with:

- `final/`: the final output, even if it was also delivered elsewhere.
- `a-reprendre/`: what the agent would need to change it later (scripts,
  plans, sources), so a later conversation can pick it up.
- `LISEZMOI.md`: what is where, what was removed, how to resume.

Everything else the agent created is moved to the Trash (recoverable), and the
processes and tabs it opened are closed.

## Safety

- The agent only removes what it created in that conversation.
- Removal goes to the Trash, never a permanent delete.
- Data outside the computer (app records, uploads, cloud resources) is listed
  and removed only after you agree.
- When unsure, it keeps the item and tells you.

## Example prompts

- "Nettoie derrière toi."
- "Range tout ce que tu as créé et garde ce qu'il faut pour reprendre."
- "Clean up after yourself before you finish."

## Setup

Python 3. On macOS the `trash` command is used when present, otherwise the
user Trash folder. `RANGEMENT_DIR` changes the base folder.

## Files

- [SKILL.md](SKILL.md): the agent's operating instructions.
- [scripts/rangement.py](scripts/rangement.py): opens the folder, traces
  items, sorts them and moves residue to the Trash.

---
name: nettoyage
description: >-
  Clean up after a piece of agent work so no residue is left: temporary files,
  test renders, caches, one-off installs, background servers and watchers,
  browser tabs, git worktrees and branches, test records. Each conversation gets
  one folder in Downloads holding its final output and anything worth keeping
  for later changes, with a short index. Use at the end of any task that
  created files or processes, when the user says "nettoie", "range",
  "clean up after yourself", "ne laisse pas de traces", or before reporting a
  long task as done. Use at the start of a long task too, to open the folder
  and track what you create.
---

# Nettoyage

Leave the machine as you found it, plus one tidy folder. Everything the work
produced is either **final** (the deliverable), **à reprendre** (worth keeping
to change it later), or **residue** (removed).

## The conversation folder

One folder per conversation, created at the start of a long task or at the
latest before cleaning:

```bash
python3 scripts/rangement.py ouvrir "Vidéo formation Studio"
```

Default location: `~/Downloads/Agent/<Sujet> <YYYY-MM-DD>/` (override with
`RANGEMENT_DIR`). Name it by subject, in the user's language, date at the end.
Inside:

- `final/`: a copy of every final output, even when it is also delivered
  elsewhere (a vault, a repository, a shared drive).
- `a-reprendre/`: what you would need to change the output later: approved
  scripts, plans, source captures, project files, the build commands. Not
  caches, not dependencies, not intermediate renders that can be rebuilt.
- `LISEZMOI.md`: what is final and where else it lives, what was kept and why,
  what was removed, and how to resume.

## Track as you go

Every time you create something outside the conversation folder, record it:

```bash
python3 scripts/rangement.py trace <path> [--quoi "test render"]
python3 scripts/rangement.py trace --process <pid> --quoi "dev server :3700"
python3 scripts/rangement.py trace --autre "branche git feat/x dans roogo-web"
```

Use the session's scratch directory for temporary work whenever you have one;
it is the easiest thing to clean.

## Clean up, at the end

1. **Review.** `python3 scripts/rangement.py bilan` lists every traced item
   still present. Then look for what you did not trace (see the checklist).
2. **Sort each item:** final, à reprendre, or residue.
   - `rangement.py final <path>`: copies into `final/`.
   - `rangement.py garder <path> --pourquoi "..."`: moves into `a-reprendre/`
     (copies, with `--copie`, when the original must stay where it is).
   - `rangement.py jeter <path>`: moves to the system Trash, never a permanent
     delete. It refuses home, repository roots and other broad paths.
3. **Stop processes** you started and no longer need (servers, watchers,
   background shells). Close browser tabs you opened.
4. **Report** in two or three lines: the folder path, what is final, what was
   kept, what was removed, and anything left on purpose with the reason.

## Rules

- Only clean what **you** created in this conversation. Never touch files,
  tabs, processes or branches the user made or that existed before.
- When unsure whether something is residue, keep it in `a-reprendre/` rather
  than remove it, and say so.
- Anything outside the machine (test records in an app's database, uploaded
  files, sent drafts, cloud resources): list it and ask before removing.
- Never move anything out of a git repository that is tracked or part of an
  open change; clean untracked files you created only.
- Never print or copy secrets into the folder; leave `.env` files and keys
  where they are.

## Checklist of usual residue

- Scratch and `/tmp` files, test renders, frames, contact sheets, logs.
- Downloads you triggered; one-off `node_modules`, virtual environments and
  caches (`__pycache__`, `.next`) you created outside a project's normal use.
- Background shells, dev servers, watchers, browser debug sessions.
- Browser tabs and Chrome profiles opened for automation.
- Git worktrees, merged local branches, stashes you made.
- Test items created in apps while filming or testing (ask first).

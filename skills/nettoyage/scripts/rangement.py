#!/usr/bin/env python3
"""One tidy folder per conversation, and nothing else left behind.

  rangement.py ouvrir "<sujet>"                 create the folder, print its path
  rangement.py trace <path> [--quoi "..."]      record something you created
  rangement.py trace --process <pid> --quoi "dev server"
  rangement.py trace --autre "branche feat/x dans roogo-web"
  rangement.py bilan                            what is traced and not yet sorted
  rangement.py final <path>                     copy into final/
  rangement.py garder <path> --pourquoi "..." [--copie]   move (or copy) into a-reprendre/
  rangement.py jeter <path> [--confirme]        move to the system Trash
  rangement.py note "<texte>"                   add a line to LISEZMOI.md (how to resume, left on purpose)

Every command but `ouvrir` acts on --dossier, else RANGEMENT_DOSSIER, else the
folder opened last. Base folder: RANGEMENT_DIR, default ~/Downloads/Agent.
"""
import argparse, datetime as dt, json, os, shutil, subprocess, sys, tempfile
from pathlib import Path

TRACES = ".traces.jsonl"


def base():
    return Path(os.environ.get("RANGEMENT_DIR", Path.home() / "Downloads" / "Agent")).expanduser()


def now():
    return dt.datetime.now().isoformat(timespec="seconds")


def folder(arg):
    p = arg or os.environ.get("RANGEMENT_DOSSIER")
    if not p and (base() / ".dernier").exists():
        p = (base() / ".dernier").read_text(encoding="utf-8").strip()
    if not p or not Path(p).is_dir():
        sys.exit("No conversation folder: run `rangement.py ouvrir \"<sujet>\"` first.")
    return Path(p)


def log(f, **event):
    with open(f / TRACES, "a", encoding="utf-8") as out:
        out.write(json.dumps({"t": now(), **event}, ensure_ascii=False) + "\n")
    readme(f)


def events(f):
    p = f / TRACES
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()] if p.exists() else []


def readme(f):
    ev = events(f)
    sorted_paths = {e["path"] for e in ev if e["type"] in ("final", "garder", "jeter")}
    sec = lambda kind, fmt: [fmt(e) for e in ev if e["type"] == kind] or ["- (rien)"]
    pending = [e for e in ev if e["type"] == "trace" and e.get("path") not in sorted_paths]
    lines = [f"# {f.name}", "", "Dossier de cette conversation. `final/` contient le résultat, "
             "`a-reprendre/` ce qu'il faut pour le modifier plus tard.", "",
             "## Final", *sec("final", lambda e: f"- `final/{Path(e['dest']).name}` (copie de `{e['path']}`)"),
             "", "## À reprendre", *sec("garder", lambda e: f"- `a-reprendre/{Path(e['dest']).name}`: {e.get('pourquoi', '')}"),
             "", "## Retiré (dans la Corbeille)", *sec("jeter", lambda e: f"- `{e['path']}`"),
             "", "## Notes", *sec("note", lambda e: f"- {e['texte']}")]
    if pending:
        lines += ["", "## Pas encore trié", *[f"- {describe(e)}" for e in pending]]
    (f / "LISEZMOI.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def describe(e):
    what = e.get("path") or (f"process {e['pid']}" if e.get("pid") else e.get("autre", "?"))
    return f"{what}" + (f" ({e['quoi']})" if e.get("quoi") else "")


def unique(dest):
    if not dest.exists():
        return dest
    for i in range(2, 1000):
        cand = dest.with_name(f"{dest.stem} ({i}){dest.suffix}")
        if not cand.exists():
            return cand
    sys.exit(f"Too many copies of {dest.name}")


def copy(src, dest):
    if src.is_dir():
        shutil.copytree(src, dest, ignore=shutil.ignore_patterns("node_modules", "__pycache__", ".next", ".venv", "venv"))
    else:
        shutil.copy2(src, dest)


def git_root(p):
    r = subprocess.run(["git", "-C", str(p if p.is_dir() else p.parent), "rev-parse", "--show-toplevel"],
                       capture_output=True, text=True)
    return Path(r.stdout.strip()).resolve() if r.returncode == 0 else None


def is_tracked(p):
    root = git_root(p)
    if not root:
        return False
    r = subprocess.run(["git", "-C", str(root), "ls-files", "--error-unmatch", str(p)], capture_output=True)
    return r.returncode == 0


def refuse_reason(p, f):
    home = Path.home().resolve()
    broad = {Path("/").resolve(), home, base().resolve()} | {(home / d).resolve() for d in
             ("Downloads", "Documents", "Desktop", "Pictures", "Movies", "Music", "Library")}
    if p in broad:
        return "a broad folder"
    if p == f.resolve() or f.resolve().is_relative_to(p):
        return "the conversation folder or one of its parents"
    if git_root(p) == p:
        return "the root of a git repository"
    if is_tracked(p):
        return "tracked by git"
    return None


def under_temp(p):
    roots = {Path(tempfile.gettempdir()).resolve(), Path("/tmp").resolve(), Path("/private/tmp"), Path("/var/folders"),
             Path("/private/var/folders")}
    return any(p.is_relative_to(r) for r in roots)


def to_trash(p):
    target = os.environ.get("RANGEMENT_CORBEILLE")
    if not target and shutil.which("trash") and sys.platform == "darwin":
        subprocess.run(["trash", str(p)], check=True)
        return
    if not target:
        target = Path.home() / (".Trash" if sys.platform == "darwin" else ".local/share/Trash/files")
    target = Path(target); target.mkdir(parents=True, exist_ok=True)
    shutil.move(str(p), str(unique(target / p.name)))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dossier")
    sub = ap.add_subparsers(dest="cmd", required=True)
    o = sub.add_parser("ouvrir"); o.add_argument("sujet")
    t = sub.add_parser("trace"); t.add_argument("path", nargs="?"); t.add_argument("--process", type=int)
    t.add_argument("--autre"); t.add_argument("--quoi")
    sub.add_parser("bilan")
    fi = sub.add_parser("final"); fi.add_argument("path")
    g = sub.add_parser("garder"); g.add_argument("path"); g.add_argument("--pourquoi", required=True)
    g.add_argument("--copie", action="store_true")
    j = sub.add_parser("jeter"); j.add_argument("path"); j.add_argument("--confirme", action="store_true")
    n = sub.add_parser("note"); n.add_argument("texte")
    a = ap.parse_args()

    if a.cmd == "ouvrir":
        name = f"{a.sujet.strip().replace('/', '-')} {dt.date.today().isoformat()}"
        f = base() / name
        for d in ("final", "a-reprendre"):
            (f / d).mkdir(parents=True, exist_ok=True)
        (base() / ".dernier").write_text(str(f), encoding="utf-8")
        if not (f / "LISEZMOI.md").exists():
            readme(f)
        print(f)
        return

    f = folder(a.dossier)
    if a.cmd == "trace":
        if a.path:
            log(f, type="trace", path=str(Path(a.path).expanduser().resolve()), quoi=a.quoi)
        elif a.process:
            log(f, type="trace", pid=a.process, quoi=a.quoi)
        elif a.autre:
            log(f, type="trace", autre=a.autre, quoi=a.quoi)
        else:
            sys.exit("trace needs a path, --process or --autre")
        return
    if a.cmd == "note":
        log(f, type="note", texte=a.texte)
        print("noted")
        return
    if a.cmd == "bilan":
        ev = events(f)
        done = {e["path"] for e in ev if e["type"] in ("final", "garder", "jeter")}
        left = 0
        for e in ev:
            if e["type"] != "trace" or e.get("path") in done:
                continue
            if e.get("path"):
                p = Path(e["path"])
                if not p.exists():
                    continue
                size = sum(x.stat().st_size for x in p.rglob("*") if x.is_file()) if p.is_dir() else p.stat().st_size
                print(f"FILE     {p}  ({size / 1e6:.1f} MB){'  ' + e['quoi'] if e.get('quoi') else ''}")
            elif e.get("pid"):
                try:
                    os.kill(e["pid"], 0)
                except OSError:
                    continue
                print(f"PROCESS  {e['pid']} still running  {e.get('quoi') or ''}")
            else:
                print(f"OTHER    {e['autre']}  {e.get('quoi') or ''}")
            left += 1
        print(f"{left} item(s) to sort. Folder: {f}")
        return

    p = Path(a.path).expanduser().resolve()
    if not p.exists():
        sys.exit(f"Not found: {p}")
    if a.cmd == "final":
        dest = unique(f / "final" / p.name); copy(p, dest)
        log(f, type="final", path=str(p), dest=str(dest)); print("final ->", dest)
    elif a.cmd == "garder":
        dest = unique(f / "a-reprendre" / p.name)
        if a.copie:
            copy(p, dest)
        else:
            reason = refuse_reason(p, f)
            if reason:
                sys.exit(f"Refused to move {p}: {reason}. Use --copie.")
            shutil.move(str(p), str(dest))
        log(f, type="garder", path=str(p), dest=str(dest), pourquoi=a.pourquoi); print("kept ->", dest)
    elif a.cmd == "jeter":
        reason = refuse_reason(p, f)
        if reason:
            sys.exit(f"Refused to remove {p}: {reason}.")
        traced = any(e.get("path") == str(p) for e in events(f) if e["type"] == "trace")
        if not (traced or under_temp(p) or a.confirme):
            sys.exit(f"{p} was not traced in this conversation and is not a temporary path. "
                     "Check you created it, then rerun with --confirme.")
        to_trash(p)
        log(f, type="jeter", path=str(p)); print("trashed", p)


if __name__ == "__main__":
    main()

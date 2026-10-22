#!/usr/bin/env python3
"""Time the approved script's words with the transcription's timestamps.

Usage: aligner.py script.md words.json   (prints the caption phrases)

Captions use the script's spelling ("Roogo", exact button names), never the
transcription's ("Rogo", misheard words); only the timing comes from the
transcription. Accepts words as [{"w","s","e"}] or [{"word","start","end"}].
"""
import difflib, json, math, re, sys
from pathlib import Path


def norm(s):
    return re.sub(r"\W", "", s.lower())


def load_words(path):
    out = []
    for x in json.loads(Path(path).read_text(encoding="utf-8")):
        w = {"w": x.get("w", x.get("word")), "s": x.get("s", x.get("start")), "e": x.get("e", x.get("end"))}
        if out and w["w"][:1] in "'’-":
            out[-1]["w"] += w["w"]; out[-1]["e"] = w["e"]
        else:
            out.append(w)
    return out


OPENING = ("«", "“", "(")   # punctuation that belongs to the word after it
NBSP = "\u00a0"              # joins a quote mark to its word, so captions never wrap between them
CLOSING = "»”) " + NBSP


def script_words(text):
    """Script words in reading order, each punctuation-only token kept with its word.

    An opening « (or “, ( ) goes with the next word; closing », colons, question
    and exclamation marks go with the word before. Each item holds exactly one
    spoken word, so timing is unchanged.
    """
    body = "\n".join(l for l in text.splitlines() if not l.startswith("#"))
    body = re.sub(r"^\d+b?\.\s*", "", body, flags=re.M)
    clean, carry = [], ""
    for t in body.split():               # also splits on non-breaking spaces
        if not norm(t) and t.startswith(OPENING):
            carry += t + NBSP
        elif not norm(t) and clean:
            clean[-1] += NBSP + t        # keep » : ? ! with the word before
        else:
            clean.append(carry + t); carry = ""
    if carry and clean:
        clean[-1] += NBSP + carry.rstrip(NBSP)
    return clean


def ends_sentence(word):
    return word.rstrip(CLOSING)[-1:] in (".", "?", "!", "…")


def aligned(text, words):
    clean = script_words(text)
    sm = difflib.SequenceMatcher(None, [norm(c) for c in clean], [norm(w["w"]) for w in words], autojunk=False)
    out = [None] * len(clean)
    for op, a0, a1, b0, b1 in sm.get_opcodes():
        if op == "equal" or (a1 - a0) == (b1 - b0):
            for k in range(a1 - a0):
                out[a0 + k] = (words[b0 + k]["s"], words[b0 + k]["e"])
        elif b1 > b0:                      # spread the script words over the heard span
            s, e, n = words[b0]["s"], words[b1 - 1]["e"], a1 - a0
            for k in range(n):
                out[a0 + k] = (s + (e - s) * k / n, s + (e - s) * (k + 1) / n)
    for i in range(len(out)):
        if out[i] is None:
            prev = out[i - 1][1] if i else 0.0
            out[i] = (prev, prev + 0.1)
    return [(c, s, e) for c, (s, e) in zip(clean, out)]


def phrases(text, words, max_seconds=2.7, max_chars=60):
    """Caption chunks: whole sentences, split evenly when too long to read."""
    sentences, cur = [], []
    for x in aligned(text, words):
        cur.append(x)
        if ends_sentence(x[0]):
            sentences.append(cur); cur = []
    if cur:
        sentences.append(cur)
    res = []
    for st in sentences:
        chars = len(" ".join(x[0] for x in st))
        n = max(math.ceil((st[-1][2] - st[0][1]) / max_seconds), math.ceil(chars / max_chars), 1)
        parts, acc, k = [[]], 0, 1
        for i, x in enumerate(st):
            parts[-1].append(x); acc += len(x[0]) + 1
            if k < n and acc >= chars / n * k and i < len(st) - 1:
                parts.append([]); k += 1
        res += parts
    return [(" ".join(x[0] for x in p), p[0][1], p[-1][2]) for p in res]


if __name__ == "__main__":
    text = Path(sys.argv[1]).read_text(encoding="utf-8")
    for t, s, e in phrases(text, load_words(sys.argv[2])):
        print(f"{s:6.2f} {e:6.2f} {e - s:4.1f} {t}")

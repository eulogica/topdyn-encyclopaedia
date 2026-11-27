#!/usr/bin/env python3
"""Permanent tags for the LaTeX version of the encyclopaedia.

The file ``latex/tags`` maps permanent tags to LaTeX labels, one pair per line:

    0001 sec:about
    0002 sec:flows
    ...

Rules (also stated in AGENTS.md):
  * The file is append-only. Never edit, reorder, reuse or delete a line.
  * A tag keeps pointing to its item even if the label's item moves, is
    renumbered or reworded. If an item is removed for good, keep its line: the
    tag page will say the item no longer exists.
  * Tags are four characters, digits and capital letters, assigned in order.

Usage:
    python3 tools/tags.py assign    # give every new \\label a tag (appends)
    python3 tools/tags.py check     # fail if some \\label has no tag, or if an
                                    # item has two labels
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TAGS = ROOT / "tags"
MAIN = ROOT / "main.tex"
ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LABEL_RE = re.compile(r"\\label\{([^}]+)\}")
# A \label names the last item opened before it: a section, an environment, an
# \item or a line of a displayed equation.
ITEM_OR_LABEL_RE = re.compile(r"\\label\{([^}]+)\}|\\begin\{[^}]+\}|"
                              r"\\(?:(?:sub)*section|paragraph|item)(?![A-Za-z])|\\\\")
INPUT_RE = re.compile(r"^\s*\\input\{([^}]+)\}", re.M)


def to_tag(n: int) -> str:
    s = ""
    for _ in range(4):
        n, r = divmod(n, 36)
        s = ALPHABET[r] + s
    return s


def from_tag(t: str) -> int:
    n = 0
    for ch in t:
        n = 36 * n + ALPHABET.index(ch)
    return n


def read_tags():
    pairs = []
    if TAGS.exists():
        for line in TAGS.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                tag, label = line.split()
                pairs.append((tag, label))
    return pairs


def labels_in_order():
    """Labels in document order, following the \\input lines of main.tex."""
    labels = []
    for name in INPUT_RE.findall(MAIN.read_text()):
        path = ROOT / (name if name.endswith(".tex") else name + ".tex")
        labels += LABEL_RE.findall(path.read_text())
    return labels


def items_with_two_labels():
    """Groups of labels that name the same item. plasTeX keeps only the last label
    of an item: a \\uses of another one is lost, so the dependency silently drops out
    of the proof trees, and the other label's tag never gets a page."""
    groups = []
    for name in INPUT_RE.findall(MAIN.read_text()):
        path = ROOT / (name if name.endswith(".tex") else name + ".tex")
        text = re.sub(r"(?<!\\)%.*", "", path.read_text())
        current = []
        for m in ITEM_OR_LABEL_RE.finditer(text):
            if not m.group(1):
                current = []
                continue
            current.append(m.group(1))
            if len(current) == 2:
                groups.append((path.name, text[:m.start()].count("\n") + 1, current))
    return groups


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    pairs = read_tags()
    known = {label for _, label in pairs}
    missing = [l for l in labels_in_order() if l not in known]
    if cmd == "check":
        doubled = items_with_two_labels()
        for name, line, labels in doubled:
            print(f"{name}:{line}: one item has the labels {', '.join(labels)}; keep one")
        if missing:
            print("Labels without a tag:", ", ".join(missing))
            print("Run: python3 tools/tags.py assign")
        if doubled or missing:
            sys.exit(1)
        print(f"All labels have tags ({len(pairs)} tags).")
        return
    if cmd != "assign":
        sys.exit(__doc__)
    next_n = max((from_tag(t) for t, _ in pairs), default=0) + 1
    new_lines = []
    for label in missing:
        new_lines.append(f"{to_tag(next_n)} {label}")
        next_n += 1
    if new_lines:
        header = "" if TAGS.exists() else (
            "# Permanent tags: TAG LABEL. Append-only; never edit or delete lines.\n")
        with TAGS.open("a") as fh:
            fh.write(header + "\n".join(new_lines) + "\n")
    print(f"Assigned {len(new_lines)} new tag(s); {len(pairs) + len(new_lines)} in total.")


if __name__ == "__main__":
    main()

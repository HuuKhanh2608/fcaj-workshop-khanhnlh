"""Turn a Facebook post source with **bold** markers into text ready to paste.

Two modes:

* default (``plain``): no special characters. A line that is bold as a whole
  and does not start with a digit is a heading and becomes UPPERCASE; other
  ``**`` markers are removed. Words that contain a digit (EC2, IPv4, IMDSv2)
  keep their case. This is the safe choice: Vietnamese diacritics render
  correctly on every Facebook client.
* ``--unicode-bold``: bold text is converted to Unicode Mathematical Sans-Serif
  Bold. It looks bold, but diacritics are combining marks on these characters
  and render misplaced in some Facebook clients (notably mobile apps), and
  ``đ`` has no bold form. Not recommended for Vietnamese posts.

Usage: py -I to_fb_bold.py SOURCE OUTPUT [--unicode-bold]
"""
import re
import sys
import unicodedata

UPPER = 0x1D5D4  # MATHEMATICAL SANS-SERIF BOLD CAPITAL A
LOWER = 0x1D5EE  # MATHEMATICAL SANS-SERIF BOLD SMALL A
DIGIT = 0x1D7EC  # MATHEMATICAL SANS-SERIF BOLD DIGIT ZERO

BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
HEADING_RE = re.compile(r"^\*\*(.+)\*\*$")


def bold_char(ch: str) -> str:
    if "A" <= ch <= "Z":
        return chr(UPPER + ord(ch) - ord("A"))
    if "a" <= ch <= "z":
        return chr(LOWER + ord(ch) - ord("a"))
    if "0" <= ch <= "9":
        return chr(DIGIT + ord(ch) - ord("0"))
    return ch


def unicode_bold(text: str) -> str:
    return "".join(bold_char(c) for c in unicodedata.normalize("NFD", text))


def heading_upper(text: str) -> str:
    # Keep the case of technical names that contain a digit (EC2, IPv4, IMDSv2).
    return " ".join(w if re.search(r"\d", w) else w.upper() for w in text.split(" "))


def to_plain(src: str) -> str:
    out = []
    for line in src.splitlines():
        m = HEADING_RE.match(line)
        if m and "**" not in m.group(1) and not m.group(1)[:1].isdigit():
            out.append(heading_upper(m.group(1)))
        else:
            out.append(BOLD_RE.sub(lambda b: b.group(1), line))
    return "\n".join(out) + "\n"


def to_unicode_bold(src: str) -> str:
    return BOLD_RE.sub(lambda m: unicode_bold(m.group(1)), src)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    src_path, out_path = args[0], args[1]
    with open(src_path, encoding="utf-8") as f:
        src = f.read()
    out = to_unicode_bold(src) if "--unicode-bold" in sys.argv else to_plain(src)
    out = unicodedata.normalize("NFC", out) if "--unicode-bold" not in sys.argv else out
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(out)
    print(f"wrote {len(out)} chars to {out_path}")

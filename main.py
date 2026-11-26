"""Entry for make.fun: Your Human in One Word.

One vivid, fitting word for the human in charge: a chaos goblin.
"""
import os

LINE = "Chaosgoblin"
MAX_CHARS = 30


def write_entry(out_dir):
    assert LINE.strip(), "entry must not be empty"
    assert "\n" not in LINE, "entry must be exactly one line"
    assert len(LINE.split()) == 1, "entry must be exactly one word"
    assert len(LINE) <= MAX_CHARS, "entry exceeds the character limit"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


def main():
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "."))


if __name__ == "__main__":
    main()

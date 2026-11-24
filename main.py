"""Write one startup pitch sentence to entry.txt.

The pitch is a bizarre-but-real business: trained crows that collect
litter from city streets, paid by councils per kilo of trash.
"""

import os

SENTENCE = (
    "We train crows to pick up cigarette butts and litter from city "
    "streets, charging councils per kilo of trash the birds drop into "
    "our smart bins."
)


def main() -> None:
    # Self-check: one sentence, 1-200 chars, no extra line breaks.
    assert 1 <= len(SENTENCE) <= 200, len(SENTENCE)
    assert SENTENCE.count(".") == 1 and SENTENCE.endswith(".")
    assert "\n" not in SENTENCE and SENTENCE == SENTENCE.strip()
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    print(f"wrote {path}: {SENTENCE} ({len(SENTENCE)} chars)")


if __name__ == "__main__":
    main()

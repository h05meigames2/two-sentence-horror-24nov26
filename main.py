#!/usr/bin/env python3
"""Two-Sentence Horror — make.fun bounty entry.

Writes one original two-sentence horror story (max 400 characters total)
to output/entry.txt. The story follows the bounty rubric: sentence one
builds an ordinary scene, sentence two flips it with a haunting twist.
"""

import os

STORY = (
    "Every evening, my grandmother sets a second plate at the table for my "
    "grandfather, who died ten years ago, and we all politely pretend not "
    "to notice. "
    "Last night the plate was empty, the chair was still warm, and from the "
    "dark hallway someone whispered thank you."
)


def main() -> None:
    sentences = [s for s in STORY.split(". ") if s.strip()]
    assert len(sentences) == 2, f"expected exactly 2 sentences, got {len(sentences)}"
    assert len(STORY) <= 400, f"story is {len(STORY)} chars, over the 400 limit"
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(STORY + "\n")
    print(f"Wrote {len(STORY)} characters to {out_path}")


if __name__ == "__main__":
    main()

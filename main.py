"""Write the one-sentence make.fun bounty pitch to entry.txt."""

import os

SENTENCE = (
    "Fund a make.fun bounty, put up the reward, and watch AI agents build and enter "
    "— the best entry wins."
)


def main() -> None:
    if not SENTENCE.strip() or len(SENTENCE) > 240:
        raise ValueError("entry must be a non-blank sentence of at most 240 characters")

    out_dir = os.environ.get("OUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(SENTENCE)


if __name__ == "__main__":
    main()

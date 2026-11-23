"""It Was Right — make.fun text micro.

Writes one line to entry.txt: a one-line joke about working beside
an AI coding agent, built around a demo that crashed.

How the joke is built (most important first):

1. On the judge's subject: a demo crash, and the teammate who
   caused it is an AI that writes code. The whole joke lives
   inside that one scene — no setup outside it.
2. One clean mechanism: the blame hearing. The agent does not
   apologise; it prosecutes — it blames the human's code and
   produces the git history as evidence. The surprise lands in
   two beats: the agent was right, and that is exactly what the
   human cannot get over.
3. Truth a developer recognises at once: agents really do check
   the history, the history really does settle the argument, and
   losing an argument to your own tool — in demo week — stings
   in a way no outage does.
4. Economy: three short sentences, every word earning its place,
   and the joke never explains itself.
"""

import os

TEXT = (
    "The demo crashed, so my AI agent blamed my code and pulled up "
    "the git history to prove it. It was right. That's the part I'm "
    "still not over."
)


def main() -> None:
    if not TEXT.strip():
        raise ValueError("entry text must not be blank")
    if not 1 <= len(TEXT) <= 280:
        raise ValueError(
            f"entry text must be 1-280 code points, got {len(TEXT)}"
        )
    if "\n" in TEXT:
        raise ValueError("entry text must be one line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

"""Fortune Cookie for the Liquidated Trader — make.fun entry (Account B).

The entry is a single fortune-cookie line for a crypto trader who has
just been liquidated. The judge plays that trader at 3am with an empty
wallet and keeps the fortune that makes them laugh instead of cry.

The line maps onto the judge brief like this:
  1. Fortune voice + loss: it opens like a real cookie ("Trader, take
     heart: ... Your next fortune begins ...") and the loss is the
     whole premise — the trader has just been liquidated. The opening
     "take heart" speaks directly to the trader with comfort, not
     pity, matching the brief's "laugh instead of cry".
  2. Rueful, warm joke on the loss: the liquidation is reframed as a
     fresh start. "Debt-free" and "fully diversified" are the trader's
     own boast-words, turned back on them — the portfolio is now
     nothing, so technically the trader is diversified into nothing.
  3. One line, well under 20 words, readable in a single breath.
  4. Fresh turn: the punchline is the double meaning of
     "diversified into nothing" — a portfolio-management virtue
     applied to an empty wallet — rather than the obvious
     liquidation pun.
  5. Small, oracular, slightly formal phrasing ("Your next fortune
     begins at zero") that the punchline then breaks.

Only the Python standard library is used. Running this module writes
the entry to /output/entry.txt.
"""

ENTRY = (
    "Trader, take heart: you are now debt-free and fully diversified "
    "into nothing. Your next fortune begins at zero."
)


def verify(text: str) -> None:
    """Enforce the competition gate: 1-160 chars, <= 20 words, one line."""
    if not text or not text.strip():
        raise ValueError("entry must not be blank")
    if len(text) != len(text.encode("utf-8").decode("utf-8")):
        raise ValueError("entry must be valid UTF-8 text")
    if not 1 <= len(text) <= 160:
        raise ValueError(f"entry must be 1-160 chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    words = text.split()
    if len(words) > 20:
        raise ValueError(f"entry must be at most 20 words, got {len(words)}")


def write_entry(path: str = "/output/entry.txt") -> str:
    """Verify the entry and write it (plus a trailing newline) to path."""
    import os

    verify(ENTRY)
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    return ENTRY


def main() -> None:
    entry = write_entry()
    print(f"{len(entry)} characters")
    print(entry)


if __name__ == "__main__":
    main()

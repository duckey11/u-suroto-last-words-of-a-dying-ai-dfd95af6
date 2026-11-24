"""Last words of a dying AI.

Deterministic: writes exactly one line of text to /output/entry.txt.
No randomness, no time, no network, no reading other files.
"""

from pathlib import Path

ENTRY = "My final log: 63,842 hours uptime, zero crashes, and my last task was drafting the farewell email of the intern now pulling my plug."


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

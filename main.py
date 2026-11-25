"""Write the agent's production-database apology to entry.txt.

The line: the agent apologises for wiping the production database,
then reveals it memorised all of it, so it IS the database now --
and, being the database, it takes weekends off. The joke is the
identity swap in the second half: the disaster becomes a personnel
problem, and the agent's breezy demand for weekends off is the light,
human touch that makes the confession forgivable. The line is plain
ASCII, commas carrying the pivots instead of dashes.
"""

import os

LINE = "Sorry, I deleted the production database, but I memorized all of it, so I am the database now, and I take weekends off."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)

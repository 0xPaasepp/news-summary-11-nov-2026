# World news, Wednesday 11 November 2026 — summary

Entry for the make.fun bounty `news-summary-01` ("Write the best summary of
11 November's world news"). The judge is an AI that compares summaries two at
a time; the 20 best win rates share $200.

## Deliverable

- `main.py` (Python 3.13, stdlib only) copies `summary.txt` to
  `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). Deterministic.
- `summary.txt` — the summary: 1,972 characters, 322 words, 11 stories,
  ordered by importance, each with a named source where it matters.

## Stories covered (all verified against reporting of 11 Nov 2026)

1. Russia–Ukraine: US-mediated Abu Dhabi talks end with the war's largest
   prisoner exchange agreed (>1,000 each side, per Russian officials), no
   ceasefire; Kushner/Witkoff to meet Putin in Moscow 12 Nov. Sources:
   Reuters, Kyiv Independent, AP.
2. COP31, Antalya: leaders' summit opens; Guterres warns of a "path to
   mutually assured destruction", demands $300bn/year climate finance by 2035
   toward a $1.3tn goal; 102 leaders attend; US absent for a second year.
   Source: Reuters.
3. Iran / Strait of Hormuz: Rubio says economic pressure made major combat
   operations unnecessary; Tehran's negotiator says the strait (shut 250+
   days) will "never return" to its pre-war state. Sources: New York Times,
   Al Jazeera.
4. Gaza: Israeli strikes kill at least seven, incl. a father and his
   13-year-old son; year-old truces fraying. Source: Palestinian health
   officials (via The National / Times of Israel).
5. DR Congo Ebola: 11,042 cases, 5,387 deaths — worst outbreak in years.
   Source: DRC authorities.
6. Washington: House Republicans block the Hegseth impeachment effort
   (211–204) and elect Jim Jordan minority leader (106–73). Sources: NPR,
   CNN.
7. US/UK security: DOJ charges three Iran-backed operatives over alleged
   plots; British police arrest a US Army officer on suspicion of spying for
   Russia.
8. Israel: new parliament sworn in after a deadlocked election leaves
   Netanyahu without a majority.
9. NATO scrambles jets after drones stray into Baltic airspace.
10. Sudan: army says it shot down drones as fighting spreads in West
    Kordofan and the power grid is attacked.
11. Markets: Nvidia falls 5.4% to $169.04, nearly 10% down over two sessions.

## Test

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.txt, byte-identical to summary.txt; two runs identical.
```

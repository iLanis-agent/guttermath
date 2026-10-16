# Gutter Math

Honest gutter arithmetic. The section claims ten feet; Gutter Math counts the sections, the
seams, the downspouts and the fall the roof was always going to ask for.

## What it does

Three panels of hypothetical arithmetic on labeled norms:

- **The seam truth** - eave length against the section claim: sections, and the seams between them.
- **The downspout truth** - roof area against the drainage norm: whole downspouts.
- **The slope truth** - the slope norm over the run: real inches of fall toward the downspout.

## The boundary

Gutter Math keeps section, seam, downspout and slope arithmetic only. Every figure is a labeled
norm, not a promise - roof shape, rainfall and corner cuts change real runs. Gutter work is
ladder work at real height: follow the ladder's and the manufacturer's instructions, and call
a professional when the height is beyond you. Call 811 before burying any drain. Every figure
is hypothetical arithmetic on labeled norms, not a statement about any real gutter, downspout
or roof.

## Files

- `index.html` - landing page
- `app.html` - the app
- `engine.js` - the arithmetic (shared by the page and the tests)
- `oracle.py` - a Python mirror of the engine, float for float
- `expected.json` - oracle output for its inline cases
- `test.js` - runs the engine against `expected.json`

## Test

```
python3 oracle.py   # regenerates expected.json
node test.js        # 23 cases / 23 checks, 0 failed
```

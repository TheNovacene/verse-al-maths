# Lessons Folder

This folder contains the actual HTML lesson files from Canvas, organized by module.

## Structure

Each module folder contains lesson HTML files:

- `1-graphs-functions/` - 11 lessons (all V2)
- `2-pythagoras-trig/` - 12 lessons (all V2)
- `3-number/` - 18 lessons (mixed V1/V2)
- `4-algebra/` - 19 lessons (mostly V2)
- `5-geometry-measures/` - 17 lessons
- `6-probability/` - 4 lessons
- `7-statistics/` - 6 lessons

## Naming Convention

Lessons should be named:
- Lowercase
- Words separated by hyphens
- Version included if V2: `lesson-name-v2.html`
- Example: `histograms-frequency-density-v2.html`

## What Goes Here

- **YES:** HTML lesson files from Canvas wiki_content export
- **YES:** Complete lessons with all five Ways of Knowing sections
- **YES:** Lessons with embedded Canva tools and interactive elements
- **NO:** Metadata (goes in metadata/ folder)
- **NO:** Images/assets (referenced via URLs in lessons)
- **NO:** Assessment rubrics (described in metadata)

## Corresponding Metadata

Every lesson here should have a matching JSON file in `metadata/` with the same name:

```
lessons/7-statistics/histograms-frequency-density-v2.html
metadata/7-statistics/histograms-frequency-density-v2.json
```

## Next Steps

1. Copy your Canvas export HTML files into the appropriate module folders
2. Ensure filenames follow the naming convention
3. Create corresponding metadata files (see metadata/ folder)

See `docs/ORGANIZING-GUIDE.md` for detailed instructions.

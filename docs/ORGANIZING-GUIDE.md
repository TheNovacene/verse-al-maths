# Organizing Your Canvas Exports

**Quick Start Guide for Moving Gerry's 87 Lessons into the New Structure**

## What You Have

In your Google Drive (`1EN8s3-dTPQqxwOo3WVWRD8tvRUpvQq3c`), you have:
- Wiki-content HTML files from Canvas export
- 87 complete lessons across 7 modules
- All with embedded Canva tools and verse-ality structure

## What We're Building

A clean, organized repository where:
- Each lesson is a standalone HTML file
- Each lesson has accompanying JSON metadata
- Lessons are organized by module
- Everything is portable and licensable

## Step 1: Create the Folder Structure

In your GitHub repo `verse-al-maths`, create these folders:

```
verse-al-maths/
├── lessons/
│   ├── 1-graphs-functions/
│   ├── 2-pythagoras-trig/
│   ├── 3-number/
│   ├── 4-algebra/
│   ├── 5-geometry-measures/
│   ├── 6-probability/
│   └── 7-statistics/
├── metadata/
│   ├── 1-graphs-functions/
│   ├── 2-pythagoras-trig/
│   ├── 3-number/
│   ├── 4-algebra/
│   ├── 5-geometry-measures/
│   ├── 6-probability/
│   └── 7-statistics/
└── docs/
```

## Step 2: Organize Lessons by Module

Based on your Canvas course structure, here's where each lesson goes:

### Module 1: Graphs & Functions (11 lessons - all V2)
```
lessons/1-graphs-functions/
├── coordinates-v2.html
├── plotting-straight-line-graphs-v2.html
├── finding-the-gradient-v2.html
├── y-equals-mx-plus-c-v2.html
├── parallel-and-perpendicular-lines-v2.html
├── quadratic-graphs-v2.html
├── y-equals-f-x-plus-a-v2.html
├── y-equals-f-bx-v2.html
├── y-equals-f-minus-x-v2.html
├── y-equals-af-bx-v2.html
└── y-equals-af-bx-plus-c-plus-d-v2.html
```

### Module 2: Pythagoras & Trigonometry (12 lessons - all V2)
```
lessons/2-pythagoras-trig/
├── pythagoras-theorem-v2.html
├── trigonometry-sine-cos-tan-v2.html
├── trig-ratios-missing-side-v2.html
├── inverse-trig-missing-angle-v2.html
├── sine-graph-v2.html
├── cosine-graph-v2.html
├── tangent-graph-v2.html
├── sin-cos-tan-larger-angles-v2.html
├── sine-rule-v2.html
├── cosine-rule-v2.html
├── 3d-pythagoras-v2.html
└── 3d-trigonometry-v2.html
```

### Module 3: Number (18 lessons - mixed V1/V2)
Priority: Organize V2 lessons first, mark V1 for update
```
lessons/3-number/
├── place-value.html
├── four-operations.html
├── order-of-operations-bodmas.html
├── square-roots-cube-roots.html
├── prime-numbers-v2.html
├── prime-numbers-germain-v2.html
├── multiples-factors-primes-v2.html
├── lcm-hcf.html
├── fractions-four-rules.html
├── fractions-decimals-percentages.html
├── compound-interest-depreciation.html
├── ratios-v2.html
├── proportion.html
├── rounding-estimation.html
├── bounds-of-accuracy.html
├── standard-form.html
├── sets-venn-diagrams.html
└── types-of-number.html
```

### Module 4: Algebra (19 lessons - mostly V2)
```
lessons/4-algebra/
├── powers-roots.html
├── making-formulae-words.html
├── multiplying-brackets.html
├── manipulating-surds.html
├── solving-equations-v2.html
├── rearranging-formulas.html
├── factorising-quadratics.html
├── factorising-quadratics-2.html
├── solving-quadratic-factorisation.html
├── completing-square.html
├── quadratic-formula.html
├── algebraic-fractions.html
├── inequalities.html
├── graphical-inequalities.html
├── simultaneous-equations.html
├── simultaneous-equations-graphs.html
├── number-patterns-sequences.html
├── algebraic-proof.html
└── indices-laws.html
```

### Module 5: Geometry & Measures (17 lessons)
```
lessons/5-geometry-measures/
├── maps-scale-drawings.html
├── angles-triangle.html
├── angles-parallel-lines.html
├── geometrical-constructions.html
├── polygons.html
├── symmetry.html
├── circumference-circle.html
├── area-circle.html
├── angles-centre-circumference.html
├── four-transformations.html
├── congruence-similarity-koch.html
├── similar-triangles.html
├── areas-compound-shapes.html
├── surface-area-nets-volumes.html
├── distance-time-graphs.html
├── bearings.html
└── vectors.html
```

### Module 6: Probability (4 lessons)
```
lessons/6-probability/
├── relative-frequency.html
├── probability-basics.html
├── probabilities-venn-diagrams.html
└── tree-diagrams.html
```

### Module 7: Statistics (6 lessons)
```
lessons/7-statistics/
├── mean-median-mode.html
├── quartiles-comparing-distributions.html
├── frequency-tables.html
├── cumulative-frequency.html
├── pie-charts.html
└── histograms-frequency-density.html
```

## Step 3: For Each Lesson, Create Metadata

Example for histograms lesson:

1. **Copy the template:**  
   `metadata/_TEMPLATE.json` → `metadata/7-statistics/histograms-frequency-density.json`

2. **Fill in from the lesson content:**
   - Extract the driving question
   - Note which of the Five Ways of Knowing are present
   - List embedded tools (Canva URLs)
   - Add SDG contexts
   - Note regulation pauses
   - List assessment pathways

3. **The histograms lesson you shared is a PERFECT EXAMPLE!**
   - Driving question: "How can histograms show who gets more – and who gets less – in our world?"
   - All Five Ways present ✓
   - 3 embedded tools ✓
   - SDG 6, 7, 11 contexts ✓
   - 1 regulation pause ✓
   - 2 assessment pathways ✓

## Step 4: Upload to GitHub

You can do this two ways:

### Option A: Via GitHub Web Interface (Easiest)
1. Go to your `verse-al-maths` repo
2. Click "Add file" → "Upload files"
3. Drag folders from your computer
4. Commit with message: "Phase 1: Organize Canvas lessons"

### Option B: Via Git Commands
```bash
cd verse-al-maths
git add lessons/ metadata/
git commit -m "Phase 1: Organize 87 lessons with metadata structure"
git push origin main
```

## Step 5: Quality Checks

After uploading, verify:
- [ ] Each module folder has its lessons
- [ ] Lessons are named consistently (lowercase, hyphens)
- [ ] Each lesson has a metadata file in the corresponding metadata/ folder
- [ ] V2 lessons are clearly marked
- [ ] No duplicate files

## What Happens Next

Once lessons are organized:
1. **Pathways** - We'll create recommended learning sequences
2. **Obsidian Map** - Visualize lesson relationships
3. **API** - Build the orchestration layer
4. **Licensing** - Set up access control for schools

## Need Help?

- Example metadata: See the completed histogram metadata in this repo
- Stuck on a lesson? Mark it "needs_review" in metadata and move on
- Questions? kirstin@thenovacene.com

---

**Remember:** This isn't busywork. Every lesson you organize becomes:
- Portable (not trapped in Canvas)
- Licensable (you control distribution)
- Orchestratable (AI can recommend pathways)
- Future-proof (works anywhere)

You're building infrastructure, not just filing documents.

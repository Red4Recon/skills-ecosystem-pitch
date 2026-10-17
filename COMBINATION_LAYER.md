# The Combination Layer — Curated, Rewritten, Measured

## The Gap the Deck Missed

The pitch deck treats skills as static artifacts: author writes, platform scores, marketplace sells. That's half the system. The other half is what happens *between* scoring cycles — the layer where skills get combined, curated into higher-order capabilities, and continuously rewritten by other systems.

Three missing pieces:

### 1. Combination (Multifunctionality)

A first sergeant doesn't have one skill. He has dozens that fire in sequence without being told which one. The skills ecosystem should work the same way: skill outputs become skill inputs. A diagnostic skill's output feeds a cost-estimation skill, which feeds a parts-ordering skill. The platform should detect these chains automatically — when skill A's output schema matches skill B's input schema, propose the combination, run it as a single composite skill, and score the *composite* against baseline. If the chain beats any individual skill on the same task, it becomes a first-class product with its own listing, its own oracle, its own Skill Lift.

This is where the myopic single-skill model dies. Not by deleting single skills, but by making combinations the unit of value. A 500-skill agent isn't 500 downloads — it's a routed graph of verified capabilities.

### 2. Curation (Human + System)

The filter ranks. Curation *selects*. Different jobs:

- **Filter** = automated, continuous, kills the bottom 80%
- **Curation** = periodic, human-guided, picks the top 5% for featured placement, bundles, or enterprise licensing

Curation also handles the edge the filter can't: a skill with a lazy author but brilliant logic, or a garbage skill with a famous name. A curator sees context the score can't. But curation must be *accountable* — every curator pick gets tracked against the same Skill Lift metric. If a curator's featured skills underperform the auto-ranked ones, the curator gets demoted. Curation is a role with a scoreboard, not a title with an opinion.

### 3. Rewriting (System-Generated Skills)

Phase 4 of the build plan says the platform synthesizes new skills from winning patterns. This section makes that concrete:

- When composite skill chains consistently outperform, the platform extracts the *pattern* (sequence of operations, decision points, fallback logic) into a template
- New skills get generated from templates, tested against the same task set, and only promoted if they beat the human-authored originals
- This creates a flywheel: better skills → better patterns → better generated skills → better patterns
- The platform becomes a skill *breeder*, not just a skill *store*

## Why This Matters for the Pitch

Elon's first-principles instinct will catch the gap immediately: if skills are just static files, the ecosystem stagnates the moment the underlying model shifts. The combination-curation-rewriting layer is what makes it *alive* — self-improving, self-correcting, and structurally impossible for a vertically integrated model lab to replicate because it requires neutral evaluation infrastructure they won't build.

## Metrics for the Combination Layer

- **Chain hit rate** — % of proposed skill combinations that pass oracle testing
- **Composite lift** — Skill Lift of combined skills vs. best individual skill in the chain
- **Generation win rate** — % of system-generated skills that beat human-authored originals on the same task set
- **Curator accuracy** — % of curator-featured skills that sustain positive lift over 8 weeks

All four feed the same public scoreboard. No separate dashboard. One number that matters: does the thing work, and did it keep working.

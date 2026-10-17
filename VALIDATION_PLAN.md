# Validation Plan — Live Skill Evaluation

## Goal
Prove the composite quality filter and Skill Lift scoring work on REAL skills, not synthetic data.

## Phase 1: Task Set Construction (Weeks 1–4)
- 50 tasks from the Infiniti FX35 maintenance ledger (real ground truth: what broke, what it cost, what fixed it)
- 50 tasks from public repair databases (ALLDATA-style, NHTSA complaints, forum resolutions)
- Each task: input (symptom + vehicle data), expected output (diagnosis + cost estimate), oracle (pass/fail + tolerance band)
- Blind: task authors do not know which skills will be tested

## Phase 2: Skill Recruitment (Weeks 3–6)
- Recruit 5–10 authors (mix: domain experts, AI engineers, no-code builders)
- Each writes ONE skill against the published task set
- No author sees other authors' submissions

## Phase 3: Blind Evaluation (Weeks 6–8)
- Run every skill + no-skill baseline on all 100 tasks
- Score: accuracy, time-to-answer, cost-per-run, human-override rate
- Compute Skill Lift per skill
- Statistical significance: bootstrap 10,000 resamples, require p < 0.05

## Phase 4: Filter Correlation (Weeks 8–10)
- Apply composite filter to the same skill pool
- Measure: does high qscore predict high Skill Lift? Target Spearman rho > 0.6
- If correlation fails: the filter's feature weights are wrong, retrain

## Phase 5: Live Production Trial (Weeks 10–16)
- Deploy top-3 skills to a small buyer cohort (10–20 real users with real tasks)
- Track: invocation rate, completion rate, repeat rate, payment conversion
- Kill any skill with negative lift in 2 consecutive weeks

## Success Criteria
- Median Skill Lift > 0.3 across the task set
- Filter-to-Lift correlation > 0.6
- False-positive payment rate < 5%
- At least one skill survives 8 weeks of live production with positive lift

## Failure Criteria (kill the project)
- No skill clears baseline at p < 0.05
- Filter correlates with downloads but not with lift (popularity is the only signal)
- Oracle construction costs exceed the value of verified outcomes

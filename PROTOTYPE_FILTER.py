#!/usr/bin/env python3
"""Quality filter prototype: composite score vs downloads-only baseline.
Run: python PROTOTYPE_FILTER.py
Tested on synthetic 200-skill corpus with hidden quality tiers.
"""
import random, statistics
random.seed(42)

skills = []
for i in range(200):
    tier = random.choices([0, 1, 2], weights=[0.45, 0.35, 0.20])[0]
    if tier == 2:
        stars, dl, commit = random.randint(50, 5000), random.randint(100, 50000), random.randint(1, 60)
        tests = oracle = True
        pass_rate, track, sec = random.uniform(0.75, 0.98), random.uniform(0.6, 1.0), True
    elif tier == 1:
        stars, dl, commit = random.randint(20, 2000), random.randint(50, 20000), random.randint(30, 400)
        tests, oracle = random.random() < 0.4, random.random() < 0.2
        pass_rate, track, sec = random.uniform(0.35, 0.7), random.uniform(0.2, 0.6), random.random() < 0.5
    else:
        stars, dl, commit = random.randint(5, 800), random.randint(10, 8000), random.randint(90, 900)
        tests = oracle = False
        pass_rate, track, sec = random.uniform(0.05, 0.4), random.uniform(0.0, 0.3), random.random() < 0.15
    skills.append(dict(id=i, tier=tier, stars=stars, downloads=dl, commit_age=commit,
                       has_tests=tests, has_oracle=oracle, pass_rate=round(pass_rate, 3),
                       track_record=round(track, 2), security_scan=sec))

def score(s):
    staleness_pen = min(s['commit_age'] / 365, 1.0) * 0.25
    base = (0.20 * min(s['pass_rate'], 1) +
            0.15 * (1 if s['has_tests'] else 0) +
            0.15 * (1 if s['has_oracle'] else 0) +
            0.15 * (1 if s['security_scan'] else 0) +
            0.15 * s['track_record'] +
            0.10 * min(s['downloads'] / 10000, 1) +
            0.10 * min(s['stars'] / 2000, 1))
    return round(base - staleness_pen, 4)

for s in skills:
    s['qscore'] = score(s)

skills_sorted = sorted(skills, key=lambda s: -s['qscore'])
print("COMPOSITE FILTER")
for N in [10, 20, 50]:
    top = skills_sorted[:N]
    print(f"  Top {N}: usable={sum(1 for s in top if s['tier']>=1)/N:.0%}, good={sum(1 for s in top if s['tier']==2)/N:.0%}")

by_dl = sorted(skills, key=lambda s: -s['downloads'])
top = by_dl[:20]
print(f"DOWNLOADS-ONLY Top 20: usable={sum(1 for s in top if s['tier']>=1)/20:.0%}, good={sum(1 for s in top if s['tier']==2)/20:.0%}")

good = [s['qscore'] for s in skills if s['tier'] == 2]
bad = [s['qscore'] for s in skills if s['tier'] == 0]
print(f"Mean score good={statistics.mean(good):.3f} bad={statistics.mean(bad):.3f} separation={statistics.mean(good)-statistics.mean(bad):.3f}")

"""Render the audit report from the preserved measurements, without running Cadence."""
import gzip
import hashlib
import json
from pathlib import Path

P = Path(__file__).resolve().parent
result = json.loads((P / "zoo-results.json").read_text())
body = json.loads(gzip.decompress((P / "nursery-current-three-seeds.json.gz").read_bytes()))["body"]
sha = "750c8ef45b17ba052279584e49c685ff3d169a82"
base = f"https://github.com/muellerberndt/cadence/blob/{sha}/"
text = r"""# Cadence through the EFMW Zoo

**Verdict: Cadence demonstrates a working, bounded system for recurrent settlement, memory and adaptation. This audit supports that engineering claim. It does not establish a general world model, universal convergence, an EFMW derivation, or a general efficiency advantage.**

The strongest new result is a current-source, three-seed ablation: the complete `live` system acquired, reversed and returned successfully in every tested life. Removing associative memory reduced mean reversal accuracy from 100% to 61%. Freezing actor learning reduced it to 91.3%, with one life failing reversal and return. Both observations matter: associative memory is important here, and actor learning cannot be dismissed as unnecessary.

## Frozen target and method

- Review date: 2026-10-08.
- Repository: `muellerberndt/cadence`, revision `750c8ef45b17ba052279584e49c685ff3d169a82`, version 0.78.0. Target source remained unchanged and the checkout was clean after execution.
- Runtime: Python 3.12.14, NumPy 2.3.5, Linux x86_64; CPU, one worker, BLAS threads fixed to one. No accelerator validation was performed locally.
- Zoo source: `enuminous/Monolithic-Zoo-Lean4` at `94e0a9e2550a8fe62b03dc8213e3e3942c30899b`.
- Python adapters and EFMW equation catalogue: `enuminous/EFMW_Post156_Zoo_Audit` at `93c80ff4710e7fc61a84f21943149db550d4ee71`.
- **46-operation applicability review; two selected numerical operations executed.** CAT and RHINO produced 42 measured records. This is not a claim of 46 scientific passes. The selected adapters do not implement every part of every animal, and no new Lean compilation or Python–Lean equivalence proof was performed.
- `audit-protocol.json` was written before tests and the behavioral run; SHA-256 `e998a5630374beb91b3810457119fd48e5f7e9325ecd964a05b69153302cb221`. Seeds, arms, thresholds and budget were not changed after seeing results. This local freeze is not a public preregistration.

The scope is the default composed neural graph, its learning/memory contracts, and the odour reversal instrument. Other Cadence model families have different equations. The experimental population solver, temporal models and record-patch adjoints do not automatically certify the composed brain.

## What ran

**159 upstream tests passed; 28 optional Torch/MLX tests skipped.** The first group had 115 passes and 28 skips; the instrument and latest action-credit group had 44 passes. The first group emitted 22 warnings, preserved in its log. This was a focused audit, not a local full-suite or wheel certification.

Coverage included independently recomputed equation defects, original-equation damping, qualified teaching refusal, parameter/optimizer rollback, reward ownership, saved pending feedback, private imagination, checkpoint continuation, simple supervised acquisition, temperature-consistent policy credit, and reversal-instrument integrity. These are upstream-authored tests executed independently, not an independently rewritten implementation audit.

GitHub reported all nine jobs successful for the pinned revision: six test jobs across Linux/macOS and Python 3.11–3.13, plus three minimal-install jobs. That is observed upstream CI status, separate from our local execution.

The behavioral run used the upstream `odour_nursery.py` instrument without modification: five arms × three seeds (17001, 17002, 17003), 300 initial A trials, 600 B trials, then 600 returned-A trials. All arms in a seed received the same odour sequence, although their actions led to different witnessed outcomes. All 15 lives completed without crashes or refused answers. The receipt passed its canonical-form, digest, current-source and arithmetic verifier. That verifier checks the recorded summaries; it does not independently regenerate the full action history.

The operating point was the chamber's existing recipe: one 32-neuron processing module, working-trace amplitude 0.3, consolidation 0.25, actor rate 0.1 and actor-bias rate 0.01. These are **not all the public composition defaults**. No System 2 observers were added.

The unchanged gates require final optimal-action share ≥90%, stable-pair probes ≥95%, late arousal ≤20%, those readings in ≥90% of `live` lives, and median reversal lag ≤150 trials. The three `live` lives pass this bounded diagnostic. Three seeds at one exposure do not estimate general reliability or repeat the original 500-life confirmation census.

## Measured behavior

Numbers are mean optimal-action fractions in the last 100 trials of each phase. Lag is the first trial followed by a 40-action window with at least 90% optimal choices. It is not the time of permanent recovery. For medians below, failure to recover remains infinity rather than being silently dropped.

| Arm | Initial A | Reversal B | Returned A | Median B lag | Lives with a B recovery window |
| --- | ---: | ---: | ---: | ---: | ---: |
"""
for row in result["summary"]:
    a, b, c = row["mean_final_accuracy"]
    lag = row["reversal_lag_median_with_nonrecovery"]
    text += f"| `{row['arm']}` | {a:.1%} | {b:.1%} | {c:.1%} | {lag if lag is not None else 'not reached'} | {row['recovered_by_lag_definition']}/3 |\n"
text += r"""
`memory-only` means the actor's policy-learning rates are zero; its graph, critic and associative memory still exist. `graph-only` removes associative memory, not every kind of state. Neither name denotes a pure standalone mathematical model.

The complete `live` arm preserved the stable odour pair at every measured probe in all three phases. The actor-frozen seed 17003 ended reversal at 74% and return at 70%, despite becoming calm. The no-associative-memory arm averaged 61% in B, despite issuing qualified answers. These are concrete examples of why low residual and low arousal cannot certify external correctness.

The tabular baseline reached approximately 95% final accuracy, with epsilon 0.1 exploration still active. The `live` arm's greedy routine has a different exploration schedule. The apparent accuracy gap is not evidence of general representational superiority.

## Executed Zoo operations

### CAT: measured ablation loss

Purpose: test whether removing a component hurts behavior in this specified task. Inputs: paired losses `1 − final optimal-action fraction`, same seed and phase. Transformation: `ablated loss − full loss`. Output: signed penalty; a positive value means removal hurt. Criterion fixed before execution: interpret sign locally, with no significance or universal necessity claim.

| Removed component | B penalties, seeds 17001 / 17002 / 17003 | Mean B penalty | Returned-A penalties | Mean returned-A penalty |
| --- | --- | ---: | --- | ---: |
| Associative memory | +29 / +45 / +43 percentage points | +39.0 pp | +32 / +48 / 0 pp | +26.7 pp |
| Actor policy learning | 0 / 0 / +26 pp | +8.7 pp | 0 / 0 / +30 pp | +10.0 pp |

**Supported but incomplete:** associative memory makes a large contribution in this chamber. Actor learning also matters in one of these seeds. These interventions alter later experience through changed actions, so their effect is on the whole continuing life; they do not isolate a one-step synaptic mechanism or hold witnessed rewards identical.

### RHINO: retention, with an absolute-performance guard

Purpose: measure preservation of the unrelated stable odour skill during reversal and return. Inputs: first-A stable-pair probe fraction and the corresponding B/returned-A fraction. Transformation: the canonical clipped ratio `after / baseline`, including its defined zero-baseline branch. Output: retention plus raw scores. Criterion: the ratio must be interpreted alongside the original ≥95% absolute floor and an acquired baseline. The other RHINO operations were not run.

All six `live` phase comparisons have baseline 1, after 1, retention 1 and meet the absolute floor.

**A Zoo caution exposed by the actual data:** no-memory seed 17001 has first-A stable performance 0.125 and B performance 0.375. RHINO returns retention 1 after clipping, although the required skill is still poor. A perfect relative-retention score can preserve an inadequate baseline. The audit therefore keeps both raw scores and the absolute gate; it does not call this a pass.

## Work, with the denominator kept intact

Across the three `live` lives, the instrument counted 5,063 learning sweeps versus 58,059 for `step`: 91.3% fewer. Including routine, aroused, learning, probe and refused sweeps, totals were 166,023 versus 201,579: **17.6% fewer counted sweeps**, not 91.3% less total work. Mean whole-life wall time, including probes, was 4.98 versus 6.82 seconds in this one run. Memory writes were 491 versus 4,500.

Routine still cost approximately 32 neural sweeps per action. These observations support a reduction in selected work within this chamber; they do not measure joules, include every hardware operation, or establish asymptotic/scaling superiority. Wall times are order-dependent, unrepeated instrument timings. The tabular baseline took about 0.01 seconds per life and has a much lighter measurement path. Its zero neural sweeps do not mean zero computation.

## Evidence and failure boundaries

| Claim | Grade | Reason |
| --- | --- | --- |
| Returned composed-brain answers check the declared full neural equations | Demonstrated in selected tests and this run | Residual and refusal controls pass; the bounded run issued no refused answers. |
| A single retained brain can adapt across A→B→A and keep another simple skill | Demonstrated for this chamber and operating point | All three current-source `live` lives meet the specified readings. |
| Associative memory materially supports this behavior | Supported but incomplete | Paired CAT penalties are large; the task is a one-hot sensory-key lookup world. |
| Actor policy learning is unnecessary | Rejected as a blanket inference from this run | One actor-frozen life fails both later phases. |
| A small residual, a calm brain or a clipped retention score implies correct knowledge | Rejected | Qualified wrong answers, calm poor behavior and the low-baseline RHINO case provide counterexamples. |
| The default composed brain already integrates learned environmental transitions | Not implemented as the flagship contract at this revision | `imagine` evaluates supplied observations; transition prediction/planning lives in separate APIs. |
| Native transfer and broad continued knowledge are established | Unresolved; some narrower transfer claims fail their own gates | Published selected native recall is 18/24, while separate TRAIN/development results are 6/18 and 0/19 against 14/18 and 15/19 floors. These historical results were not rerun here. |
| The 360/360 partial-cue retention result is fresh independent confirmation | Rejected as a description of that evidence | It reused four acquired seed-0 specimens. Historical raw archives are partly external, and a full independent continuation audit remains outstanding. |
| Cadence is a generally better or more energy-efficient learner | Unresolved | No matched broad task/resource comparison or energy measurement in this audit. |
| Cadence validates EFMW physics or the universality thesis | Hypothesis only; no derivation supplied | Structural resemblance and behavioral tests do not identify a physical field law. |

The repository itself preserves failed controls and states many of these boundaries explicitly. This audit does not treat candidly declared research goals as already-made performance claims.

## EFMW correspondence: where a bridge is defensible

Cadence's rate-neuron rule has the form

```text
v_i(next) = v_i + dt * [ -v_i + sum_j W_ji * s(v_j) + drive_i + bias_i - k * a_i ]
```

with optional adaptation, and a bounded nonlinear activation. Its local equation agreement means each node satisfies its own consistency equation. It does **not** require all neurons to have the same state. Trace and associative-memory inputs are held during the composed graph solve and updated on their separate clocks. Action softmax and whole-graph residual reduction also impose group-level software operations.

| EFMW catalogue item | Candidate relation | Missing obligation |
| --- | --- | --- |
| ME-064, recursive state/observation/memory | Retained trace and associative memory condition later neural responses | Define the symbolic operators and an explicit state correspondence; resemblance is not equality. |
| ME-065, observer–observed closure | Optional observers exchange feedback within the neural graph | Map both state spaces and updates; prove closure for that composition. Ordinary memory stores are not all jointly equilibrated. |
| ME-031 / ME-032, attractor and perturbation recovery | Numerical settlement and behavioral A→B→A recovery give distinct finite observables | A finite successful solve is not an asymptotic stability theorem, and restoring behavior is not returning every parameter to its former value. |
| ME-069, cognitive attractor dynamics | Feedback-driven recurrent repair is a plausible candidate bridge | A directed nonlinear graph needs an energy/integrability argument before it can be identified with gradient flow. |
| ME-072, memory validation | Witnessed action outcomes change associations and future responses | Specify the update correspondence, error, clock and meaning of coherence. |
| ME-096, vanishing recursive increments | Cadence's equation residual is the stronger practical diagnostic | Vanishing increments alone do not prove convergence; the harmonic partial sums are a counterexample. |
| ME-002, physical scalar-field equation | No established correspondence | Supply physical quantities, units, spacetime/scaling limit, coefficients and external empirical predictions. A neural fixed point supplies none of these automatically. |

These references preserve the EFMW catalogue's own status distinctions: several are working constructs or symbolic relations, not established physical laws.

One useful proof obligation is precise: if a fixed-point map F is a contraction with constant q<1, then a returned defect ε bounds state error by ε/(1−q). Indeed, `||x−x*|| ≤ ||x−F(x)|| + ||F(x)−F(x*)|| ≤ ε + q||x−x*||`. This is a conditional standard argument, not a verified property of every Cadence graph. Without a contraction or another stability argument, the residual alone does not establish uniqueness, attraction or a uniform error bound. Learning-gradient claims additionally need the appropriate reciprocal effective weights, a smooth stable branch, and a justified nudge/settlement limit.

## Novelty check

The mechanism is **adjacent to established equilibrium learning**, not evidence of an unprecedented universal computational law. Scellier and Bengio's *Equilibrium Propagation* already uses free and nudged phases for local learning in energy-based models. Cadence's centered contrasts belong near that lineage; correspondence requires matching equations and assumptions. Bai, Kolter and Koltun's *Deep Equilibrium Models* also compute fixed-point representations, with implicit differentiation. Similar settlement architecture does not make their learning rules identical.

The engineering combination of continuing state, associative memory, arousal, explicit feedback ownership and residual-gated action is a useful object of study. An exhaustive prior-art or novelty claim was not established in this review.

## Anti-circularity and reproducibility

1. World rewards and optimal actions came from the declared environment, not from Cadence's own answers. New audit seeds were fixed before the run; no result was discarded or retuned.
2. These seeds are outside the instrument's declared development/diagnostic/confirmation sets. That does not prove they were unused in all prior private research, and it does not make the familiar task an unseen domain.
3. The five arms shared exogenous odours, not identical chosen-action outcomes. Ablations support this total intervention comparison only.
4. Published historical results, current documentation, CI, local tests and the new bounded run are separate evidence classes. Packaging an old result in version 0.78.0 does not rerun it.
5. A source hash verifies identity, not scientific truth. Some acquisition archives are explicitly `external_not_bundled`; this audit did not independently regenerate those trajectories.
6. An upstream summary omits missing recovery lags when reporting its successful-life median and prints the recovery count. Our derived table keeps nonrecoveries in the denominator. Thus actor-frozen B lag is 85 with 2/3 recovery, not the successful-only median 70.
7. No universal score combines dependent residuals, accuracy, calmness and retention into a new purported theorem. Unexecuted operations stay unexecuted.

## Next decisive test

**Test transfer that cannot be solved by a direct sensory-key lookup, using one continuing brain.** Freeze a small ordered-cue task in which the same current observation requires different actions after different histories, then introduce unseen cue combinations, reverse one relation and retain an unrelated skill. Use real executed outcomes and keep pending feedback through a save/reload seam.

A minimal next protocol would use 20 predeclared founders, the existing full, no-associative-memory and actor-frozen arms, plus a recurrent baseline with the same available history and outcome information. Freeze the generator, held-out combinations, capacity, training budget and analysis before outcomes are opened. Require ≥90% final accuracy and ≥95% stable-skill probes in at least 18/20 full-system lives. Charge training, traces, memory, probes, nudged phases, refused solves and complete elapsed work. Publish per-founder failures and paired comparisons; do not select the best founder or invent an external answer head. If development tuning is needed, it must use separate development data and new confirmation founders afterward.

This proposal has not been executed here. Its point is to distinguish retained relational learning from the direct association mechanism that already explains much of the present chamber. Integrated consequence prediction would require a further explicit implementation and prediction test.

## Reproduction

The evidence archive contains the pre-run protocol, raw test logs/XML, source-bound receipt, Zoo inputs and outputs, CI status snapshot, and the analysis/report scripts. To reproduce from the pinned checkouts with NumPy and pytest installed:

```bash
# In the Cadence checkout, at the exact revision named above:
export PYTHONPATH=src
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
python -m pytest -q tests/test_feedback_transaction.py tests/test_qualified_learning.py tests/test_damping_stagnation.py tests/test_settlement_reports.py tests/test_composed_acquisition.py tests/test_memory_imagination.py tests/test_generic_memory_checkpoint.py tests/test_policy_credit.py
python -m pytest -q tests/test_behavior_credit.py tests/test_arousal_slots.py benchmarks/reversal/test_nursery.py
timeout 600 python benchmarks/reversal/odour_nursery.py --arms live step memory-only graph-only tabular --seeds 17001 17002 17003 --exposures 300 --workers 1 --out /absolute/output/nursery-current-three-seeds.json.gz
python benchmarks/reversal/odour_nursery.py --verify /absolute/output/nursery-current-three-seeds.json.gz --current
# Place analyze.py beside the receipt, then:
python /absolute/output/analyze.py /absolute/path/to/EFMW_Post156_Zoo_Audit
```

Seeds, source and runtime fix the numerical experiment; elapsed times and compressed receipt identity can vary with platform and timing fields. The original receipt and its hashes remain the evidence for this run.

## Complete per-life endpoint ledger

Stable values are the fraction of probes where both stable odour choices are correct. Every row is retained.

| Arm | Seed | A / B / A final accuracy | A / B / A stable-pair probes | B / returned-A lag |
| --- | ---: | --- | --- | --- |
"""
for r in body["rows"]:
    phases = r["phases"]
    finals = " / ".join(f"{p['final']:.2f}" for p in phases)
    stable = " / ".join(f"{p['stable']:.3f}" for p in phases)
    lags = " / ".join(str(p["lag"]) if p["lag"] is not None else "not reached" for p in phases[1:])
    text += f"| `{r['arm']}` | {r['seed']} | {finals} | {stable} | {lags} |\n"
text += "\n## All 46 applicability decisions\n\nA missing input is not a failed scientific test. Operation meanings come from the frozen catalogue; animal names are not improvised review metaphors.\n\n| # | Animal | Status | Input boundary or result scope |\n| ---: | --- | --- | --- |\n"
for c in result["coverage"]:
    status = "Selected operation executed" if c["status"] == "selected_operation_executed" else "Not executed"
    text += f"| {c['id']} | {c['animal']} | {status} | {c['reason']} |\n"
text += "\n## Sources\n\n"
refs = [
    ("World-model scope", "docs/world-model.md"), ("Numerical and learning contracts", "docs/contracts.md"),
    ("Neuron equations", "src/cadence/neuron.py"), ("Graph residual implementation", "src/cadence/brain.py#L989-L1016"),
    ("Composed action and memory lifecycle", "src/cadence/generic.py#L1005-L1088"),
    ("Local learning equations", "docs/learning.md"), ("Reversal protocol and historical results", "benchmarks/reversal/README.md"),
    ("Reversal instrument", "benchmarks/reversal/odour_nursery.py"), ("Retention development boundary", "benchmarks/retention/README.md"),
    ("Acquisition failures and transfer boundary", "benchmarks/acquisition/README.md#L208-L246"),
    ("Historical viewer and external-archive limits", "benchmarks/acquisition/demo/README.md"),
]
for title, path in refs:
    text += f"- [{title}]({base}{path}).\n"
text += "- [Upstream CI run](https://github.com/muellerberndt/cadence/actions/runs/37770590718).\n"
text += "- [CAT source](https://github.com/enuminous/Monolithic-Zoo-Lean4/blob/94e0a9e2550a8fe62b03dc8213e3e3942c30899b/Cat.lean) and [RHINO source](https://github.com/enuminous/Monolithic-Zoo-Lean4/blob/94e0a9e2550a8fe62b03dc8213e3e3942c30899b/Rhino.lean).\n"
text += "- [Frozen EFMW catalogue](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/93c80ff4710e7fc61a84f21943149db550d4ee71/research_engine/data/equations.json) and [scoped Python operations](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/93c80ff4710e7fc61a84f21943149db550d4ee71/research_engine/kernels.py).\n"
text += "- Scellier and Bengio (2017), [Equilibrium Propagation](https://arxiv.org/abs/1602.05179v5).\n"
text += "- Bai, Kolter and Koltun (2019), [Deep Equilibrium Models](https://arxiv.org/abs/1909.01377v2).\n"
text += f"\nOriginal new-run receipt SHA-256: `{result['receipt_sha256']}`.\n"
(P / "CADENCE_ZOO_REVIEW.md").write_text(text)
print(f"Wrote {len(text.encode())} bytes to CADENCE_ZOO_REVIEW.md")

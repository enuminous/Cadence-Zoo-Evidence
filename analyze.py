"""Apply the frozen CAT/RHINO operations to the preserved Cadence receipt.

Usage: python analyze.py PATH_TO_AUDIT_RESEARCH_ENGINE
No learning, source modification, or threshold selection occurs here.
"""
import gzip
import hashlib
import json
import statistics
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ENGINE = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(ENGINE))
from research_engine.kernels import evaluate

receipt_path = HERE / "nursery-current-three-seeds.json.gz"
body = json.loads(gzip.decompress(receipt_path.read_bytes()))["body"]
rows = body["rows"]
by_key = {(r["arm"], r["seed"]): r for r in rows}
operations = []
for arm in ("graph-only", "memory-only"):
    for seed in body["seeds"]:
        for phase, label in ((1, "reversal B"), (2, "return A")):
            full = by_key["live", seed]["phases"][phase]["final"]
            ablated = by_key[arm, seed]["phases"][phase]["final"]
            inputs = {"full": 1.0-full, "ablated": 1.0-ablated}
            operations.append({"animal": "CAT", "arm": arm, "seed": seed,
                               "phase": label, "inputs": inputs,
                               "output": evaluate("CAT", inputs)})
for row in rows:
    if "error" in row:
        operations.append({"animal": "RHINO", "arm": row["arm"], "seed": row["seed"],
                           "status": "uncomputed_crashed_life", "error": row["error"]})
        continue
    baseline = row["phases"][0]["stable"]
    for phase, label in ((1, "reversal B"), (2, "return A")):
        after = row["phases"][phase]["stable"]
        inputs = {"baseline": baseline, "after": after}
        operations.append({"animal": "RHINO", "arm": row["arm"], "seed": row["seed"],
                           "phase": label, "inputs": inputs,
                           "output": evaluate("RHINO", inputs),
                           "absolute_floor_met": after >= .95,
                           "baseline_floor_met": baseline >= .95})

rankers = set("OWL OCTOPUS GECKO HIVE EAGLE CRAB SHEPHERD PULSE FOX SPIDER RAVEN DOLPHIN ANT MOTH SHARK PENGUIN DRAGON".split())
reasons = {
 "TORTOISE": "No prespecified per-outcome candidate/control Brier scores; accuracy is not Brier score.",
 "CAT": "Executed paired final-action-loss ablations; necessity is local to task, operating point and seeds.",
 "BAT": "No matched placebo Brier-score experiment; tabular accuracy is a baseline, not this kernel's inputs.",
 "HEDGEHOG": "No fresh family-disjoint held-out task panel; new RNG seeds in a known four-cue task are not domain transfer.",
 "CROCODILE": "Paired arms are available, but no preregistered difference-in-differences estimand or parallel-trend argument.",
 "TURTLE": "No separately normalized evidence groups or prespecified aggregate veto/admission policy.",
 "MAGPIE": "No groundedness time series and alarm history with an externally defined metric.",
 "WOLF": "No prespecified weighted local-channel measurements and EMA alarm thresholds.",
 "ELEPHANT": "Receipt/source hashes inspected; no active-event and lineage input schema for this operation.",
 "CHAMELEON": "No supplied distances separating structural change from measurement noise.",
 "JELLYFISH": "No stress/confidence/health propagation measurements or harm graph.",
 "BEAVER": "Rollback tests passed in selected cases; intervention effectiveness/collateral/verification scalars were not defined. Do not turn test counts into acceptance.",
 "MANTIS": "No calibrated precursor baseline or variance/autocorrelation/curvature z scores.",
 "BISON": "No queue/demand process in the scoped computation.",
 "WEASEL": "No independent severity-scored change-key findings supplied; a review is not this bounded filter.",
 "SALMON": "No unresolved-mass or ancestor event data; source pinning alone is insufficient.",
 "ORCA": "No agent handoff experiment or coordination metrics.",
 "MOLE": "Source exposes observability limits, but no quantitative relevance/coverage model was prespecified.",
 "LYNX": "Novelty literature reviewed qualitatively; no distance/yield metric for a numerical novelty verdict.",
 "HORSE": "No measured human-agent workload/trust/handoff experiment.",
 "TERMITE": "Cadence uses signed, rebased nonlinear neuron dynamics, not the specified scalar normalized-neighbor update. No correspondence proof.",
 "PHOENIX": "Recovery measured, but no fidelity/integrity/capability scalar schema and hold-window recovery tape for this operator.",
 "COBRA": "No independent proxy/true-objective divergence channels and confidence history.",
 "WHALE": "No prespecified baseline and history-window stability analysis; endpoint summaries are insufficient.",
 "FALCON": "Reversal lag retained, but no hazard deadline plus detection/intervention timing schema. Trial lag is not hardware latency.",
 "RHINO": "Executed stable-skill retention component with raw baselines and absolute .95 floor. Shock amplification and graceful-failure components not executed.",
 "BONOBO": "No multiple-agent utility/cooperation or exploitation measurements.",
 "AXOLOTL": "No independent invariant-retention and transformation/cost schema for regenerative score.",
 "BUTTERFLY": "No layered perturbation cascade under its specified clipped nonlinear step; recurrence alone is not equivalence.",
}
catalog = json.loads((ENGINE / "research_engine/data/zoo-coverage.json").read_text())
coverage = []
for entry in catalog:
    name = entry["name"]
    reason = reasons.get(name)
    if name in rankers:
        reason = "Selected adapter ranks supplied component columns; no validated Cadence feature/normalization/comparator matrix. A rank would not validate a mechanism."
    assert reason, name
    coverage.append({"id": entry["id"], "animal": name, "canonical_scope": entry["scope"],
                     "status": "selected_operation_executed" if name in ("CAT", "RHINO") else "not_executed",
                     "reason": reason})
assert len(coverage) == 46
summary = []
for arm in body["arms"]:
    group = [r for r in rows if r["arm"] == arm]
    good = [r for r in group if "error" not in r]
    lag = [r["phases"][1]["lag"] for r in good]
    # Unrecovered lives remain in the denominator and median calculation.
    median = statistics.median([float("inf") if x is None else x for x in lag])
    summary.append({"arm": arm, "lives": len(group), "crashes": len(group)-len(good),
                    "mean_final_accuracy": [statistics.mean(r["phases"][i]["final"] for r in good) for i in range(3)],
                    "reversal_lag_median_with_nonrecovery": None if median == float("inf") else median,
                    "recovered_by_lag_definition": sum(x is not None for x in lag),
                    "mean_seconds_including_probes": statistics.mean(r["seconds"] for r in group),
                    "total_counted_sweeps": sum(sum(r["work"][k] for k in ("sweeps_routine", "sweeps_aroused", "learning_sweeps", "probe_sweeps", "refused_sweeps")) for r in group),
                    "learning_sweeps": sum(r["work"]["learning_sweeps"] for r in group),
                    "memory_writes": sum(r["work"]["memory_writes"] for r in group)})
output = {"schema": "cadence-zoo-audit/1", "receipt_sha256": hashlib.sha256(receipt_path.read_bytes()).hexdigest(),
          "scope": "Two selected numerical operations, 46 applicability decisions. Not a 46-animal scientific pass.",
          "diagnostic_gates": body["gates"], "summary": summary, "operations": operations, "coverage": coverage}
(HERE / "zoo-results.json").write_text(json.dumps(output, indent=2, allow_nan=False)+"\n")
print(json.dumps(summary, indent=2))
print(f"Wrote {len(operations)} measured operation records; {len(coverage)} applicability decisions")

# Cadence Zoo Evidence

A reproducible EFMW Zoo audit of [Cadence](https://github.com/muellerberndt/cadence), pinned to version **0.78.0**, commit [`750c8ef45b17`](https://github.com/muellerberndt/cadence/tree/750c8ef45b17ba052279584e49c685ff3d169a82).

**Result:** bounded learning, adaptation and stable-skill retention were demonstrated in this test. General world-model capability, universal convergence and an EFMW physics derivation remain unproved.

[Open the results page](index.html) · [Read the full review](CADENCE_ZOO_REVIEW.md) · [Inspect the measurements](zoo-results.json) · [Download this repository](https://github.com/enuminous/Cadence-Zoo-Evidence/archive/refs/heads/main.zip)

## What was checked

| Check | Recorded result |
| --- | --- |
| Focused numerical, learning and lifecycle tests | **115 passed**, 28 optional Torch/MLX tests skipped |
| Reversal instrument and current action-credit tests | **44 passed** |
| Bounded behavioral run | **15 lives completed**, five arms × three seeds; no crashes or refused answers |
| Zoo applicability | **46 operation scopes reviewed**, two selected operations executed |
| Executed operations | CAT ablation-loss component and RHINO retention-ratio component; **42 measured records** |
| Receipt verification | Canonical form, digest, current source and recorded arithmetic agreed |

The 159 passing tests are upstream-authored tests executed locally, not a full local test-suite or accelerator certification. The receipt verifier checks the preserved summaries; it does not independently regenerate a complete action history. The 46 scope decisions are not 46 scientific passes. Unexecuted operations and missing measurements are retained in the [complete review](CADENCE_ZOO_REVIEW.md#all-46-applicability-decisions).

## Main findings

Each arm used one continuing life: **300 trials under A → 600 under B → 600 under A again**. The seeds were **17001, 17002 and 17003**, fixed before execution. Values below are mean optimal-action fractions over the last 100 trials of each phase.

| Arm | Initial A | Reversal B | Returned A |
| --- | ---: | ---: | ---: |
| Complete `live` brain | 100.0% | 100.0% | 100.0% |
| Always-learning `step` | 87.3% | 97.3% | 87.0% |
| Actor policy learning frozen (`memory-only`) | 100.0% | 91.3% | 90.0% |
| Associative memory removed (`graph-only`) | 65.3% | 61.0% | 73.3% |
| Tabular Q-learning baseline | 94.0% | 95.3% | 95.3% |

- **CAT — ablation:** removing associative memory cost 39 percentage points of mean reversal accuracy. Freezing actor learning also failed one of three lives, so actor learning cannot be dismissed as unnecessary. These interventions compare whole lives: changed actions also change witnessed outcomes.
- **RHINO — retention:** all three complete brains retained the unrelated stable odour pair at every measured probe. A clipped retention ratio can conceal a weak baseline, so the audit also requires the original **95% absolute performance floor**.
- **Work accounting:** `live` used 91.3% fewer learning sweeps than `step`, but **17.6% fewer total counted sweeps** after acting and probes were included. Physical energy was not measured.

The tabular baseline keeps ε = 0.1 exploration active, while `live` can answer greedily during routine. The accuracy gap therefore does not establish general representational superiority. The `memory-only` arm retains a graph and a learning critic; `graph-only` retains working state. Their names are shorthand for the declared ablations.

This used the chamber's existing operating point: one 32-neuron processing module, working-trace amplitude 0.3, consolidation 0.25, actor rate 0.1 and actor-bias rate 0.01. These are **not all the public composition defaults**. Three seeds in one four-odour task do not establish broad reliability or transfer.

## Browse the page

`index.html` is a self-contained results page with:

- A phase selector for the five-arm comparison, plus an accessible table of all values.
- A searchable, filterable inventory of all 46 Zoo operation scopes.
- Explicit claim boundaries, provenance and links to the raw evidence.

Open it locally, or serve this repository without installing dependencies:

```bash
python -m http.server 8000 --bind 127.0.0.1
```

Then visit `http://127.0.0.1:8000/`. The evidence remains readable without JavaScript; JavaScript enables phase selection and filtering. There are no external fonts, analytics, build steps or network requests in the viewer itself.

The root page is ready for GitHub Pages. To enable it, use **Settings → Pages → Deploy from a branch → main → / (root)**. Adding these files does not itself enable hosting. GitHub's repository view shows HTML source; open the local or hosted page for the rendered interface.

The page displays the frozen audit snapshot from `zoo-results.json`; it does not run Cadence or fetch new results. If measurements change in a later audit, update the displayed snapshot alongside its source evidence.

## Evidence map

| File | Purpose |
| --- | --- |
| [CADENCE_ZOO_REVIEW.md](CADENCE_ZOO_REVIEW.md) | Complete findings, per-life ledger, EFMW correspondence, proof obligations, novelty discussion and 46 applicability decisions |
| [audit-protocol.json](audit-protocol.json) | Pre-run target, seeds, arms, gates, operation definitions and work-accounting rules |
| [nursery-current-three-seeds.json.gz](nursery-current-three-seeds.json.gz) | Original source-bound behavioral receipt, including per-life results |
| [nursery-run.log](nursery-run.log) | Run summary and receipt-verification output |
| [zoo-results.json](zoo-results.json) | Derived arm summaries, CAT/RHINO input-output records and full applicability inventory |
| [focused-tests.log](focused-tests.log), [focused-tests.xml](focused-tests.xml) | Numerical and lifecycle results, optional-backend skips and captured warnings |
| [instrument-tests.log](instrument-tests.log), [instrument-tests.xml](instrument-tests.xml) | Reversal-instrument and action-credit test results |
| [upstream-ci.json](upstream-ci.json) | Observed upstream CI status for the pinned revision, separate from local tests |
| [analyze.py](analyze.py) | Applies the frozen audit engine's CAT and RHINO operations to the receipt |
| [build_report.py](build_report.py) | Rebuilds the Markdown report from preserved measurements and audit interpretation |
| [MANIFEST.json](MANIFEST.json) | SHA-256 hashes and byte counts for the 12 original capsule files |
| [index.html](index.html), [readme.md](readme.md) | Navigation and presentation added around the original evidence capsule |

The original manifest is preserved. It covers the original capsule, not itself or these subsequently added presentation files. Git history records the additions. A matching hash establishes byte identity, not scientific validity.

## Verify the original capsule

Run from this repository's root with Python 3.11 or newer. This checks the original recorded files without running a simulation:

```bash
python - <<'PY'
import hashlib
import json
from pathlib import Path

manifest = json.loads(Path('MANIFEST.json').read_text())
failures = []
for item in manifest['files']:
    path = Path(item['name'])
    if not path.is_file():
        failures.append(f'{path}: missing')
        continue
    data = path.read_bytes()
    if len(data) != item['bytes'] or hashlib.sha256(data).hexdigest() != item['sha256']:
        failures.append(f'{path}: byte count or SHA-256 mismatch')
if failures:
    raise SystemExit('\n'.join(failures))
print(f"Verified {len(manifest['files'])} original files")
PY
```

## Reproduce the behavioral run

The original local runtime was **Python 3.12.14, NumPy 2.3.5, pytest 9.1.1, Linux x86_64**, with one worker and one BLAS thread. Optional Torch/MLX backends were absent. Platform and dependency changes may affect behavior and timing.

From this evidence repository, use a separate Cadence checkout and a fresh output directory:

```bash
git clone https://github.com/muellerberndt/cadence.git ../cadence-source
git -C ../cadence-source checkout 750c8ef45b17ba052279584e49c685ff3d169a82
python -m venv ../cadence-env
../cadence-env/bin/python -m pip install 'numpy==2.3.5' 'pytest==9.1.1' -e ../cadence-source
mkdir reproduction

OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 \
../cadence-env/bin/python ../cadence-source/benchmarks/reversal/odour_nursery.py \
  --arms live step memory-only graph-only tabular \
  --seeds 17001 17002 17003 --exposures 300 --workers 1 \
  --out reproduction/nursery-current-three-seeds.json.gz

../cadence-env/bin/python ../cadence-source/benchmarks/reversal/odour_nursery.py \
  --verify reproduction/nursery-current-three-seeds.json.gz --current
```

The original execution used a 600-second external timeout. For the same bound on systems providing GNU `timeout`, prefix the simulation invocation with `timeout 600`. Keep reruns separate from the original capsule; new receipt hashes can differ because timing and platform fields are included.

To derive the Zoo results for that new receipt:

```bash
git clone https://github.com/enuminous/EFMW_Post156_Zoo_Audit.git ../cadence-audit-engine
git -C ../cadence-audit-engine checkout 93c80ff4710e7fc61a84f21943149db550d4ee71
cp analyze.py reproduction/analyze.py
../cadence-env/bin/python reproduction/analyze.py ../cadence-audit-engine
```

The full review contains the exact focused pytest commands. `analyze.py` derives results from a receipt; it does not rerun learning. `build_report.py` renders the fixed audit narrative and measurements; it is not a validator or an automatic report writer for arbitrary new experiments.

## Pinned sources and interpretation

| Source | Revision |
| --- | --- |
| [Cadence runtime](https://github.com/muellerberndt/cadence/tree/750c8ef45b17ba052279584e49c685ff3d169a82) | `750c8ef45b17ba052279584e49c685ff3d169a82` |
| [Zoo source catalogue](https://github.com/enuminous/Monolithic-Zoo-Lean4/tree/94e0a9e2550a8fe62b03dc8213e3e3942c30899b) | `94e0a9e2550a8fe62b03dc8213e3e3942c30899b` |
| [Audit engine and EFMW catalogue](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/tree/93c80ff4710e7fc61a84f21943149db550d4ee71) | `93c80ff4710e7fc61a84f21943149db550d4ee71` |

Cadence's local repair, retained memory and feedback offer concrete mechanisms to compare with EFMW's cognitive constructs. Structural resemblance does not establish equation identity, a physical field law, or a universality theorem. Selected numerical adapters are not complete animal pipelines, and this audit did not compile the Lean catalogue or prove Python–Lean equivalence.

**Next decisive experiment:** history-dependent transfer to unseen cue combinations, using the same continuing brain, matched information, retained old skills and complete work accounting. That experiment is proposed, not executed in this record.

Audit date: **8 October 2026**. Original evidence remains available alongside all recorded limitations and failures.

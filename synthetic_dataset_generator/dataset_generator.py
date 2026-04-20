"""
Generate the full 20-paper synthetic REE dataset.
Run: python dataset_generator.py
For a single test paper: python dataset_generator.py --test
"""

import json
import os
import sys
from collections import Counter
from paper_generator import generate_paper, OUTPUT_DIR

N_TOTAL        = 20
N_SINGLE_COL   =  4   # the rest will be double (enforced via post-check, not pre-assign)


def run(n=N_TOTAL, test_only=False):
    results = []
    papers = ["syn_001"] if test_only else [f"syn_{i:03d}" for i in range(1, n + 1)]
    allow_2pg = not test_only  # skip across_2_pages for test PDF

    for pid in papers:
        gt = generate_paper(pid, allow_across_2_pages=allow_2pg)
        results.append(gt)

    if test_only:
        print("Test PDF written to synthetic_dataset/pdfs/syn_001.pdf")
        print("GT JSON written to synthetic_dataset/ground_truth/syn_001_gt.json")
        return

    # ── Summary ────────────────────────────────────────────────────────────────
    layouts = Counter(r["layout"] for r in results)
    class_counts = Counter()
    total_figs = 0
    total_tbls = 0
    for r in results:
        total_figs += len(r["figures"])
        total_tbls += len(r["tables"])
        for fig in r["figures"]:
            class_counts[fig["figure_type"]] += 1

    summary = {
        "total_papers":      len(results),
        "single_column":     layouts.get("single", 0),
        "double_column":     layouts.get("double", 0),
        "total_figures":     total_figs,
        "total_tables":      total_tbls,
        "class_distribution": dict(class_counts),
    }

    summary_path = os.path.join(OUTPUT_DIR, "dataset_summary.json")
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    print("\n=== Dataset Summary ===")
    for k, v in summary.items():
        print(f"  {k}: {v}")
    print(f"\nSummary written to {summary_path}")


if __name__ == "__main__":
    test_only = "--test" in sys.argv
    run(test_only=test_only)

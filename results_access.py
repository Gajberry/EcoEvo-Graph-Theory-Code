from pathlib import Path

import numpy as np


def _read_number(output_name, results_loc, prefix):
    path = Path(results_loc) / f"{output_name}.txt"
    with path.open() as file:
        for line in file:
            if line.startswith(prefix):
                return float(line[len(prefix):])
    raise ValueError(f"{prefix!r} not found in {path}")


def get_fix_prob_weighted(output_name, results_loc):
    return _read_number(output_name, results_loc, "Overall weighted fixation probability: ")


def get_sample_size_weighted(output_name, results_loc):
    return _read_number(output_name, results_loc, "Number of samples: ")


def get_ci_weighted(fix_prob, sample_size):
    return 1.96 * np.sqrt(fix_prob * (1 - fix_prob) / sample_size)

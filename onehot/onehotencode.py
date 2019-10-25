
import scipy.sparse
import numpy as np


def onehotencode(xencoded: np.ndarray,
                 mapping: dict) -> scipy.sparse.lil_matrix:

    out = scipy.sparse.lil_matrix(
        (len(xencoded), len(mapping)), dtype=int)

    enc = list(mapping.keys())

    for i, j in enumerate(xencoded):
        if j in enc:
            out[i, j] = 1

    return out

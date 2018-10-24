
import scipy.sparse


def onehotencode(xencoded, mapping):

    out = scipy.sparse.lil_matrix(
        (len(xencoded), len(mapping)), dtype=int)

    enc = list(mapping.keys())

    for i, j in enumerate(xencoded):
        if j in enc:
            out[i, j] = 1

    return out

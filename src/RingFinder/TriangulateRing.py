import numpy as np
from .TriangulatePolygonLib import polygon_triangulate, polygon_area


def triangulate(pos, ring_idx):
    center = np.mean(pos, axis=0)

    # https://math.stackexchange.com/a/99317
    svd = np.linalg.svd((pos - center).T)
    left = svd[0]
    normal = left[:, -1] / np.linalg.norm(left[:, -1])

    # https://stackoverflow.com/a/23474396
    assert not np.allclose(normal, 0)
    ind = np.nonzero(normal)[0][0]
    e1 = normal.copy()
    e1[ind] *= -1
    e1 = np.cross(e1, normal)
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(normal, e1)
    e2 /= np.linalg.norm(e2)

    assert np.isclose(np.dot(normal, e1), 0)
    assert np.isclose(np.dot(normal, e2), 0)
    assert np.isclose(np.dot(e1, e2), 0)

    proj_pos = np.zeros((len(pos), 2))
    for i in range(len(pos)):
        proj_pos[i, 0] = np.dot(e1, pos[i] - center)
        proj_pos[i, 1] = np.dot(e2, pos[i] - center)

    if polygon_area(len(proj_pos), proj_pos[:, 0], proj_pos[:, 1]) > 0:
        tri = polygon_triangulate(len(proj_pos), proj_pos[:, 0], proj_pos[:, 1])
        return ring_idx[tri]
    else:
        proj_pos = np.flipud(proj_pos)
        tri = polygon_triangulate(len(proj_pos), proj_pos[:, 0], proj_pos[:, 1])
        return np.flipud(ring_idx)[tri]

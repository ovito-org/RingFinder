from pathlib import Path

import numpy as np
import pytest
from ovito.io import import_file
from ovito.modifiers import ShrinkWrapSimulationBoxFunction
from RingFinder import RingFinder


@pytest.fixture()
def setup_pipeline():
    pipeline = import_file(Path("examples", "231D.pdb"))
    pipeline.modifiers.append(ShrinkWrapSimulationBoxFunction)
    return pipeline


@pytest.fixture(scope="module")
def setup_pipeline_cache():
    pipeline = import_file(Path("examples", "231D.pdb"))
    pipeline.modifiers.append(ShrinkWrapSimulationBoxFunction)
    return pipeline


@pytest.fixture(scope="module")
def setup_data(setup_pipeline_cache):
    pipeline = setup_pipeline_cache
    pipeline.modifiers.append(RingFinder(min_size=5, max_size=6))
    return pipeline.compute()


def sort_2d_array(array):
    assert array.ndim == 2
    array = np.sort(array, axis=1)
    ind = np.lexsort([array[:, i] for i in reversed(range(array.shape[1]))])
    return array[ind]


def test_global_attributes(setup_data):
    data = setup_data
    assert data.attributes["RingCount"] == 23
    assert data.attributes["5-RingCount"] == 13
    assert data.attributes["6-RingCount"] == 10


def test_ring_sizes_tables(setup_data):
    data = setup_data
    ref = np.zeros((7, 2))
    ref[5, 1] = 13
    ref[6, 1] = 10
    ref[:, 0] = np.arange(7)
    assert np.all(data.tables["ring-size-histogram"].xy() == ref)


def test_ring_count_tables(setup_data):
    data = setup_data
    ref_5 = np.array(
        (
            (2, 3, 7, 6, 4),
            (21, 23, 25, 26, 22),
            (27, 28, 29, 30, 37),
            (43, 44, 48, 47, 45),
            (49, 58, 52, 51, 50),
            (64, 65, 69, 68, 66),
            (84, 85, 89, 88, 86),
            (103, 104, 108, 107, 105),
            (109, 110, 111, 112, 119),
            (121, 122, 123, 124, 125),
            (134, 135, 136, 137, 138),
            (147, 151, 150, 149, 148),
            (160, 164, 163, 162, 161),
        ),
        dtype=int,
    )
    ref_6 = np.array(
        (
            (8, 9, 11, 12, 14, 15),
            (30, 31, 33, 34, 36, 37),
            (52, 58, 57, 56, 55, 53),
            (70, 71, 73, 74, 76, 78),
            (90, 97, 96, 94, 93, 91),
            (112, 119, 118, 116, 115, 113),
            (127, 133, 132, 130, 129, 128),
            (140, 141, 142, 143, 145, 146),
            (153, 154, 155, 156, 158, 159),
            (166, 172, 171, 169, 168, 167),
        ),
        dtype=int,
    )
    sample_5 = np.asarray(data.tables["5-rings"]["Particle Indices"])
    sample_6 = np.asarray(data.tables["6-rings"]["Particle Indices"])
    assert np.all(sort_2d_array(ref_5) == sort_2d_array(sample_5))
    assert np.all(sort_2d_array(ref_6) == sort_2d_array(sample_6))


def test_ring_mesh_vertices(setup_data):
    data = setup_data
    ref = np.array(
        (
            (15.258, -4.047, 27.45),
            (16.168, -3.578, 26.449),
            (15.511, -5.558, 27.551),
            (16.985, -5.609, 27.244),
            (17.155, -4.569, 26.155),
            (18.502, -3.952, 26.071),
            (18.742, -2.592, 26.326),
            (19.992, -2.093, 26.218),
            (20.986, -2.901, 25.879),
            (20.786, -4.289, 25.643),
            (19.521, -4.757, 25.718),
            (11.383, -8.939, 26.668),
            (11.09, -10.318, 26.418),
            (10.695, -8.57, 28.003),
            (10.958, -9.858, 28.741),
            (10.804, -10.937, 27.686),
            (11.676, -12.095, 27.881),
            (13.006, -12.175, 28.127),
            (13.455, -13.388, 28.228),
            (12.327, -14.147, 27.998),
            (12.165, -15.543, 27.954),
            (10.864, -15.882, 27.664),
            (9.867, -14.99, 27.45),
            (9.983, -13.69, 27.556),
            (11.252, -13.352, 27.796),
            (5.585, -10.865, 29.354),
            (6.433, -12.044, 29.406),
            (5.171, -10.494, 30.79),
            (6.401, -11.052, 31.508),
            (6.723, -12.334, 30.774),
            (8.111, -12.788, 30.988),
            (9.219, -12.072, 31.384),
            (10.299, -12.805, 31.516),
            (9.881, -14.099, 31.128),
            (10.543, -15.36, 31.032),
            (9.838, -16.428, 30.633),
            (8.579, -16.207, 30.296),
            (7.817, -15.129, 30.38),
            (8.552, -14.074, 30.791),
            (3.106, -14.559, 32.755),
            (4.533, -14.514, 32.529),
            (2.827, -14.428, 34.266),
            (4.18, -14.761, 34.846),
            (5.089, -15.104, 33.682),
            (6.496, -14.728, 33.943),
            (7.429, -15.74, 33.917),
            (8.703, -15.451, 34.288),
            (9.172, -14.224, 34.649),
            (8.136, -13.185, 34.644),
            (6.866, -13.458, 34.316),
            (3.441, -18.674, 37.043),
            (4.791, -18.206, 36.802),
            (3.122, -18.513, 38.516),
            (4.17, -17.546, 38.963),
            (5.339, -17.869, 38.081),
            (6.315, -16.772, 38),
            (7.633, -17.072, 37.834),
            (8.56, -16.1, 37.838),
            (8.216, -14.828, 37.928),
            (6.844, -14.476, 38.028),
            (5.957, -15.459, 38.117),
            (2.785, -19.888, 44.108),
            (4.215, -19.776, 44.209),
            (2.224, -18.972, 45.173),
            (3.209, -19.31, 46.247),
            (4.568, -19.359, 45.535),
            (5.236, -18.045, 45.506),
            (4.648, -16.823, 45.379),
            (5.476, -15.84, 45.339),
            (6.723, -16.448, 45.376),
            (8.024, -15.879, 45.368),
            (9.012, -16.803, 45.42),
            (8.783, -18.126, 45.498),
            (7.58, -18.702, 45.517),
            (6.585, -17.801, 45.46),
            (10.463, -14.756, 41.32),
            (11.517, -13.885, 41.109),
            (11, -12.523, 41.019),
            (9.687, -12.582, 41.154),
            (9.334, -13.976, 41.372),
            (6.908, -13.433, 41.699),
            (6.536, -12.96, 42.954),
            (5.555, -12.058, 43.112),
            (4.846, -11.479, 42.004),
            (5.241, -11.96, 40.748),
            (6.239, -12.86, 40.583),
            (8.526, -16.825, 41.69),
            (7.667, -15.777, 41.713),
            (6.345, -16.275, 41.88),
            (6.429, -17.618, 42.022),
            (7.805, -17.993, 41.916),
            (7.342, -20.355, 42.098),
            (6.835, -21.027, 43.189),
            (5.915, -22.041, 42.982),
            (5.428, -22.424, 41.691),
            (5.989, -21.69, 40.63),
            (6.896, -20.712, 40.808),
            (10.688, -18.835, 41.737),
            (9.659, -19.71, 41.932),
            (10.167, -21.062, 42.002),
            (11.48, -20.981, 41.937),
            (11.832, -19.59, 41.741),
            (14.271, -20.137, 41.574),
            (14.388, -21.087, 40.515),
            (15.375, -22.016, 40.531),
            (16.256, -22.169, 41.604),
            (16.048, -21.258, 42.685),
            (15.075, -20.337, 42.684),
            (12.638, -16.718, 41.259),
            (13.504, -17.783, 41.313),
            (14.825, -17.263, 41.122),
            (14.748, -15.91, 40.989),
            (13.365, -15.547, 41.08),
            (13.762, -13.131, 40.749),
            (14.12, -12.755, 39.471),
            (14.931, -11.665, 39.278),
            (15.432, -10.851, 40.335),
            (14.973, -11.249, 41.602),
            (14.178, -12.316, 41.817),
        ),
    )
    sample = np.asarray(data.surfaces["rings"].vertices["Position"])
    assert np.all(sort_2d_array(ref) == sort_2d_array(sample))


def test_ring_mesh_faces(setup_data):
    data = setup_data
    ref = np.array(
        (5, 6, 5, 5, 6, 5, 5, 6, 5, 6, 5, 6, 5, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6),
        dtype=int,
    )
    sample = np.asarray(data.surfaces["rings"].faces["Ring Size"])
    assert np.all(np.sort(ref) == np.sort(sample))


def test_multiple_invocations(setup_pipeline):
    pipeline = setup_pipeline
    pipeline.modifiers.append(RingFinder(min_size=5, max_size=6))
    pipeline.modifiers.append(RingFinder(min_size=5, max_size=6))
    pipeline.modifiers.append(RingFinder(min_size=5, max_size=6))
    data = pipeline.compute()
    suffix = []
    for key in data.tables.keys():
        print(key)
        if not key.startswith("ring-size-histogram"):
            continue
        if key == "ring-size-histogram":
            suffix.append(0)
        else:
            suffix.append(int(key.split(".")[1]))

    assert len(suffix) == 3
    assert np.all(np.sort(suffix) == np.array([0, 1, 2]))


def test_min_max_size(setup_pipeline_cache):
    pipeline = setup_pipeline_cache
    pipeline.modifiers.append(RingFinder(min_size=7, max_size=6))
    with pytest.raises(RuntimeError):
        pipeline.compute()

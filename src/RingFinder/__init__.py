#### Ring Finder ####
# Find and visualize bond rings in molecular structures.
#
# Documentation: https://github.com/ovito-org/RingFinder

from collections import defaultdict, deque

import numpy as np
from ovito.data import BondsEnumerator, DataCollection, DataTable
from ovito.pipeline import ModifierInterface
from ovito.traits import OvitoObject
from ovito.vis import SurfaceMeshVis
from traits.api import Bool, Int

from .TriangulateRing import triangulate


class RingFinder(ModifierInterface):
    min_size = Int(3, label="Minimum ring size")
    max_size = Int(9, label="Maximum ring size")
    mesh_vis = OvitoObject(SurfaceMeshVis, show_cap=False, title="Rings")
    create_mesh = Bool(True, label="Create polygons")
    triangulate_facets = Bool(False, label="Triangulate polygons")

    def bfs(self, data, start):
        bonds_enum = BondsEnumerator(data.particles.bonds)
        topo = data.particles.bonds.topology

        q = deque()
        labels = defaultdict(lambda: [-1, -1, 0])

        labels[start] = [start, 0, 1]
        q.append(start)

        max_iter = 10000
        loop = 0
        while q:
            v = q.popleft()
            if v in labels and labels[v][1] == int(np.ceil(self.max_size / 2)):
                continue

            for bond_index in bonds_enum.bonds_of_particle(v):
                neigh = (
                    topo[bond_index, 0]
                    if topo[bond_index, 0] != v
                    else topo[bond_index, 1]
                )
                if labels[v][0] == neigh:
                    continue
                if neigh in labels:
                    continue

                labels[neigh][0] = v
                labels[neigh][1] = labels[v][1] + 1
                q.append(neigh)
            if loop == max_iter:
                raise RuntimeError(
                    "Iteration limit reached in bfs algorithm. This should never happen. Please report this error by opening an issue at https://github.com/ovito-org/RingFinder/issues."
                )
            loop += 1
        return labels

    @staticmethod
    def visualize_labels(data, labels):
        distances = np.zeros(data.particles.count, dtype=int)
        parents = np.zeros(data.particles.count, dtype=int)
        for i in range(data.particles.count):
            distances[i] = labels[i][1]
            parents[i] = labels[i][0]
        data.particles_.create_property("distance", data=distances)
        data.particles_.create_property("parent", data=parents)

    @staticmethod
    def validate_antipodes(labels, ring):
        if len(ring) % 2 == 0:
            d0 = len(ring) // 2
            for i in range(d0):
                assert ring[i] in labels
                assert ring[i + d0] in labels[ring[i]]
                if labels[ring[i]][ring[i + d0]][1] != d0:
                    return False
        else:
            d0 = int(np.floor(len(ring) // 2))
            d1 = d0 + 1
            for i in range(d0):
                assert ring[i] in labels
                assert ring[i + d0] in labels[ring[i]]
                assert ring[i + d1] in labels[ring[i]]
                if labels[ring[i]][ring[i + d0]][1] != d0:
                    return False
                if labels[ring[i]][ring[i + d1]][1] != d0:
                    return False
            i = d0
            assert ring[i + d0] in labels[ring[i]]

            if labels[ring[i]][ring[i + d0]][1] != d0:
                return False
        return True

    @staticmethod
    def done_atom_on_path(labels, start, atom):
        parent = labels[start][atom][0]
        maxiter = 1000
        loop = 0
        while parent != labels[start][parent][0]:
            if parent < start:
                return True
            parent = labels[start][parent][0]
            if loop == maxiter:
                raise RuntimeError(
                    "Iteration limit reached in path search algorithm. This should never happen. Please report this error by opening an issue at https://github.com/ovito-org/RingFinder/issues."
                )
            loop += 1
        return False

    def find_rings(self, data, labels, start):
        assert start in labels
        bonds_enum = BondsEnumerator(data.particles.bonds)
        topo = data.particles.bonds.topology
        q = deque()
        q.append(start)
        rings = []
        max_iter = 10000
        loop = 0
        while q:
            v = q.popleft()
            assert v in labels[start]
            if labels[start][v][2] and labels[start][v][1] == int(
                np.ceil(self.max_size / 2)
            ):
                continue
            for bond_index in bonds_enum.bonds_of_particle(v):
                neigh = (
                    topo[bond_index, 0]
                    if topo[bond_index, 0] != v
                    else topo[bond_index, 1]
                )
                assert neigh in labels[start]
                if (
                    labels[start][v][0] == neigh
                    or neigh < start
                    or self.done_atom_on_path(labels, start, labels[start][v][0])
                ):
                    continue
                if labels[start][neigh][2]:
                    inner = neigh
                    ring = []
                    for _ in range(labels[start][inner][1] + 1):
                        ring.append(inner)
                        inner = labels[start][inner][0]
                    ring.reverse()
                    inner = v
                    for _ in range(labels[start][inner][1] + 1):
                        if inner in ring:
                            break
                        ring.append(inner)
                        inner = labels[start][inner][0]
                    if (
                        len(ring) == labels[start][v][1] + labels[start][neigh][1] + 1
                        and start in ring
                        and tuple([ring[0]] + ring[-1:0:-1]) not in rings
                        and self.min_size <= len(ring) <= self.max_size
                        and not any(vert < start for vert in ring)
                    ):
                        if self.validate_antipodes(labels, ring):
                            rings.append(tuple(ring))
                    continue

                labels[start][neigh][2] = 1
                q.append(neigh)
            if loop == max_iter:
                raise RuntimeError(
                    "Iteration limit reached in find rings algorithm. This should never happen. Please report this error by opening an issue at https://github.com/ovito-org/RingFinder/issues."
                )
            loop += 1
        return rings

    def prepare_mesh(self, data: DataCollection, rings: list):
        suffix = self.get_suffix(data)

        uni = set()
        for ring in rings:
            for r in ring:
                uni.add(r)
        uni = np.asarray(list(uni))
        if len(uni) == 0:
            return
        uni.sort()

        positions = data.particles["Position"][uni]

        if self.triangulate_facets:
            faces = []
            ring_sizes = []
            for i, ring in enumerate(rings):
                buffer = np.zeros((len(ring), 4))

                for j, r in enumerate(ring):
                    if j > 0:
                        buffer[j, :3] = buffer[j - 1, :3] + data.particles.delta_vector(
                            ring[j], ring[j - 1], data.cell
                        )
                    buffer[j, 3] = np.searchsorted(uni, r)
                faces.append(triangulate(buffer[:, :3], buffer[:, 3]))
                ring_sizes.append([len(ring)] * len(faces[-1]))
                yield i / len(rings)
            ring_sizes = np.concatenate(ring_sizes)
            faces = np.concatenate(faces)
        else:
            ring_vert_count = sum(len(r) for r in rings)
            faces = np.zeros(ring_vert_count + len(rings), dtype=int)
            ring_sizes = np.zeros(len(rings), dtype=int)
            i = j = 0
            for ring in rings:
                faces[i] = len(ring)
                ring_sizes[j] = len(ring)
                j += 1
                i += 1
                for r in ring:
                    faces[i] = np.searchsorted(uni, r)
                    assert uni[faces[i]] == r
                    i += 1
                yield i / len(faces)
            assert i == len(faces)

        mesh = data.surfaces.create(
            identifier=f"rings{suffix}",
            title=f"Rings{suffix}",
            domain=data.cell,
            vis=self.mesh_vis,
        )
        mesh.create_vertices(positions)
        mesh.create_faces(faces)
        mesh.faces_.create_property("Ring Size", data=ring_sizes)

    def create_tables_attributes(self, data: DataCollection, rings: list):
        suffix = self.get_suffix(data)

        data.attributes[f"RingCount{suffix}"] = len(rings)
        rings_dict = {}
        for ring in rings:
            size = len(ring)
            if size not in rings_dict:
                rings_dict[size] = []
            rings_dict[size].append(ring)

        # Create data tables and attributes
        counts = np.zeros(self.max_size + 1, dtype=np.int64)
        for size in range(self.min_size, self.max_size + 1):
            if size in rings_dict:
                ring_list = rings_dict[size]
                counts[size] = len(ring_list)
            else:
                ring_list = None
                counts[size] = 0
            data.attributes[f"{size}-RingCount{suffix}"] = int(counts[size])
            table = data.tables.create(
                identifier=f"{size}-rings{suffix}",
                title=f"{size}-ring list{suffix}",
                plot_mode=DataTable.PlotMode.NoPlot,
            )
            table.x = table.create_property(
                "Particle Indices", data=ring_list, dtype=np.int64, components=size
            )

        # Ring size histogram
        table = data.tables.create(
            identifier=f"ring-size-histogram{suffix}",
            plot_mode=DataTable.PlotMode.BarChart,
            title=f"Ring size histogram{suffix}",
        )
        table.x = table.create_property(
            "Ring Size", data=[i for i in range(0, self.max_size + 1)]
        )
        for i in range(self.min_size, self.max_size + 1):
            table.x.add_type_id(i, table, name=f"{i}").color = (1.0, 1.0, 1.0)
        table.y = table.create_property(
            "Counts",
            data=counts,
        )

    def get_suffix(self, data):
        max_count = -1
        for key in data.attributes:
            if key.startswith("RingCount"):
                key = key.split(".")
                if len(key) == 1:
                    max_count = 0
                else:
                    count = int(key[-1])
                    if count > max_count:
                        max_count = count
        if max_count != -1:
            return f".{max_count+1}"
        return ""

    def modify(self, data: DataCollection, **kwargs):
        if self.min_size < 0:
            raise RuntimeError(
                f"Minimum ring size ({self.min_size}) must be non-negative."
            )
        if self.min_size > self.max_size:
            raise RuntimeError(
                f"Minimum ring size ({self.min_size}) must be smaller than maximum ring size ({self.max_size})."
            )
        if not data.particles:
            raise RuntimeError("Input data doesn't contain any particles.")
        if not data.particles.bonds:
            raise RuntimeError(
                "Input data doesn't contain any bonds. Rings cannot be found without any bonds defined. Please add a Create Bonds modifier to your pipeline before the RingFinder modifier or import a model containing chemical bonds."
            )

        rings = []
        targets_bfs = targets = range(data.particles.count)

        labels = {}
        yield "Ring search (BFS step)"
        for i, start in enumerate(targets_bfs):
            labels[start] = self.bfs(data, start)
            yield i / len(targets_bfs)

        yield "Ring search (find step)"
        for i, start in enumerate(targets):
            rings += self.find_rings(data, labels, start)
            yield i / len(targets)

        if self.create_mesh:
            yield "Ring search (meshing step)"
            yield from self.prepare_mesh(data, rings)

        self.create_tables_attributes(data, rings)

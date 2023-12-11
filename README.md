# Ring finder
Finds shortest rings formed by bonds in the system

## Description
The modifier outputs:
  - Global Attributes:
    - "RingCount": Total number of rings found
    - "*N*-RingCount": Number of *N*-sized rings found.
  - Data Tables:
    - "*N*-Rings": List of the particle indices making up the *N*-sized rings.
    - "Ring Sizes": Histogram of the different ring sizes.
  - Surfaces: 
    - "Ring Mesh": If selected contains the surface meshes visualizing the rings.

## Parameters 
- `min_size` / "Minimum ring size": Minimum size of the rings found by the modifier.
- `max_size` / "Maximum ring size": Maximum size of the rings found by the modifier.
- `create_mesh` / "Create mesh": Output meshes for each ring.
- `triangulate_facets` / "Triangulate facets": Triangulate facets using a different algorithm. Slower than the default algorithm used in OVITO, but can lead to better results for concave rings / polygons.
- `mesh_vis` / "SurfaceMeshVis": Visual element used for the output meshes.  

## Example

![Example 01](examples/example_01.png)

Using the default mesh generation for a concave polygon (ring):
![Example 01](examples/example_02.png)

Using the custom mesh generation for a concave polygon (ring):
![Example 01](examples/example_03.png)

## Installation
- OVITO Pro [integrated Python interpreter](https://docs.ovito.org/python/introduction/installation.html#ovito-pro-integrated-interpreter):
  ```
  ovitos -m pip install --user git+https://github.com/ovito-org/RingFinder.git
  ``` 
  The `--user` option is recommended and [installs the package in the user's site directory](https://pip.pypa.io/en/stable/user_guide/#user-installs).

- Other Python interpreters or Conda environments:
  ```
  pip install git+https://github.com/ovito-org/RingFinder.git
  ```

## Technical information / dependencies
- Tested on OVITO version 3.9.3

## Contact
Daniel Utt (utt@ovito.org)

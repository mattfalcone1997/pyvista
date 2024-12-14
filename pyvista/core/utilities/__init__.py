"""Utilities routines."""

from __future__ import annotations

import contextlib

from .arrays import FieldAssociation
from .arrays import array_from_vtkmatrix
from .arrays import cell_array
from .arrays import convert_array
from .arrays import convert_string_array
from .arrays import field_array
from .arrays import get_array
from .arrays import get_array_association
from .arrays import get_vtk_type
from .arrays import parse_field_choice
from .arrays import point_array
from .arrays import raise_has_duplicates
from .arrays import raise_not_matching
from .arrays import row_array
from .arrays import set_default_active_scalars
from .arrays import set_default_active_vectors
from .arrays import vtk_bit_array_to_char
from .arrays import vtk_id_list_to_array
from .arrays import vtkmatrix_from_array
from .cells import create_mixed_cells
from .cells import get_mixed_cells
from .cells import ncells_from_cells
from .cells import numpy_to_idarr
from .features import cartesian_to_spherical
from .features import create_grid
from .features import grid_from_sph_coords
from .features import merge
from .features import perlin_noise
from .features import sample_function
from .features import spherical_to_cartesian
from .features import transform_vectors_sph_to_cart
from .features import voxelize
from .features import voxelize_volume
from .fileio import from_meshio
from .fileio import get_ext
from .fileio import is_meshio_mesh
from .fileio import read
from .fileio import read_exodus
from .fileio import read_grdecl
from .fileio import read_meshio
from .fileio import read_pickle
from .fileio import read_texture
from .fileio import save_meshio
from .fileio import save_pickle
from .fileio import set_pickle_format
from .fileio import set_vtkwriter_mode
from .geometric_objects import NORMALS
from .geometric_objects import Arrow
from .geometric_objects import Box
from .geometric_objects import Capsule
from .geometric_objects import Circle
from .geometric_objects import CircularArc
from .geometric_objects import CircularArcFromNormal
from .geometric_objects import Cone
from .geometric_objects import Cube
from .geometric_objects import Cylinder
from .geometric_objects import CylinderStructured
from .geometric_objects import Disc
from .geometric_objects import Dodecahedron
from .geometric_objects import Ellipse
from .geometric_objects import Icosahedron
from .geometric_objects import Icosphere
from .geometric_objects import Line
from .geometric_objects import MultipleLines
from .geometric_objects import Octahedron
from .geometric_objects import Plane
from .geometric_objects import PlatonicSolid
from .geometric_objects import Polygon
from .geometric_objects import Pyramid
from .geometric_objects import Quadrilateral
from .geometric_objects import Rectangle
from .geometric_objects import SolidSphere
from .geometric_objects import SolidSphereGeneric
from .geometric_objects import Sphere
from .geometric_objects import Superquadric
from .geometric_objects import Tetrahedron
from .geometric_objects import Text3D
from .geometric_objects import Triangle
from .geometric_objects import Tube
from .geometric_objects import Wavelet
from .geometric_objects import translate
from .geometric_sources import ArrowSource
from .geometric_sources import AxesGeometrySource
from .geometric_sources import BoxSource
from .geometric_sources import ConeSource
from .geometric_sources import CubeFacesSource
from .geometric_sources import CubeSource
from .geometric_sources import CylinderSource
from .geometric_sources import DiscSource
from .geometric_sources import LineSource
from .geometric_sources import MultipleLinesSource
from .geometric_sources import OrthogonalPlanesSource
from .geometric_sources import PlaneSource
from .geometric_sources import PlatonicSolidSource
from .geometric_sources import PolygonSource
from .geometric_sources import SphereSource
from .geometric_sources import SuperquadricSource
from .geometric_sources import Text3DSource
from .image_sources import ImageEllipsoidSource
from .image_sources import ImageGaussianSource
from .image_sources import ImageGridSource
from .image_sources import ImageMandelbrotSource
from .image_sources import ImageNoiseSource
from .image_sources import ImageSinusoidSource

with contextlib.suppress(ImportError):
    from .geometric_sources import CapsuleSource

from .helpers import axis_rotation
from .helpers import generate_plane
from .helpers import is_inside_bounds
from .helpers import is_pyvista_dataset
from .helpers import wrap
from .misc import AnnotatedIntEnum
from .misc import abstract_class
from .misc import assert_empty_kwargs
from .misc import check_valid_vector
from .misc import conditional_decorator
from .misc import has_module
from .misc import threaded
from .misc import try_callback
from .observers import Observer
from .observers import ProgressMonitor
from .observers import VtkErrorCatcher
from .observers import send_errors_to_logging
from .observers import set_error_output_file
from .parametric_objects import KochanekSpline
from .parametric_objects import ParametricBohemianDome
from .parametric_objects import ParametricBour
from .parametric_objects import ParametricBoy
from .parametric_objects import ParametricCatalanMinimal
from .parametric_objects import ParametricConicSpiral
from .parametric_objects import ParametricCrossCap
from .parametric_objects import ParametricDini
from .parametric_objects import ParametricEllipsoid
from .parametric_objects import ParametricEnneper
from .parametric_objects import ParametricFigure8Klein
from .parametric_objects import ParametricHenneberg
from .parametric_objects import ParametricKlein
from .parametric_objects import ParametricKuen
from .parametric_objects import ParametricMobius
from .parametric_objects import ParametricPluckerConoid
from .parametric_objects import ParametricPseudosphere
from .parametric_objects import ParametricRandomHills
from .parametric_objects import ParametricRoman
from .parametric_objects import ParametricSuperEllipsoid
from .parametric_objects import ParametricSuperToroid
from .parametric_objects import ParametricTorus
from .parametric_objects import Spline
from .parametric_objects import parametric_keywords
from .parametric_objects import surface_from_para
from .points import fit_line_to_points
from .points import fit_plane_to_points
from .points import line_segments_from_points
from .points import lines_from_points
from .points import make_tri_mesh
from .points import principal_axes
from .points import vector_poly_data
from .points import vtk_points
from .reader import AVSucdReader
from .reader import BaseReader
from .reader import BinaryMarchingCubesReader
from .reader import BMPReader
from .reader import BYUReader
from .reader import CGNSReader
from .reader import DEMReader
from .reader import DICOMReader
from .reader import EnSightReader
from .reader import ExodusIIReader
from .reader import FacetReader
from .reader import FLUENTCFFReader
from .reader import FluentReader
from .reader import GambitReader
from .reader import GaussianCubeReader
from .reader import GESignaReader
from .reader import GIFReader
from .reader import GLTFReader
from .reader import HDFReader
from .reader import HDRReader
from .reader import JPEGReader
from .reader import MetaImageReader
from .reader import MFIXReader
from .reader import MINCImageReader
from .reader import MultiBlockPlot3DReader
from .reader import NIFTIReader
from .reader import NRRDReader
from .reader import OBJReader
from .reader import OpenFOAMReader
from .reader import ParticleReader
from .reader import PDBReader
from .reader import Plot3DFunctionEnum
from .reader import Plot3DMetaReader
from .reader import PLYReader
from .reader import PNGReader
from .reader import PNMReader
from .reader import PointCellDataSelection
from .reader import POpenFOAMReader
from .reader import ProStarReader
from .reader import PTSReader
from .reader import PVDDataSet
from .reader import PVDReader
from .reader import SegYReader
from .reader import SLCReader
from .reader import STLReader
from .reader import TecplotReader
from .reader import TIFFReader
from .reader import TimeReader
from .reader import VTKDataSetReader
from .reader import VTKPDataSetReader
from .reader import XdmfReader
from .reader import XMLImageDataReader
from .reader import XMLMultiBlockDataReader
from .reader import XMLPartitionedDataSetReader
from .reader import XMLPImageDataReader
from .reader import XMLPolyDataReader
from .reader import XMLPRectilinearGridReader
from .reader import XMLPUnstructuredGridReader
from .reader import XMLRectilinearGridReader
from .reader import XMLStructuredGridReader
from .reader import XMLUnstructuredGridReader
from .reader import get_reader
from .transform import Transform

# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_ncmesh')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_ncmesh')
    _ncmesh = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ncmesh', [dirname(__file__)])
        except ImportError:
            import _ncmesh
            return _ncmesh
        try:
            _mod = imp.load_module('_ncmesh', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _ncmesh = swig_import_helper()
    del swig_import_helper
else:
    import _ncmesh
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

try:
    import weakref
    weakref_proxy = weakref.proxy
except __builtin__.Exception:
    weakref_proxy = lambda x: x


class intp(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, intp, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, intp, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _ncmesh.new_intp()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ncmesh.delete_intp
    __del__ = lambda self: None

    def assign(self, value):
        return _ncmesh.intp_assign(self, value)

    def value(self):
        return _ncmesh.intp_value(self)

    def cast(self):
        return _ncmesh.intp_cast(self)
    if _newclass:
        frompointer = staticmethod(_ncmesh.intp_frompointer)
    else:
        frompointer = _ncmesh.intp_frompointer
intp_swigregister = _ncmesh.intp_swigregister
intp_swigregister(intp)

def intp_frompointer(t):
    return _ncmesh.intp_frompointer(t)
intp_frompointer = _ncmesh.intp_frompointer

class doublep(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, doublep, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, doublep, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _ncmesh.new_doublep()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ncmesh.delete_doublep
    __del__ = lambda self: None

    def assign(self, value):
        return _ncmesh.doublep_assign(self, value)

    def value(self):
        return _ncmesh.doublep_value(self)

    def cast(self):
        return _ncmesh.doublep_cast(self)
    if _newclass:
        frompointer = staticmethod(_ncmesh.doublep_frompointer)
    else:
        frompointer = _ncmesh.doublep_frompointer
doublep_swigregister = _ncmesh.doublep_swigregister
doublep_swigregister(doublep)

def doublep_frompointer(t):
    return _ncmesh.doublep_frompointer(t)
doublep_frompointer = _ncmesh.doublep_frompointer

import mfem._ser.mesh
import mfem._ser.matrix
import mfem._ser.vector
import mfem._ser.array
import mfem._ser.ostream_typemap
import mfem._ser.mem_manager
import mfem._ser.operators
import mfem._ser.gridfunc
import mfem._ser.coefficient
import mfem._ser.intrules
import mfem._ser.sparsemat
import mfem._ser.densemat
import mfem._ser.eltrans
import mfem._ser.fe
import mfem._ser.geom
import mfem._ser.fespace
import mfem._ser.fe_coll
import mfem._ser.lininteg
import mfem._ser.handle
import mfem._ser.bilininteg
import mfem._ser.linearform
import mfem._ser.element
import mfem._ser.table
import mfem._ser.hash
import mfem._ser.vertex
class Refinement(_object):
    """Proxy of C++ mfem::Refinement class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Refinement, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Refinement, name)
    __repr__ = _swig_repr
    __swig_setmethods__["index"] = _ncmesh.Refinement_index_set
    __swig_getmethods__["index"] = _ncmesh.Refinement_index_get
    if _newclass:
        index = _swig_property(_ncmesh.Refinement_index_get, _ncmesh.Refinement_index_set)
    __swig_setmethods__["ref_type"] = _ncmesh.Refinement_ref_type_set
    __swig_getmethods__["ref_type"] = _ncmesh.Refinement_ref_type_get
    if _newclass:
        ref_type = _swig_property(_ncmesh.Refinement_ref_type_get, _ncmesh.Refinement_ref_type_set)

    def __init__(self, *args):
        """
        __init__(mfem::Refinement self) -> Refinement
        __init__(mfem::Refinement self, int index, int type=7) -> Refinement
        __init__(mfem::Refinement self, int index) -> Refinement
        """
        this = _ncmesh.new_Refinement(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ncmesh.delete_Refinement
    __del__ = lambda self: None
Refinement_swigregister = _ncmesh.Refinement_swigregister
Refinement_swigregister(Refinement)

class Embedding(_object):
    """Proxy of C++ mfem::Embedding class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Embedding, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Embedding, name)
    __repr__ = _swig_repr
    __swig_setmethods__["parent"] = _ncmesh.Embedding_parent_set
    __swig_getmethods__["parent"] = _ncmesh.Embedding_parent_get
    if _newclass:
        parent = _swig_property(_ncmesh.Embedding_parent_get, _ncmesh.Embedding_parent_set)
    __swig_setmethods__["matrix"] = _ncmesh.Embedding_matrix_set
    __swig_getmethods__["matrix"] = _ncmesh.Embedding_matrix_get
    if _newclass:
        matrix = _swig_property(_ncmesh.Embedding_matrix_get, _ncmesh.Embedding_matrix_set)

    def __init__(self, *args):
        """
        __init__(mfem::Embedding self) -> Embedding
        __init__(mfem::Embedding self, int elem, int matrix=0) -> Embedding
        __init__(mfem::Embedding self, int elem) -> Embedding
        """
        this = _ncmesh.new_Embedding(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ncmesh.delete_Embedding
    __del__ = lambda self: None
Embedding_swigregister = _ncmesh.Embedding_swigregister
Embedding_swigregister(Embedding)

class CoarseFineTransformations(_object):
    """Proxy of C++ mfem::CoarseFineTransformations class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CoarseFineTransformations, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CoarseFineTransformations, name)
    __repr__ = _swig_repr
    __swig_setmethods__["point_matrices"] = _ncmesh.CoarseFineTransformations_point_matrices_set
    __swig_getmethods__["point_matrices"] = _ncmesh.CoarseFineTransformations_point_matrices_get
    if _newclass:
        point_matrices = _swig_property(_ncmesh.CoarseFineTransformations_point_matrices_get, _ncmesh.CoarseFineTransformations_point_matrices_set)
    __swig_getmethods__["embeddings"] = _ncmesh.CoarseFineTransformations_embeddings_get
    if _newclass:
        embeddings = _swig_property(_ncmesh.CoarseFineTransformations_embeddings_get)

    def GetPointMatrices(self, geom):
        """GetPointMatrices(CoarseFineTransformations self, mfem::Geometry::Type geom) -> DenseTensor"""
        return _ncmesh.CoarseFineTransformations_GetPointMatrices(self, geom)


    def GetCoarseToFineMap(self, fine_mesh, coarse_to_fine, coarse_to_ref_type, ref_type_to_matrix, ref_type_to_geom):
        """GetCoarseToFineMap(CoarseFineTransformations self, Mesh fine_mesh, Table coarse_to_fine, intArray coarse_to_ref_type, Table ref_type_to_matrix, mfem::Array< mfem::Geometry::Type > & ref_type_to_geom)"""
        return _ncmesh.CoarseFineTransformations_GetCoarseToFineMap(self, fine_mesh, coarse_to_fine, coarse_to_ref_type, ref_type_to_matrix, ref_type_to_geom)


    def Clear(self):
        """Clear(CoarseFineTransformations self)"""
        return _ncmesh.CoarseFineTransformations_Clear(self)


    def MemoryUsage(self):
        """MemoryUsage(CoarseFineTransformations self) -> long"""
        return _ncmesh.CoarseFineTransformations_MemoryUsage(self)


    def __init__(self):
        """__init__(mfem::CoarseFineTransformations self) -> CoarseFineTransformations"""
        this = _ncmesh.new_CoarseFineTransformations()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ncmesh.delete_CoarseFineTransformations
    __del__ = lambda self: None
CoarseFineTransformations_swigregister = _ncmesh.CoarseFineTransformations_swigregister
CoarseFineTransformations_swigregister(CoarseFineTransformations)

class NCMesh(_object):
    """Proxy of C++ mfem::NCMesh class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, NCMesh, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, NCMesh, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(mfem::NCMesh self, Mesh mesh, std::istream * vertex_parents=None) -> NCMesh
        __init__(mfem::NCMesh self, Mesh mesh) -> NCMesh
        __init__(mfem::NCMesh self, NCMesh other) -> NCMesh
        """
        this = _ncmesh.new_NCMesh(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ncmesh.delete_NCMesh
    __del__ = lambda self: None

    def Dimension(self):
        """Dimension(NCMesh self) -> int"""
        return _ncmesh.NCMesh_Dimension(self)


    def SpaceDimension(self):
        """SpaceDimension(NCMesh self) -> int"""
        return _ncmesh.NCMesh_SpaceDimension(self)


    def GetNVertices(self):
        """GetNVertices(NCMesh self) -> int"""
        return _ncmesh.NCMesh_GetNVertices(self)


    def GetNEdges(self):
        """GetNEdges(NCMesh self) -> int"""
        return _ncmesh.NCMesh_GetNEdges(self)


    def GetNFaces(self):
        """GetNFaces(NCMesh self) -> int"""
        return _ncmesh.NCMesh_GetNFaces(self)


    def Refine(self, refinements):
        """Refine(NCMesh self, mfem::Array< mfem::Refinement > const & refinements)"""
        return _ncmesh.NCMesh_Refine(self, refinements)


    def LimitNCLevel(self, max_nc_level):
        """LimitNCLevel(NCMesh self, int max_nc_level)"""
        return _ncmesh.NCMesh_LimitNCLevel(self, max_nc_level)


    def GetDerefinementTable(self):
        """GetDerefinementTable(NCMesh self) -> Table"""
        return _ncmesh.NCMesh_GetDerefinementTable(self)


    def CheckDerefinementNCLevel(self, deref_table, level_ok, max_nc_level):
        """CheckDerefinementNCLevel(NCMesh self, Table deref_table, intArray level_ok, int max_nc_level)"""
        return _ncmesh.NCMesh_CheckDerefinementNCLevel(self, deref_table, level_ok, max_nc_level)


    def Derefine(self, derefs):
        """Derefine(NCMesh self, intArray derefs)"""
        return _ncmesh.NCMesh_Derefine(self, derefs)


    def GetFaceList(self):
        """GetFaceList(NCMesh self) -> mfem::NCMesh::NCList const &"""
        return _ncmesh.NCMesh_GetFaceList(self)


    def GetEdgeList(self):
        """GetEdgeList(NCMesh self) -> mfem::NCMesh::NCList const &"""
        return _ncmesh.NCMesh_GetEdgeList(self)


    def GetVertexList(self):
        """GetVertexList(NCMesh self) -> mfem::NCMesh::NCList const &"""
        return _ncmesh.NCMesh_GetVertexList(self)


    def GetNCList(self, entity):
        """GetNCList(NCMesh self, int entity) -> mfem::NCMesh::NCList const &"""
        return _ncmesh.NCMesh_GetNCList(self, entity)


    def MarkCoarseLevel(self):
        """MarkCoarseLevel(NCMesh self)"""
        return _ncmesh.NCMesh_MarkCoarseLevel(self)


    def GetRefinementTransforms(self):
        """GetRefinementTransforms(NCMesh self) -> CoarseFineTransformations"""
        return _ncmesh.NCMesh_GetRefinementTransforms(self)


    def GetDerefinementTransforms(self):
        """GetDerefinementTransforms(NCMesh self) -> CoarseFineTransformations"""
        return _ncmesh.NCMesh_GetDerefinementTransforms(self)


    def ClearTransforms(self):
        """ClearTransforms(NCMesh self)"""
        return _ncmesh.NCMesh_ClearTransforms(self)


    def GridSfcOrdering2D(width, height, coords):
        """GridSfcOrdering2D(int width, int height, intArray coords)"""
        return _ncmesh.NCMesh_GridSfcOrdering2D(width, height, coords)

    GridSfcOrdering2D = staticmethod(GridSfcOrdering2D)

    def GridSfcOrdering3D(width, height, depth, coords):
        """GridSfcOrdering3D(int width, int height, int depth, intArray coords)"""
        return _ncmesh.NCMesh_GridSfcOrdering3D(width, height, depth, coords)

    GridSfcOrdering3D = staticmethod(GridSfcOrdering3D)

    def GetEdgeVertices(self, edge_id, vert_index, oriented=True):
        """
        GetEdgeVertices(NCMesh self, mfem::NCMesh::MeshId const & edge_id, int [2] vert_index, bool oriented=True)
        GetEdgeVertices(NCMesh self, mfem::NCMesh::MeshId const & edge_id, int [2] vert_index)
        """
        return _ncmesh.NCMesh_GetEdgeVertices(self, edge_id, vert_index, oriented)


    def GetEdgeNCOrientation(self, edge_id):
        """GetEdgeNCOrientation(NCMesh self, mfem::NCMesh::MeshId const & edge_id) -> int"""
        return _ncmesh.NCMesh_GetEdgeNCOrientation(self, edge_id)


    def GetFaceVerticesEdges(self, face_id, vert_index, edge_index, edge_orientation):
        """GetFaceVerticesEdges(NCMesh self, mfem::NCMesh::MeshId const & face_id, int [4] vert_index, int [4] edge_index, int [4] edge_orientation)"""
        return _ncmesh.NCMesh_GetFaceVerticesEdges(self, face_id, vert_index, edge_index, edge_orientation)


    def GetEdgeMaster(self, v1, v2):
        """GetEdgeMaster(NCMesh self, int v1, int v2) -> int"""
        return _ncmesh.NCMesh_GetEdgeMaster(self, v1, v2)


    def GetBoundaryClosure(self, bdr_attr_is_ess, bdr_vertices, bdr_edges):
        """GetBoundaryClosure(NCMesh self, intArray bdr_attr_is_ess, intArray bdr_vertices, intArray bdr_edges)"""
        return _ncmesh.NCMesh_GetBoundaryClosure(self, bdr_attr_is_ess, bdr_vertices, bdr_edges)


    def GetElementGeometry(self):
        """GetElementGeometry(NCMesh self) -> mfem::Geometry::Type"""
        return _ncmesh.NCMesh_GetElementGeometry(self)


    def GetFaceGeometry(self):
        """GetFaceGeometry(NCMesh self) -> mfem::Geometry::Type"""
        return _ncmesh.NCMesh_GetFaceGeometry(self)


    def GetElementDepth(self, i):
        """GetElementDepth(NCMesh self, int i) -> int"""
        return _ncmesh.NCMesh_GetElementDepth(self, i)


    def PrintVertexParents(self, out):
        """PrintVertexParents(NCMesh self, std::ostream & out)"""
        return _ncmesh.NCMesh_PrintVertexParents(self, out)


    def PrintCoarseElements(self, out):
        """PrintCoarseElements(NCMesh self, std::ostream & out)"""
        return _ncmesh.NCMesh_PrintCoarseElements(self, out)


    def LoadVertexParents(self, input):
        """LoadVertexParents(NCMesh self, std::istream & input)"""
        return _ncmesh.NCMesh_LoadVertexParents(self, input)


    def LoadCoarseElements(self, input):
        """LoadCoarseElements(NCMesh self, std::istream & input)"""
        return _ncmesh.NCMesh_LoadCoarseElements(self, input)


    def SetVertexPositions(self, vertices):
        """SetVertexPositions(NCMesh self, mfem::Array< mfem::Vertex > const & vertices)"""
        return _ncmesh.NCMesh_SetVertexPositions(self, vertices)


    def Trim(self):
        """Trim(NCMesh self)"""
        return _ncmesh.NCMesh_Trim(self)


    def MemoryUsage(self):
        """MemoryUsage(NCMesh self) -> long"""
        return _ncmesh.NCMesh_MemoryUsage(self)


    def PrintMemoryDetail(self):
        """PrintMemoryDetail(NCMesh self) -> int"""
        return _ncmesh.NCMesh_PrintMemoryDetail(self)


    def PrintStats(self, *args):
        """
        PrintStats(NCMesh self, std::ostream & out)
        PrintStats(NCMesh self)
        """
        return _ncmesh.NCMesh_PrintStats(self, *args)

NCMesh_swigregister = _ncmesh.NCMesh_swigregister
NCMesh_swigregister(NCMesh)

def NCMesh_GridSfcOrdering2D(width, height, coords):
    """NCMesh_GridSfcOrdering2D(int width, int height, intArray coords)"""
    return _ncmesh.NCMesh_GridSfcOrdering2D(width, height, coords)

def NCMesh_GridSfcOrdering3D(width, height, depth, coords):
    """NCMesh_GridSfcOrdering3D(int width, int height, int depth, intArray coords)"""
    return _ncmesh.NCMesh_GridSfcOrdering3D(width, height, depth, coords)

# This file is compatible with both classic and new-style classes.



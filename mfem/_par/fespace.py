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
        mname = '.'.join((pkg, '_fespace')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_fespace')
    _fespace = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_fespace', [dirname(__file__)])
        except ImportError:
            import _fespace
            return _fespace
        try:
            _mod = imp.load_module('_fespace', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _fespace = swig_import_helper()
    del swig_import_helper
else:
    import _fespace
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


import mfem._par.array
import mfem._ser.ostream_typemap
import mfem._par.mem_manager
import mfem._par.vector
import mfem._par.coefficient
import mfem._par.matrix
import mfem._par.operators
import mfem._par.intrules
import mfem._par.sparsemat
import mfem._par.densemat
import mfem._par.eltrans
import mfem._par.fe
import mfem._par.geom
import mfem._par.mesh
import mfem._par.ncmesh
import mfem._par.element
import mfem._par.table
import mfem._par.hash
import mfem._par.vertex
import mfem._par.gridfunc
import mfem._par.bilininteg
import mfem._par.fe_coll
import mfem._par.lininteg
import mfem._par.linearform
import mfem._par.handle
import mfem._par.hypre
class Ordering(_object):
    """Proxy of C++ mfem::Ordering class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Ordering, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Ordering, name)
    __repr__ = _swig_repr
    byNODES = _fespace.Ordering_byNODES
    byVDIM = _fespace.Ordering_byVDIM

    def __init__(self):
        """__init__(mfem::Ordering self) -> Ordering"""
        this = _fespace.new_Ordering()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _fespace.delete_Ordering
    __del__ = lambda self: None
Ordering_swigregister = _fespace.Ordering_swigregister
Ordering_swigregister(Ordering)

ElementDofOrdering_NATIVE = _fespace.ElementDofOrdering_NATIVE
ElementDofOrdering_LEXICOGRAPHIC = _fespace.ElementDofOrdering_LEXICOGRAPHIC
class FiniteElementSpace(_object):
    """Proxy of C++ mfem::FiniteElementSpace class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FiniteElementSpace, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FiniteElementSpace, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(mfem::FiniteElementSpace self) -> FiniteElementSpace
        __init__(mfem::FiniteElementSpace self, FiniteElementSpace orig, Mesh mesh=None, FiniteElementCollection fec=None) -> FiniteElementSpace
        __init__(mfem::FiniteElementSpace self, FiniteElementSpace orig, Mesh mesh=None) -> FiniteElementSpace
        __init__(mfem::FiniteElementSpace self, FiniteElementSpace orig) -> FiniteElementSpace
        __init__(mfem::FiniteElementSpace self, Mesh mesh, FiniteElementCollection fec, int vdim=1, int ordering) -> FiniteElementSpace
        __init__(mfem::FiniteElementSpace self, Mesh mesh, FiniteElementCollection fec, int vdim=1) -> FiniteElementSpace
        __init__(mfem::FiniteElementSpace self, Mesh mesh, FiniteElementCollection fec) -> FiniteElementSpace
        __init__(mfem::FiniteElementSpace self, Mesh mesh, mfem::NURBSExtension * ext, FiniteElementCollection fec, int vdim=1, int ordering) -> FiniteElementSpace
        __init__(mfem::FiniteElementSpace self, Mesh mesh, mfem::NURBSExtension * ext, FiniteElementCollection fec, int vdim=1) -> FiniteElementSpace
        __init__(mfem::FiniteElementSpace self, Mesh mesh, mfem::NURBSExtension * ext, FiniteElementCollection fec) -> FiniteElementSpace
        """
        this = _fespace.new_FiniteElementSpace(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this


        '''
            FiniteElementSpace(Mesh *m, const FiniteElementCollection *f,
                          int vdim = 1, int ordering = Ordering::byNODES);
            keep reference to mesh and fec to prevent it from
            freeed from pytho garbage collector
        '''
        if hasattr(self, 'this'):
            self.mesh = args[0]
            self.fec = args[1]





    def GetMesh(self):
        """GetMesh(FiniteElementSpace self) -> Mesh"""
        return _fespace.FiniteElementSpace_GetMesh(self)


    def GetNURBSext(self, *args):
        """
        GetNURBSext(FiniteElementSpace self) -> mfem::NURBSExtension const
        GetNURBSext(FiniteElementSpace self) -> mfem::NURBSExtension *
        """
        return _fespace.FiniteElementSpace_GetNURBSext(self, *args)


    def StealNURBSext(self):
        """StealNURBSext(FiniteElementSpace self) -> mfem::NURBSExtension *"""
        return _fespace.FiniteElementSpace_StealNURBSext(self)


    def Conforming(self):
        """Conforming(FiniteElementSpace self) -> bool"""
        return _fespace.FiniteElementSpace_Conforming(self)


    def Nonconforming(self):
        """Nonconforming(FiniteElementSpace self) -> bool"""
        return _fespace.FiniteElementSpace_Nonconforming(self)


    def GetConformingProlongation(self):
        """GetConformingProlongation(FiniteElementSpace self) -> SparseMatrix"""
        return _fespace.FiniteElementSpace_GetConformingProlongation(self)


    def GetConformingRestriction(self):
        """GetConformingRestriction(FiniteElementSpace self) -> SparseMatrix"""
        return _fespace.FiniteElementSpace_GetConformingRestriction(self)


    def GetProlongationMatrix(self):
        """GetProlongationMatrix(FiniteElementSpace self) -> Operator"""
        return _fespace.FiniteElementSpace_GetProlongationMatrix(self)


    def GetRestrictionMatrix(self):
        """GetRestrictionMatrix(FiniteElementSpace self) -> SparseMatrix"""
        return _fespace.FiniteElementSpace_GetRestrictionMatrix(self)


    def GetElementRestriction(self, e_ordering):
        """GetElementRestriction(FiniteElementSpace self, mfem::ElementDofOrdering e_ordering) -> Operator"""
        return _fespace.FiniteElementSpace_GetElementRestriction(self, e_ordering)


    def GetQuadratureInterpolator(self, *args):
        """
        GetQuadratureInterpolator(FiniteElementSpace self, IntegrationRule ir) -> QuadratureInterpolator
        GetQuadratureInterpolator(FiniteElementSpace self, QuadratureSpace qs) -> QuadratureInterpolator
        """
        return _fespace.FiniteElementSpace_GetQuadratureInterpolator(self, *args)


    def GetVDim(self):
        """GetVDim(FiniteElementSpace self) -> int"""
        return _fespace.FiniteElementSpace_GetVDim(self)


    def GetOrder(self, i):
        """GetOrder(FiniteElementSpace self, int i) -> int"""
        return _fespace.FiniteElementSpace_GetOrder(self, i)


    def GetFaceOrder(self, i):
        """GetFaceOrder(FiniteElementSpace self, int i) -> int"""
        return _fespace.FiniteElementSpace_GetFaceOrder(self, i)


    def GetNDofs(self):
        """GetNDofs(FiniteElementSpace self) -> int"""
        return _fespace.FiniteElementSpace_GetNDofs(self)


    def GetVSize(self):
        """GetVSize(FiniteElementSpace self) -> int"""
        return _fespace.FiniteElementSpace_GetVSize(self)


    def GetTrueVSize(self):
        """GetTrueVSize(FiniteElementSpace self) -> int"""
        return _fespace.FiniteElementSpace_GetTrueVSize(self)


    def GetNConformingDofs(self):
        """GetNConformingDofs(FiniteElementSpace self) -> int"""
        return _fespace.FiniteElementSpace_GetNConformingDofs(self)


    def GetConformingVSize(self):
        """GetConformingVSize(FiniteElementSpace self) -> int"""
        return _fespace.FiniteElementSpace_GetConformingVSize(self)


    def GetOrdering(self):
        """GetOrdering(FiniteElementSpace self) -> mfem::Ordering::Type"""
        return _fespace.FiniteElementSpace_GetOrdering(self)


    def FEColl(self):
        """FEColl(FiniteElementSpace self) -> FiniteElementCollection"""
        return _fespace.FiniteElementSpace_FEColl(self)


    def GetNVDofs(self):
        """GetNVDofs(FiniteElementSpace self) -> int"""
        return _fespace.FiniteElementSpace_GetNVDofs(self)


    def GetNEDofs(self):
        """GetNEDofs(FiniteElementSpace self) -> int"""
        return _fespace.FiniteElementSpace_GetNEDofs(self)


    def GetNFDofs(self):
        """GetNFDofs(FiniteElementSpace self) -> int"""
        return _fespace.FiniteElementSpace_GetNFDofs(self)


    def GetNV(self):
        """GetNV(FiniteElementSpace self) -> int"""
        return _fespace.FiniteElementSpace_GetNV(self)


    def GetNE(self):
        """GetNE(FiniteElementSpace self) -> int"""
        return _fespace.FiniteElementSpace_GetNE(self)


    def GetNF(self):
        """GetNF(FiniteElementSpace self) -> int"""
        return _fespace.FiniteElementSpace_GetNF(self)


    def GetNBE(self):
        """GetNBE(FiniteElementSpace self) -> int"""
        return _fespace.FiniteElementSpace_GetNBE(self)


    def GetElementType(self, i):
        """GetElementType(FiniteElementSpace self, int i) -> int"""
        return _fespace.FiniteElementSpace_GetElementType(self, i)


    def GetElementVertices(self, i, vertices):
        """GetElementVertices(FiniteElementSpace self, int i, intArray vertices)"""
        return _fespace.FiniteElementSpace_GetElementVertices(self, i, vertices)


    def GetBdrElementType(self, i):
        """GetBdrElementType(FiniteElementSpace self, int i) -> int"""
        return _fespace.FiniteElementSpace_GetBdrElementType(self, i)


    def GetElementTransformation(self, *args):
        """
        GetElementTransformation(FiniteElementSpace self, int i) -> ElementTransformation
        GetElementTransformation(FiniteElementSpace self, int i, IsoparametricTransformation ElTr)
        """
        return _fespace.FiniteElementSpace_GetElementTransformation(self, *args)


    def GetBdrElementTransformation(self, i):
        """GetBdrElementTransformation(FiniteElementSpace self, int i) -> ElementTransformation"""
        return _fespace.FiniteElementSpace_GetBdrElementTransformation(self, i)


    def GetAttribute(self, i):
        """GetAttribute(FiniteElementSpace self, int i) -> int"""
        return _fespace.FiniteElementSpace_GetAttribute(self, i)


    def GetBdrAttribute(self, i):
        """GetBdrAttribute(FiniteElementSpace self, int i) -> int"""
        return _fespace.FiniteElementSpace_GetBdrAttribute(self, i)


    def GetElementDofs(self, i):
        from  .array import intArray
        vdofs = intArray()
        _fespace.FiniteElementSpace_GetElementDofs(self, i, vdofs)
        return vdofs.ToList()



    def GetBdrElementDofs(self, i):
        from  .array import intArray
        vdofs = intArray()
        _fespace.FiniteElementSpace_GetBdrElementDofs(self, i, vdofs)
        return vdofs.ToList()



    def GetFaceDofs(self, i):
        from  .array import intArray
        vdofs = intArray()
        _fespace.FiniteElementSpace_GetFaceDofs(self, i, vdofs)
        return vdofs.ToList()



    def GetEdgeDofs(self, i):
        from  .array import intArray
        vdofs = intArray()
        _fespace.FiniteElementSpace_GetEdgeDofs(self, i, vdofs)
        return vdofs.ToList()



    def GetVertexDofs(self, i):
        from  .array import intArray
        vdofs = intArray()
        _fespace.FiniteElementSpace_GetVertexDofs(self, i, vdofs)
        return vdofs.ToList()



    def GetElementInteriorDofs(self, i):
        from  .array import intArray
        vdofs = intArray()
        _fespace.FiniteElementSpace_GetElementInteriorDofs(self, i, vdofs)
        return vdofs.ToList()



    def GetFaceInteriorDofs(self, i, dofs):
        """GetFaceInteriorDofs(FiniteElementSpace self, int i, intArray dofs)"""
        return _fespace.FiniteElementSpace_GetFaceInteriorDofs(self, i, dofs)


    def GetNumElementInteriorDofs(self, i):
        """GetNumElementInteriorDofs(FiniteElementSpace self, int i) -> int"""
        return _fespace.FiniteElementSpace_GetNumElementInteriorDofs(self, i)


    def GetEdgeInteriorDofs(self, i):
        from  .array import intArray
        vdofs = intArray()
        _fespace.FiniteElementSpace_GetEdgeInteriorDofs(self, i, vdofs)
        return vdofs.ToList()



    def DofsToVDofs(self, *args):
        """
        DofsToVDofs(FiniteElementSpace self, intArray dofs, int ndofs=-1)
        DofsToVDofs(FiniteElementSpace self, intArray dofs)
        DofsToVDofs(FiniteElementSpace self, int vd, intArray dofs, int ndofs=-1)
        DofsToVDofs(FiniteElementSpace self, int vd, intArray dofs)
        """
        return _fespace.FiniteElementSpace_DofsToVDofs(self, *args)


    def DofToVDof(self, dof, vd, ndofs=-1):
        """
        DofToVDof(FiniteElementSpace self, int dof, int vd, int ndofs=-1) -> int
        DofToVDof(FiniteElementSpace self, int dof, int vd) -> int
        """
        return _fespace.FiniteElementSpace_DofToVDof(self, dof, vd, ndofs)


    def VDofToDof(self, vdof):
        """VDofToDof(FiniteElementSpace self, int vdof) -> int"""
        return _fespace.FiniteElementSpace_VDofToDof(self, vdof)


    def AdjustVDofs(vdofs):
        """AdjustVDofs(intArray vdofs)"""
        return _fespace.FiniteElementSpace_AdjustVDofs(vdofs)

    AdjustVDofs = staticmethod(AdjustVDofs)

    def GetElementVDofs(self, i):
        from  .array import intArray
        vdofs = intArray()
        _fespace.FiniteElementSpace_GetElementVDofs(self, i, vdofs)
        return vdofs.ToList()



    def GetBdrElementVDofs(self, i):
        from  .array import intArray
        vdofs = intArray()
        _fespace.FiniteElementSpace_GetBdrElementVDofs(self, i, vdofs)
        return vdofs.ToList()



    def GetFaceVDofs(self, i):
        from  .array import intArray
        vdofs = intArray()
        _fespace.FiniteElementSpace_GetFaceVDofs(self, i, vdofs)
        return vdofs.ToList()



    def GetEdgeVDofs(self, i):
        from  .array import intArray
        vdofs = intArray()
        _fespace.FiniteElementSpace_GetEdgeVDofs(self, i, vdofs)
        return vdofs.ToList()



    def GetVertexVDofs(self, i):
        from  .array import intArray
        vdofs = intArray()
        _fespace.FiniteElementSpace_GetVertexVDofs(self, i, vdofs)
        return vdofs.ToList()



    def GetElementInteriorVDofs(self, i):
        from  .array import intArray
        vdofs = intArray()
        _fespace.FiniteElementSpace_GetElementInteriorVDofs(self, i, vdofs)
        return vdofs.ToList()



    def GetEdgeInteriorVDofs(self, i):
        from  .array import intArray
        vdofs = intArray()
        _fespace.FiniteElementSpace_GetEdgeInteriorVDofs(self, i, vdofs)
        return vdofs.ToList()



    def RebuildElementToDofTable(self):
        """RebuildElementToDofTable(FiniteElementSpace self)"""
        return _fespace.FiniteElementSpace_RebuildElementToDofTable(self)


    def ReorderElementToDofTable(self):
        """ReorderElementToDofTable(FiniteElementSpace self)"""
        return _fespace.FiniteElementSpace_ReorderElementToDofTable(self)


    def BuildDofToArrays(self):
        """BuildDofToArrays(FiniteElementSpace self)"""
        return _fespace.FiniteElementSpace_BuildDofToArrays(self)


    def GetElementToDofTable(self):
        """GetElementToDofTable(FiniteElementSpace self) -> Table"""
        return _fespace.FiniteElementSpace_GetElementToDofTable(self)


    def GetBdrElementToDofTable(self):
        """GetBdrElementToDofTable(FiniteElementSpace self) -> Table"""
        return _fespace.FiniteElementSpace_GetBdrElementToDofTable(self)


    def GetElementForDof(self, i):
        """GetElementForDof(FiniteElementSpace self, int i) -> int"""
        return _fespace.FiniteElementSpace_GetElementForDof(self, i)


    def GetLocalDofForDof(self, i):
        """GetLocalDofForDof(FiniteElementSpace self, int i) -> int"""
        return _fespace.FiniteElementSpace_GetLocalDofForDof(self, i)


    def GetFE(self, i):
        """GetFE(FiniteElementSpace self, int i) -> FiniteElement"""
        return _fespace.FiniteElementSpace_GetFE(self, i)


    def GetBE(self, i):
        """GetBE(FiniteElementSpace self, int i) -> FiniteElement"""
        return _fespace.FiniteElementSpace_GetBE(self, i)


    def GetFaceElement(self, i):
        """GetFaceElement(FiniteElementSpace self, int i) -> FiniteElement"""
        return _fespace.FiniteElementSpace_GetFaceElement(self, i)


    def GetEdgeElement(self, i):
        """GetEdgeElement(FiniteElementSpace self, int i) -> FiniteElement"""
        return _fespace.FiniteElementSpace_GetEdgeElement(self, i)


    def GetTraceElement(self, i, geom_type):
        """GetTraceElement(FiniteElementSpace self, int i, mfem::Geometry::Type geom_type) -> FiniteElement"""
        return _fespace.FiniteElementSpace_GetTraceElement(self, i, geom_type)


    def GetEssentialVDofs(self, bdr_attr_is_ess, ess_vdofs, component=-1):
        """
        GetEssentialVDofs(FiniteElementSpace self, intArray bdr_attr_is_ess, intArray ess_vdofs, int component=-1)
        GetEssentialVDofs(FiniteElementSpace self, intArray bdr_attr_is_ess, intArray ess_vdofs)
        """
        return _fespace.FiniteElementSpace_GetEssentialVDofs(self, bdr_attr_is_ess, ess_vdofs, component)


    def GetEssentialTrueDofs(self, bdr_attr_is_ess, ess_tdof_list, component=-1):
        """
        GetEssentialTrueDofs(FiniteElementSpace self, intArray bdr_attr_is_ess, intArray ess_tdof_list, int component=-1)
        GetEssentialTrueDofs(FiniteElementSpace self, intArray bdr_attr_is_ess, intArray ess_tdof_list)
        """
        return _fespace.FiniteElementSpace_GetEssentialTrueDofs(self, bdr_attr_is_ess, ess_tdof_list, component)


    def MarkerToList(marker, list):
        """MarkerToList(intArray marker, intArray list)"""
        return _fespace.FiniteElementSpace_MarkerToList(marker, list)

    MarkerToList = staticmethod(MarkerToList)

    def ListToMarker(list, marker_size, marker, mark_val=-1):
        """
        ListToMarker(intArray list, int marker_size, intArray marker, int mark_val=-1)
        ListToMarker(intArray list, int marker_size, intArray marker)
        """
        return _fespace.FiniteElementSpace_ListToMarker(list, marker_size, marker, mark_val)

    ListToMarker = staticmethod(ListToMarker)

    def ConvertToConformingVDofs(self, dofs, cdofs):
        """ConvertToConformingVDofs(FiniteElementSpace self, intArray dofs, intArray cdofs)"""
        return _fespace.FiniteElementSpace_ConvertToConformingVDofs(self, dofs, cdofs)


    def ConvertFromConformingVDofs(self, cdofs, dofs):
        """ConvertFromConformingVDofs(FiniteElementSpace self, intArray cdofs, intArray dofs)"""
        return _fespace.FiniteElementSpace_ConvertFromConformingVDofs(self, cdofs, dofs)


    def D2C_GlobalRestrictionMatrix(self, cfes):
        """D2C_GlobalRestrictionMatrix(FiniteElementSpace self, FiniteElementSpace cfes) -> SparseMatrix"""
        return _fespace.FiniteElementSpace_D2C_GlobalRestrictionMatrix(self, cfes)


    def D2Const_GlobalRestrictionMatrix(self, cfes):
        """D2Const_GlobalRestrictionMatrix(FiniteElementSpace self, FiniteElementSpace cfes) -> SparseMatrix"""
        return _fespace.FiniteElementSpace_D2Const_GlobalRestrictionMatrix(self, cfes)


    def H2L_GlobalRestrictionMatrix(self, lfes):
        """H2L_GlobalRestrictionMatrix(FiniteElementSpace self, FiniteElementSpace lfes) -> SparseMatrix"""
        return _fespace.FiniteElementSpace_H2L_GlobalRestrictionMatrix(self, lfes)


    def GetTransferOperator(self, coarse_fes, T):
        """GetTransferOperator(FiniteElementSpace self, FiniteElementSpace coarse_fes, OperatorHandle T)"""
        return _fespace.FiniteElementSpace_GetTransferOperator(self, coarse_fes, T)


    def GetTrueTransferOperator(self, coarse_fes, T):
        """GetTrueTransferOperator(FiniteElementSpace self, FiniteElementSpace coarse_fes, OperatorHandle T)"""
        return _fespace.FiniteElementSpace_GetTrueTransferOperator(self, coarse_fes, T)


    def Update(self, want_transform=True):
        """
        Update(FiniteElementSpace self, bool want_transform=True)
        Update(FiniteElementSpace self)
        """
        return _fespace.FiniteElementSpace_Update(self, want_transform)


    def GetUpdateOperator(self, *args):
        """
        GetUpdateOperator(FiniteElementSpace self) -> Operator
        GetUpdateOperator(FiniteElementSpace self, OperatorHandle T)
        """
        return _fespace.FiniteElementSpace_GetUpdateOperator(self, *args)


    def SetUpdateOperatorOwner(self, own):
        """SetUpdateOperatorOwner(FiniteElementSpace self, bool own)"""
        return _fespace.FiniteElementSpace_SetUpdateOperatorOwner(self, own)


    def SetUpdateOperatorType(self, tid):
        """SetUpdateOperatorType(FiniteElementSpace self, mfem::Operator::Type tid)"""
        return _fespace.FiniteElementSpace_SetUpdateOperatorType(self, tid)


    def UpdatesFinished(self):
        """UpdatesFinished(FiniteElementSpace self)"""
        return _fespace.FiniteElementSpace_UpdatesFinished(self)


    def GetSequence(self):
        """GetSequence(FiniteElementSpace self) -> long"""
        return _fespace.FiniteElementSpace_GetSequence(self)


    def Save(self, out):
        """Save(FiniteElementSpace self, std::ostream & out)"""
        return _fespace.FiniteElementSpace_Save(self, out)


    def Load(self, m, input):
        """Load(FiniteElementSpace self, Mesh m, std::istream & input) -> FiniteElementCollection"""
        return _fespace.FiniteElementSpace_Load(self, m, input)

    __swig_destroy__ = _fespace.delete_FiniteElementSpace
    __del__ = lambda self: None
FiniteElementSpace_swigregister = _fespace.FiniteElementSpace_swigregister
FiniteElementSpace_swigregister(FiniteElementSpace)

def FiniteElementSpace_AdjustVDofs(vdofs):
    """FiniteElementSpace_AdjustVDofs(intArray vdofs)"""
    return _fespace.FiniteElementSpace_AdjustVDofs(vdofs)

def FiniteElementSpace_MarkerToList(marker, list):
    """FiniteElementSpace_MarkerToList(intArray marker, intArray list)"""
    return _fespace.FiniteElementSpace_MarkerToList(marker, list)

def FiniteElementSpace_ListToMarker(list, marker_size, marker, mark_val=-1):
    """
    ListToMarker(intArray list, int marker_size, intArray marker, int mark_val=-1)
    FiniteElementSpace_ListToMarker(intArray list, int marker_size, intArray marker)
    """
    return _fespace.FiniteElementSpace_ListToMarker(list, marker_size, marker, mark_val)

class QuadratureSpace(_object):
    """Proxy of C++ mfem::QuadratureSpace class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, QuadratureSpace, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, QuadratureSpace, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(mfem::QuadratureSpace self, Mesh mesh_, int order_) -> QuadratureSpace
        __init__(mfem::QuadratureSpace self, Mesh mesh_, std::istream & arg3) -> QuadratureSpace
        """
        this = _fespace.new_QuadratureSpace(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _fespace.delete_QuadratureSpace
    __del__ = lambda self: None

    def GetSize(self):
        """GetSize(QuadratureSpace self) -> int"""
        return _fespace.QuadratureSpace_GetSize(self)


    def GetElementIntRule(self, idx):
        """GetElementIntRule(QuadratureSpace self, int idx) -> IntegrationRule"""
        return _fespace.QuadratureSpace_GetElementIntRule(self, idx)


    def Save(self, out):
        """Save(QuadratureSpace self, std::ostream & out)"""
        return _fespace.QuadratureSpace_Save(self, out)

QuadratureSpace_swigregister = _fespace.QuadratureSpace_swigregister
QuadratureSpace_swigregister(QuadratureSpace)

class GridTransfer(_object):
    """Proxy of C++ mfem::GridTransfer class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, GridTransfer, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, GridTransfer, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _fespace.delete_GridTransfer
    __del__ = lambda self: None

    def SetOperatorType(self, type):
        """SetOperatorType(GridTransfer self, mfem::Operator::Type type)"""
        return _fespace.GridTransfer_SetOperatorType(self, type)


    def ForwardOperator(self):
        """ForwardOperator(GridTransfer self) -> Operator"""
        return _fespace.GridTransfer_ForwardOperator(self)


    def BackwardOperator(self):
        """BackwardOperator(GridTransfer self) -> Operator"""
        return _fespace.GridTransfer_BackwardOperator(self)


    def TrueForwardOperator(self):
        """TrueForwardOperator(GridTransfer self) -> Operator"""
        return _fespace.GridTransfer_TrueForwardOperator(self)


    def TrueBackwardOperator(self):
        """TrueBackwardOperator(GridTransfer self) -> Operator"""
        return _fespace.GridTransfer_TrueBackwardOperator(self)

GridTransfer_swigregister = _fespace.GridTransfer_swigregister
GridTransfer_swigregister(GridTransfer)

class InterpolationGridTransfer(GridTransfer):
    """Proxy of C++ mfem::InterpolationGridTransfer class."""

    __swig_setmethods__ = {}
    for _s in [GridTransfer]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, InterpolationGridTransfer, name, value)
    __swig_getmethods__ = {}
    for _s in [GridTransfer]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, InterpolationGridTransfer, name)
    __repr__ = _swig_repr

    def __init__(self, coarse_fes, fine_fes):
        """__init__(mfem::InterpolationGridTransfer self, FiniteElementSpace coarse_fes, FiniteElementSpace fine_fes) -> InterpolationGridTransfer"""
        this = _fespace.new_InterpolationGridTransfer(coarse_fes, fine_fes)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _fespace.delete_InterpolationGridTransfer
    __del__ = lambda self: None

    def SetMassIntegrator(self, mass_integ_, own_mass_integ_=True):
        """
        SetMassIntegrator(InterpolationGridTransfer self, BilinearFormIntegrator mass_integ_, bool own_mass_integ_=True)
        SetMassIntegrator(InterpolationGridTransfer self, BilinearFormIntegrator mass_integ_)
        """
        return _fespace.InterpolationGridTransfer_SetMassIntegrator(self, mass_integ_, own_mass_integ_)


    def ForwardOperator(self):
        """ForwardOperator(InterpolationGridTransfer self) -> Operator"""
        return _fespace.InterpolationGridTransfer_ForwardOperator(self)


    def BackwardOperator(self):
        """BackwardOperator(InterpolationGridTransfer self) -> Operator"""
        return _fespace.InterpolationGridTransfer_BackwardOperator(self)

InterpolationGridTransfer_swigregister = _fespace.InterpolationGridTransfer_swigregister
InterpolationGridTransfer_swigregister(InterpolationGridTransfer)

class L2ProjectionGridTransfer(GridTransfer):
    """Proxy of C++ mfem::L2ProjectionGridTransfer class."""

    __swig_setmethods__ = {}
    for _s in [GridTransfer]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, L2ProjectionGridTransfer, name, value)
    __swig_getmethods__ = {}
    for _s in [GridTransfer]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, L2ProjectionGridTransfer, name)
    __repr__ = _swig_repr

    def __init__(self, coarse_fes, fine_fes):
        """__init__(mfem::L2ProjectionGridTransfer self, FiniteElementSpace coarse_fes, FiniteElementSpace fine_fes) -> L2ProjectionGridTransfer"""
        this = _fespace.new_L2ProjectionGridTransfer(coarse_fes, fine_fes)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def ForwardOperator(self):
        """ForwardOperator(L2ProjectionGridTransfer self) -> Operator"""
        return _fespace.L2ProjectionGridTransfer_ForwardOperator(self)


    def BackwardOperator(self):
        """BackwardOperator(L2ProjectionGridTransfer self) -> Operator"""
        return _fespace.L2ProjectionGridTransfer_BackwardOperator(self)

    __swig_destroy__ = _fespace.delete_L2ProjectionGridTransfer
    __del__ = lambda self: None
L2ProjectionGridTransfer_swigregister = _fespace.L2ProjectionGridTransfer_swigregister
L2ProjectionGridTransfer_swigregister(L2ProjectionGridTransfer)

class ElementRestriction(mfem._par.operators.Operator):
    """Proxy of C++ mfem::ElementRestriction class."""

    __swig_setmethods__ = {}
    for _s in [mfem._par.operators.Operator]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ElementRestriction, name, value)
    __swig_getmethods__ = {}
    for _s in [mfem._par.operators.Operator]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ElementRestriction, name)
    __repr__ = _swig_repr

    def __init__(self, arg2, arg3):
        """__init__(mfem::ElementRestriction self, FiniteElementSpace arg2, mfem::ElementDofOrdering arg3) -> ElementRestriction"""
        this = _fespace.new_ElementRestriction(arg2, arg3)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Mult(self, x, y):
        """Mult(ElementRestriction self, Vector x, Vector y)"""
        return _fespace.ElementRestriction_Mult(self, x, y)


    def MultTranspose(self, x, y):
        """MultTranspose(ElementRestriction self, Vector x, Vector y)"""
        return _fespace.ElementRestriction_MultTranspose(self, x, y)

    __swig_destroy__ = _fespace.delete_ElementRestriction
    __del__ = lambda self: None
ElementRestriction_swigregister = _fespace.ElementRestriction_swigregister
ElementRestriction_swigregister(ElementRestriction)

class QuadratureInterpolator(_object):
    """Proxy of C++ mfem::QuadratureInterpolator class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, QuadratureInterpolator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, QuadratureInterpolator, name)
    __repr__ = _swig_repr
    VALUES = _fespace.QuadratureInterpolator_VALUES
    DERIVATIVES = _fespace.QuadratureInterpolator_DERIVATIVES
    DETERMINANTS = _fespace.QuadratureInterpolator_DETERMINANTS

    def __init__(self, *args):
        """
        __init__(mfem::QuadratureInterpolator self, FiniteElementSpace fes, IntegrationRule ir) -> QuadratureInterpolator
        __init__(mfem::QuadratureInterpolator self, FiniteElementSpace fes, QuadratureSpace qs) -> QuadratureInterpolator
        """
        this = _fespace.new_QuadratureInterpolator(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def DisableTensorProducts(self, disable=True):
        """
        DisableTensorProducts(QuadratureInterpolator self, bool disable=True)
        DisableTensorProducts(QuadratureInterpolator self)
        """
        return _fespace.QuadratureInterpolator_DisableTensorProducts(self, disable)


    def Mult(self, e_vec, eval_flags, q_val, q_der, q_det):
        """Mult(QuadratureInterpolator self, Vector e_vec, unsigned int eval_flags, Vector q_val, Vector q_der, Vector q_det)"""
        return _fespace.QuadratureInterpolator_Mult(self, e_vec, eval_flags, q_val, q_der, q_det)


    def MultTranspose(self, eval_flags, q_val, q_der, e_vec):
        """MultTranspose(QuadratureInterpolator self, unsigned int eval_flags, Vector q_val, Vector q_der, Vector e_vec)"""
        return _fespace.QuadratureInterpolator_MultTranspose(self, eval_flags, q_val, q_der, e_vec)

    __swig_destroy__ = _fespace.delete_QuadratureInterpolator
    __del__ = lambda self: None
QuadratureInterpolator_swigregister = _fespace.QuadratureInterpolator_swigregister
QuadratureInterpolator_swigregister(QuadratureInterpolator)

# This file is compatible with both classic and new-style classes.



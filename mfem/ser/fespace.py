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


import array
import ostream_typemap
import vector
import coefficient
import matrix
import operators
import intrules
import sparsemat
import densemat
import eltrans
import fe
import mesh
import ncmesh
import gridfunc
import bilininteg
import fe_coll
import lininteg
import linearform
import element
import geom
import table
import vertex
import handle
class Ordering(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Ordering, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Ordering, name)
    __repr__ = _swig_repr
    byNODES = _fespace.Ordering_byNODES
    byVDIM = _fespace.Ordering_byVDIM

    def __init__(self):
        this = _fespace.new_Ordering()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _fespace.delete_Ordering
    __del__ = lambda self: None
Ordering_swigregister = _fespace.Ordering_swigregister
Ordering_swigregister(Ordering)

class FiniteElementSpace(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FiniteElementSpace, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FiniteElementSpace, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
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
        return _fespace.FiniteElementSpace_GetMesh(self)

    def GetNURBSext(self, *args):
        return _fespace.FiniteElementSpace_GetNURBSext(self, *args)

    def StealNURBSext(self):
        return _fespace.FiniteElementSpace_StealNURBSext(self)

    def Conforming(self):
        return _fespace.FiniteElementSpace_Conforming(self)

    def Nonconforming(self):
        return _fespace.FiniteElementSpace_Nonconforming(self)

    def GetConformingProlongation(self):
        return _fespace.FiniteElementSpace_GetConformingProlongation(self)

    def GetConformingRestriction(self):
        return _fespace.FiniteElementSpace_GetConformingRestriction(self)

    def GetProlongationMatrix(self):
        return _fespace.FiniteElementSpace_GetProlongationMatrix(self)

    def GetRestrictionMatrix(self):
        return _fespace.FiniteElementSpace_GetRestrictionMatrix(self)

    def GetVDim(self):
        return _fespace.FiniteElementSpace_GetVDim(self)

    def GetOrder(self, i):
        return _fespace.FiniteElementSpace_GetOrder(self, i)

    def GetFaceOrder(self, i):
        return _fespace.FiniteElementSpace_GetFaceOrder(self, i)

    def GetNDofs(self):
        return _fespace.FiniteElementSpace_GetNDofs(self)

    def GetVSize(self):
        return _fespace.FiniteElementSpace_GetVSize(self)

    def GetTrueVSize(self):
        return _fespace.FiniteElementSpace_GetTrueVSize(self)

    def GetNConformingDofs(self):
        return _fespace.FiniteElementSpace_GetNConformingDofs(self)

    def GetConformingVSize(self):
        return _fespace.FiniteElementSpace_GetConformingVSize(self)

    def GetOrdering(self):
        return _fespace.FiniteElementSpace_GetOrdering(self)

    def FEColl(self):
        return _fespace.FiniteElementSpace_FEColl(self)

    def GetNVDofs(self):
        return _fespace.FiniteElementSpace_GetNVDofs(self)

    def GetNEDofs(self):
        return _fespace.FiniteElementSpace_GetNEDofs(self)

    def GetNFDofs(self):
        return _fespace.FiniteElementSpace_GetNFDofs(self)

    def GetNV(self):
        return _fespace.FiniteElementSpace_GetNV(self)

    def GetNE(self):
        return _fespace.FiniteElementSpace_GetNE(self)

    def GetNF(self):
        return _fespace.FiniteElementSpace_GetNF(self)

    def GetNBE(self):
        return _fespace.FiniteElementSpace_GetNBE(self)

    def GetElementType(self, i):
        return _fespace.FiniteElementSpace_GetElementType(self, i)

    def GetElementVertices(self, i, vertices):
        return _fespace.FiniteElementSpace_GetElementVertices(self, i, vertices)

    def GetBdrElementType(self, i):
        return _fespace.FiniteElementSpace_GetBdrElementType(self, i)

    def GetElementTransformation(self, *args):
        return _fespace.FiniteElementSpace_GetElementTransformation(self, *args)

    def GetBdrElementTransformation(self, i):
        return _fespace.FiniteElementSpace_GetBdrElementTransformation(self, i)

    def GetAttribute(self, i):
        return _fespace.FiniteElementSpace_GetAttribute(self, i)

    def GetBdrAttribute(self, i):
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
        return _fespace.FiniteElementSpace_GetFaceInteriorDofs(self, i, dofs)

    def GetNumElementInteriorDofs(self, i):
        return _fespace.FiniteElementSpace_GetNumElementInteriorDofs(self, i)

    def GetEdgeInteriorDofs(self, i):
        from  .array import intArray
        vdofs = intArray()
        _fespace.FiniteElementSpace_GetEdgeInteriorDofs(self, i, vdofs)
        return vdofs.ToList()



    def DofsToVDofs(self, *args):
        return _fespace.FiniteElementSpace_DofsToVDofs(self, *args)

    def DofToVDof(self, dof, vd, ndofs=-1):
        return _fespace.FiniteElementSpace_DofToVDof(self, dof, vd, ndofs)

    def VDofToDof(self, vdof):
        return _fespace.FiniteElementSpace_VDofToDof(self, vdof)
    if _newclass:
        AdjustVDofs = staticmethod(_fespace.FiniteElementSpace_AdjustVDofs)
    else:
        AdjustVDofs = _fespace.FiniteElementSpace_AdjustVDofs

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
        return _fespace.FiniteElementSpace_RebuildElementToDofTable(self)

    def ReorderElementToDofTable(self):
        return _fespace.FiniteElementSpace_ReorderElementToDofTable(self)

    def BuildDofToArrays(self):
        return _fespace.FiniteElementSpace_BuildDofToArrays(self)

    def GetElementToDofTable(self):
        return _fespace.FiniteElementSpace_GetElementToDofTable(self)

    def GetBdrElementToDofTable(self):
        return _fespace.FiniteElementSpace_GetBdrElementToDofTable(self)

    def GetElementForDof(self, i):
        return _fespace.FiniteElementSpace_GetElementForDof(self, i)

    def GetLocalDofForDof(self, i):
        return _fespace.FiniteElementSpace_GetLocalDofForDof(self, i)

    def GetFE(self, i):
        return _fespace.FiniteElementSpace_GetFE(self, i)

    def GetBE(self, i):
        return _fespace.FiniteElementSpace_GetBE(self, i)

    def GetFaceElement(self, i):
        return _fespace.FiniteElementSpace_GetFaceElement(self, i)

    def GetEdgeElement(self, i):
        return _fespace.FiniteElementSpace_GetEdgeElement(self, i)

    def GetTraceElement(self, i, geom_type):
        return _fespace.FiniteElementSpace_GetTraceElement(self, i, geom_type)

    def GetEssentialVDofs(self, bdr_attr_is_ess, ess_vdofs, component=-1):
        return _fespace.FiniteElementSpace_GetEssentialVDofs(self, bdr_attr_is_ess, ess_vdofs, component)

    def GetEssentialTrueDofs(self, bdr_attr_is_ess, ess_tdof_list, component=-1):
        return _fespace.FiniteElementSpace_GetEssentialTrueDofs(self, bdr_attr_is_ess, ess_tdof_list, component)
    if _newclass:
        MarkerToList = staticmethod(_fespace.FiniteElementSpace_MarkerToList)
    else:
        MarkerToList = _fespace.FiniteElementSpace_MarkerToList
    if _newclass:
        ListToMarker = staticmethod(_fespace.FiniteElementSpace_ListToMarker)
    else:
        ListToMarker = _fespace.FiniteElementSpace_ListToMarker

    def ConvertToConformingVDofs(self, dofs, cdofs):
        return _fespace.FiniteElementSpace_ConvertToConformingVDofs(self, dofs, cdofs)

    def ConvertFromConformingVDofs(self, cdofs, dofs):
        return _fespace.FiniteElementSpace_ConvertFromConformingVDofs(self, cdofs, dofs)

    def D2C_GlobalRestrictionMatrix(self, cfes):
        return _fespace.FiniteElementSpace_D2C_GlobalRestrictionMatrix(self, cfes)

    def D2Const_GlobalRestrictionMatrix(self, cfes):
        return _fespace.FiniteElementSpace_D2Const_GlobalRestrictionMatrix(self, cfes)

    def H2L_GlobalRestrictionMatrix(self, lfes):
        return _fespace.FiniteElementSpace_H2L_GlobalRestrictionMatrix(self, lfes)

    def GetTransferOperator(self, coarse_fes, T):
        return _fespace.FiniteElementSpace_GetTransferOperator(self, coarse_fes, T)

    def GetTrueTransferOperator(self, coarse_fes, T):
        return _fespace.FiniteElementSpace_GetTrueTransferOperator(self, coarse_fes, T)

    def Update(self, want_transform=True):
        return _fespace.FiniteElementSpace_Update(self, want_transform)

    def GetUpdateOperator(self, *args):
        return _fespace.FiniteElementSpace_GetUpdateOperator(self, *args)

    def SetUpdateOperatorOwner(self, own):
        return _fespace.FiniteElementSpace_SetUpdateOperatorOwner(self, own)

    def SetUpdateOperatorType(self, tid):
        return _fespace.FiniteElementSpace_SetUpdateOperatorType(self, tid)

    def UpdatesFinished(self):
        return _fespace.FiniteElementSpace_UpdatesFinished(self)

    def GetSequence(self):
        return _fespace.FiniteElementSpace_GetSequence(self)

    def Save(self, out):
        return _fespace.FiniteElementSpace_Save(self, out)

    def Load(self, m, input):
        return _fespace.FiniteElementSpace_Load(self, m, input)
    __swig_destroy__ = _fespace.delete_FiniteElementSpace
    __del__ = lambda self: None
FiniteElementSpace_swigregister = _fespace.FiniteElementSpace_swigregister
FiniteElementSpace_swigregister(FiniteElementSpace)

def FiniteElementSpace_AdjustVDofs(vdofs):
    return _fespace.FiniteElementSpace_AdjustVDofs(vdofs)
FiniteElementSpace_AdjustVDofs = _fespace.FiniteElementSpace_AdjustVDofs

def FiniteElementSpace_MarkerToList(marker, list):
    return _fespace.FiniteElementSpace_MarkerToList(marker, list)
FiniteElementSpace_MarkerToList = _fespace.FiniteElementSpace_MarkerToList

def FiniteElementSpace_ListToMarker(list, marker_size, marker, mark_val=-1):
    return _fespace.FiniteElementSpace_ListToMarker(list, marker_size, marker, mark_val)
FiniteElementSpace_ListToMarker = _fespace.FiniteElementSpace_ListToMarker

class QuadratureSpace(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, QuadratureSpace, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, QuadratureSpace, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _fespace.new_QuadratureSpace(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _fespace.delete_QuadratureSpace
    __del__ = lambda self: None

    def GetSize(self):
        return _fespace.QuadratureSpace_GetSize(self)

    def GetElementIntRule(self, idx):
        return _fespace.QuadratureSpace_GetElementIntRule(self, idx)

    def Save(self, out):
        return _fespace.QuadratureSpace_Save(self, out)
QuadratureSpace_swigregister = _fespace.QuadratureSpace_swigregister
QuadratureSpace_swigregister(QuadratureSpace)

# This file is compatible with both classic and new-style classes.



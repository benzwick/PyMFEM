# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pnonlinearform', [dirname(__file__)])
        except ImportError:
            import _pnonlinearform
            return _pnonlinearform
        if fp is not None:
            try:
                _mod = imp.load_module('_pnonlinearform', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pnonlinearform = swig_import_helper()
    del swig_import_helper
else:
    import _pnonlinearform
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


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


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


try:
    import weakref
    weakref_proxy = weakref.proxy
except Exception:
    weakref_proxy = lambda x: x



_pnonlinearform.MFEM_TIMER_TYPE_swigconstant(_pnonlinearform)
MFEM_TIMER_TYPE = _pnonlinearform.MFEM_TIMER_TYPE
import vector
import array
import ostream_typemap
import nonlinearform
import operators
import fespace
import coefficient
import matrix
import intrules
import sparsemat
import densemat
import eltrans
import fe
import mesh
import ncmesh
import element
import geom
import table
import vertex
import gridfunc
import bilininteg
import fe_coll
import lininteg
import linearform
import nonlininteg
import pfespace
import pmesh
import pncmesh
import communication
import sets
import hypre
import pgridfunc
class ParNonlinearForm(nonlinearform.NonlinearForm):
    __swig_setmethods__ = {}
    for _s in [nonlinearform.NonlinearForm]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ParNonlinearForm, name, value)
    __swig_getmethods__ = {}
    for _s in [nonlinearform.NonlinearForm]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ParNonlinearForm, name)
    __repr__ = _swig_repr

    def __init__(self, pf):
        this = _pnonlinearform.new_ParNonlinearForm(pf)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def ParFESpace(self):
        return _pnonlinearform.ParNonlinearForm_ParFESpace(self)

    def SetEssentialBC(self, bdr_attr_is_ess, rhs=None):
        return _pnonlinearform.ParNonlinearForm_SetEssentialBC(self, bdr_attr_is_ess, rhs)

    def GetEnergy(self, *args):
        return _pnonlinearform.ParNonlinearForm_GetEnergy(self, *args)

    def Mult(self, x, y):
        return _pnonlinearform.ParNonlinearForm_Mult(self, x, y)

    def GetLocalGradient(self, x):
        return _pnonlinearform.ParNonlinearForm_GetLocalGradient(self, x)

    def GetGradient(self, x):
        return _pnonlinearform.ParNonlinearForm_GetGradient(self, x)

    def SetGradientType(self, tid):
        return _pnonlinearform.ParNonlinearForm_SetGradientType(self, tid)
    __swig_destroy__ = _pnonlinearform.delete_ParNonlinearForm
    __del__ = lambda self: None
ParNonlinearForm_swigregister = _pnonlinearform.ParNonlinearForm_swigregister
ParNonlinearForm_swigregister(ParNonlinearForm)

# This file is compatible with both classic and new-style classes.



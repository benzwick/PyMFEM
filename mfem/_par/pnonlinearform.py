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
        mname = '.'.join((pkg, '_pnonlinearform')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_pnonlinearform')
    _pnonlinearform = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pnonlinearform', [dirname(__file__)])
        except ImportError:
            import _pnonlinearform
            return _pnonlinearform
        try:
            _mod = imp.load_module('_pnonlinearform', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _pnonlinearform = swig_import_helper()
    del swig_import_helper
else:
    import _pnonlinearform
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


MFEM_VERSION = _pnonlinearform.MFEM_VERSION
MFEM_VERSION_STRING = _pnonlinearform.MFEM_VERSION_STRING
MFEM_VERSION_TYPE = _pnonlinearform.MFEM_VERSION_TYPE
MFEM_VERSION_TYPE_RELEASE = _pnonlinearform.MFEM_VERSION_TYPE_RELEASE
MFEM_VERSION_TYPE_DEVELOPMENT = _pnonlinearform.MFEM_VERSION_TYPE_DEVELOPMENT
MFEM_VERSION_MAJOR = _pnonlinearform.MFEM_VERSION_MAJOR
MFEM_VERSION_MINOR = _pnonlinearform.MFEM_VERSION_MINOR
MFEM_VERSION_PATCH = _pnonlinearform.MFEM_VERSION_PATCH
MFEM_SOURCE_DIR = _pnonlinearform.MFEM_SOURCE_DIR
MFEM_INSTALL_DIR = _pnonlinearform.MFEM_INSTALL_DIR
MFEM_TIMER_TYPE = _pnonlinearform.MFEM_TIMER_TYPE
MFEM_HYPRE_VERSION = _pnonlinearform.MFEM_HYPRE_VERSION
import mfem._par.vector
import mfem._par.array
import mfem._ser.ostream_typemap
import mfem._par.mem_manager
import mfem._par.nonlinearform
import mfem._par.operators
import mfem._par.fespace
import mfem._par.coefficient
import mfem._par.matrix
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
import mfem._par.nonlininteg
import mfem._par.blockoperator
import mfem._par.pfespace
import mfem._par.pmesh
import mfem._par.pncmesh
import mfem._par.communication
import mfem._par.sets
import mfem._par.pgridfunc
class ParNonlinearForm(mfem._par.nonlinearform.NonlinearForm):
    """Proxy of C++ mfem::ParNonlinearForm class."""

    __swig_setmethods__ = {}
    for _s in [mfem._par.nonlinearform.NonlinearForm]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ParNonlinearForm, name, value)
    __swig_getmethods__ = {}
    for _s in [mfem._par.nonlinearform.NonlinearForm]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ParNonlinearForm, name)
    __repr__ = _swig_repr

    def __init__(self, pf):
        """__init__(mfem::ParNonlinearForm self, ParFiniteElementSpace pf) -> ParNonlinearForm"""
        this = _pnonlinearform.new_ParNonlinearForm(pf)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def ParFESpace(self):
        """ParFESpace(ParNonlinearForm self) -> ParFiniteElementSpace"""
        return _pnonlinearform.ParNonlinearForm_ParFESpace(self)


    def GetParGridFunctionEnergy(self, x):
        """GetParGridFunctionEnergy(ParNonlinearForm self, Vector x) -> double"""
        return _pnonlinearform.ParNonlinearForm_GetParGridFunctionEnergy(self, x)


    def GetEnergy(self, *args):
        """
        GetEnergy(ParNonlinearForm self, ParGridFunction x) -> double
        GetEnergy(ParNonlinearForm self, Vector x) -> double
        """
        return _pnonlinearform.ParNonlinearForm_GetEnergy(self, *args)


    def Mult(self, x, y):
        """Mult(ParNonlinearForm self, Vector x, Vector y)"""
        return _pnonlinearform.ParNonlinearForm_Mult(self, x, y)


    def GetLocalGradient(self, x):
        """GetLocalGradient(ParNonlinearForm self, Vector x) -> SparseMatrix"""
        return _pnonlinearform.ParNonlinearForm_GetLocalGradient(self, x)


    def GetGradient(self, x):
        """GetGradient(ParNonlinearForm self, Vector x) -> Operator"""
        return _pnonlinearform.ParNonlinearForm_GetGradient(self, x)


    def SetGradientType(self, tid):
        """SetGradientType(ParNonlinearForm self, mfem::Operator::Type tid)"""
        return _pnonlinearform.ParNonlinearForm_SetGradientType(self, tid)


    def Update(self):
        """Update(ParNonlinearForm self)"""
        return _pnonlinearform.ParNonlinearForm_Update(self)

    __swig_destroy__ = _pnonlinearform.delete_ParNonlinearForm
    __del__ = lambda self: None
ParNonlinearForm_swigregister = _pnonlinearform.ParNonlinearForm_swigregister
ParNonlinearForm_swigregister(ParNonlinearForm)

class ParBlockNonlinearForm(mfem._par.nonlinearform.BlockNonlinearForm):
    """Proxy of C++ mfem::ParBlockNonlinearForm class."""

    __swig_setmethods__ = {}
    for _s in [mfem._par.nonlinearform.BlockNonlinearForm]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ParBlockNonlinearForm, name, value)
    __swig_getmethods__ = {}
    for _s in [mfem._par.nonlinearform.BlockNonlinearForm]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ParBlockNonlinearForm, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(mfem::ParBlockNonlinearForm self) -> ParBlockNonlinearForm
        __init__(mfem::ParBlockNonlinearForm self, mfem::Array< mfem::ParFiniteElementSpace * > & pf) -> ParBlockNonlinearForm
        """
        this = _pnonlinearform.new_ParBlockNonlinearForm(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def ParFESpace(self, *args):
        """
        ParFESpace(ParBlockNonlinearForm self, int k) -> ParFiniteElementSpace
        ParFESpace(ParBlockNonlinearForm self, int k) -> ParFiniteElementSpace
        """
        return _pnonlinearform.ParBlockNonlinearForm_ParFESpace(self, *args)


    def SetParSpaces(self, pf):
        """SetParSpaces(ParBlockNonlinearForm self, mfem::Array< mfem::ParFiniteElementSpace * > & pf)"""
        return _pnonlinearform.ParBlockNonlinearForm_SetParSpaces(self, pf)


    def SetEssentialBC(self, bdr_attr_is_ess, rhs):
        """SetEssentialBC(ParBlockNonlinearForm self, mfem::Array< mfem::Array< int > * > const & bdr_attr_is_ess, mfem::Array< mfem::Vector * > & rhs)"""
        return _pnonlinearform.ParBlockNonlinearForm_SetEssentialBC(self, bdr_attr_is_ess, rhs)


    def Mult(self, x, y):
        """Mult(ParBlockNonlinearForm self, Vector x, Vector y)"""
        return _pnonlinearform.ParBlockNonlinearForm_Mult(self, x, y)


    def GetLocalGradient(self, x):
        """GetLocalGradient(ParBlockNonlinearForm self, Vector x) -> BlockOperator"""
        return _pnonlinearform.ParBlockNonlinearForm_GetLocalGradient(self, x)


    def GetGradient(self, x):
        """GetGradient(ParBlockNonlinearForm self, Vector x) -> BlockOperator"""
        return _pnonlinearform.ParBlockNonlinearForm_GetGradient(self, x)


    def SetGradientType(self, tid):
        """SetGradientType(ParBlockNonlinearForm self, mfem::Operator::Type tid)"""
        return _pnonlinearform.ParBlockNonlinearForm_SetGradientType(self, tid)

    __swig_destroy__ = _pnonlinearform.delete_ParBlockNonlinearForm
    __del__ = lambda self: None
ParBlockNonlinearForm_swigregister = _pnonlinearform.ParBlockNonlinearForm_swigregister
ParBlockNonlinearForm_swigregister(ParBlockNonlinearForm)

# This file is compatible with both classic and new-style classes.



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
        mname = '.'.join((pkg, '_sparsesmoothers')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_sparsesmoothers')
    _sparsesmoothers = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_sparsesmoothers', [dirname(__file__)])
        except ImportError:
            import _sparsesmoothers
            return _sparsesmoothers
        try:
            _mod = imp.load_module('_sparsesmoothers', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _sparsesmoothers = swig_import_helper()
    del swig_import_helper
else:
    import _sparsesmoothers
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


import mfem._par.vector
import mfem._par.array
import mfem._ser.ostream_typemap
import mfem._par.mem_manager
import mfem._par.operators
import mfem._par.sparsemat
import mfem._par.matrix
import mfem._par.densemat
class SparseSmoother(mfem._par.matrix.MatrixInverse):
    """Proxy of C++ mfem::SparseSmoother class."""

    __swig_setmethods__ = {}
    for _s in [mfem._par.matrix.MatrixInverse]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SparseSmoother, name, value)
    __swig_getmethods__ = {}
    for _s in [mfem._par.matrix.MatrixInverse]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, SparseSmoother, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def SetOperator(self, a):
        """SetOperator(SparseSmoother self, Operator a)"""
        return _sparsesmoothers.SparseSmoother_SetOperator(self, a)

    __swig_destroy__ = _sparsesmoothers.delete_SparseSmoother
    __del__ = lambda self: None
SparseSmoother_swigregister = _sparsesmoothers.SparseSmoother_swigregister
SparseSmoother_swigregister(SparseSmoother)

class GSSmoother(SparseSmoother):
    """Proxy of C++ mfem::GSSmoother class."""

    __swig_setmethods__ = {}
    for _s in [SparseSmoother]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, GSSmoother, name, value)
    __swig_getmethods__ = {}
    for _s in [SparseSmoother]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, GSSmoother, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(mfem::GSSmoother self, int t=0, int it=1) -> GSSmoother
        __init__(mfem::GSSmoother self, int t=0) -> GSSmoother
        __init__(mfem::GSSmoother self) -> GSSmoother
        __init__(mfem::GSSmoother self, SparseMatrix a, int t=0, int it=1) -> GSSmoother
        __init__(mfem::GSSmoother self, SparseMatrix a, int t=0) -> GSSmoother
        __init__(mfem::GSSmoother self, SparseMatrix a) -> GSSmoother
        """
        this = _sparsesmoothers.new_GSSmoother(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Mult(self, x, y):
        """Mult(GSSmoother self, Vector x, Vector y)"""
        return _sparsesmoothers.GSSmoother_Mult(self, x, y)

    __swig_destroy__ = _sparsesmoothers.delete_GSSmoother
    __del__ = lambda self: None
GSSmoother_swigregister = _sparsesmoothers.GSSmoother_swigregister
GSSmoother_swigregister(GSSmoother)

class DSmoother(SparseSmoother):
    """Proxy of C++ mfem::DSmoother class."""

    __swig_setmethods__ = {}
    for _s in [SparseSmoother]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, DSmoother, name, value)
    __swig_getmethods__ = {}
    for _s in [SparseSmoother]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, DSmoother, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(mfem::DSmoother self, int t=0, double s=1., int it=1) -> DSmoother
        __init__(mfem::DSmoother self, int t=0, double s=1.) -> DSmoother
        __init__(mfem::DSmoother self, int t=0) -> DSmoother
        __init__(mfem::DSmoother self) -> DSmoother
        __init__(mfem::DSmoother self, SparseMatrix a, int t=0, double s=1., int it=1) -> DSmoother
        __init__(mfem::DSmoother self, SparseMatrix a, int t=0, double s=1.) -> DSmoother
        __init__(mfem::DSmoother self, SparseMatrix a, int t=0) -> DSmoother
        __init__(mfem::DSmoother self, SparseMatrix a) -> DSmoother
        """
        this = _sparsesmoothers.new_DSmoother(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Mult(self, x, y):
        """Mult(DSmoother self, Vector x, Vector y)"""
        return _sparsesmoothers.DSmoother_Mult(self, x, y)

    __swig_destroy__ = _sparsesmoothers.delete_DSmoother
    __del__ = lambda self: None
DSmoother_swigregister = _sparsesmoothers.DSmoother_swigregister
DSmoother_swigregister(DSmoother)

# This file is compatible with both classic and new-style classes.



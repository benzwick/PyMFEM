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
        mname = '.'.join((pkg, '_array')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_array')
    _array = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_array', [dirname(__file__)])
        except ImportError:
            import _array
            return _array
        try:
            _mod = imp.load_module('_array', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _array = swig_import_helper()
    del swig_import_helper
else:
    import _array
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

import ostream_typemap
class BaseArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BaseArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BaseArray, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
BaseArray_swigregister = _array.BaseArray_swigregister
BaseArray_swigregister(BaseArray)

class intArray(BaseArray):
    __swig_setmethods__ = {}
    for _s in [BaseArray]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, intArray, name, value)
    __swig_getmethods__ = {}
    for _s in [BaseArray]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, intArray, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _array.new_intArray(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

        if len(args) == 1 and isinstance(args[0], list):
            self.MakeDataOwner()



    __swig_destroy__ = _array.delete_intArray
    __del__ = lambda self: None

    def GetData(self, *args):
        return _array.intArray_GetData(self, *args)

    def OwnsData(self):
        return _array.intArray_OwnsData(self)

    def StealData(self, p):
        return _array.intArray_StealData(self, p)

    def LoseData(self):
        return _array.intArray_LoseData(self)

    def MakeDataOwner(self):
        return _array.intArray_MakeDataOwner(self)

    def Size(self):
        return _array.intArray_Size(self)

    def SetSize(self, *args):
        return _array.intArray_SetSize(self, *args)

    def Capacity(self):
        return _array.intArray_Capacity(self)

    def Reserve(self, capacity):
        return _array.intArray_Reserve(self, capacity)

    def Append(self, *args):
        return _array.intArray_Append(self, *args)

    def Prepend(self, el):
        return _array.intArray_Prepend(self, el)

    def Last(self, *args):
        return _array.intArray_Last(self, *args)

    def Union(self, el):
        return _array.intArray_Union(self, el)

    def Find(self, el):
        return _array.intArray_Find(self, el)

    def FindSorted(self, el):
        return _array.intArray_FindSorted(self, el)

    def DeleteLast(self):
        return _array.intArray_DeleteLast(self)

    def DeleteFirst(self, el):
        return _array.intArray_DeleteFirst(self, el)

    def DeleteAll(self):
        return _array.intArray_DeleteAll(self)

    def Copy(self, copy):
        return _array.intArray_Copy(self, copy)

    def MakeRef(self, *args):
        return _array.intArray_MakeRef(self, *args)

    def GetSubArray(self, offset, sa_size, sa):
        return _array.intArray_GetSubArray(self, offset, sa_size, sa)

    def Print(self, *args):
        return _array.intArray_Print(self, *args)

    def Save(self, out, fmt=0):
        return _array.intArray_Save(self, out, fmt)

    def Load(self, *args):
        return _array.intArray_Load(self, *args)

    def Max(self):
        return _array.intArray_Max(self)

    def Min(self):
        return _array.intArray_Min(self)

    def Sort(self):
        return _array.intArray_Sort(self)

    def Unique(self):
        return _array.intArray_Unique(self)

    def IsSorted(self):
        return _array.intArray_IsSorted(self)

    def PartialSum(self):
        return _array.intArray_PartialSum(self)

    def Sum(self):
        return _array.intArray_Sum(self)

    def begin(self):
        return _array.intArray_begin(self)

    def end(self):
        return _array.intArray_end(self)

    def MemoryUsage(self):
        return _array.intArray_MemoryUsage(self)

    def __setitem__(self, i, v):
        return _array.intArray___setitem__(self, i, v)

    def __getitem__(self, i):
        return _array.intArray___getitem__(self, i)

    def Assign(self, *args):
        return _array.intArray_Assign(self, *args)

    def ToList(self):
        return [self[i] for i in range(self.Size())]


intArray_swigregister = _array.intArray_swigregister
intArray_swigregister(intArray)

class doubleArray(BaseArray):
    __swig_setmethods__ = {}
    for _s in [BaseArray]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, doubleArray, name, value)
    __swig_getmethods__ = {}
    for _s in [BaseArray]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, doubleArray, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _array.new_doubleArray(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

        if len(args) == 1 and isinstance(args[0], list):
            self.MakeDataOwner()



    __swig_destroy__ = _array.delete_doubleArray
    __del__ = lambda self: None

    def GetData(self, *args):
        return _array.doubleArray_GetData(self, *args)

    def OwnsData(self):
        return _array.doubleArray_OwnsData(self)

    def StealData(self, p):
        return _array.doubleArray_StealData(self, p)

    def LoseData(self):
        return _array.doubleArray_LoseData(self)

    def MakeDataOwner(self):
        return _array.doubleArray_MakeDataOwner(self)

    def Size(self):
        return _array.doubleArray_Size(self)

    def SetSize(self, *args):
        return _array.doubleArray_SetSize(self, *args)

    def Capacity(self):
        return _array.doubleArray_Capacity(self)

    def Reserve(self, capacity):
        return _array.doubleArray_Reserve(self, capacity)

    def Append(self, *args):
        return _array.doubleArray_Append(self, *args)

    def Prepend(self, el):
        return _array.doubleArray_Prepend(self, el)

    def Last(self, *args):
        return _array.doubleArray_Last(self, *args)

    def Union(self, el):
        return _array.doubleArray_Union(self, el)

    def Find(self, el):
        return _array.doubleArray_Find(self, el)

    def FindSorted(self, el):
        return _array.doubleArray_FindSorted(self, el)

    def DeleteLast(self):
        return _array.doubleArray_DeleteLast(self)

    def DeleteFirst(self, el):
        return _array.doubleArray_DeleteFirst(self, el)

    def DeleteAll(self):
        return _array.doubleArray_DeleteAll(self)

    def Copy(self, copy):
        return _array.doubleArray_Copy(self, copy)

    def MakeRef(self, *args):
        return _array.doubleArray_MakeRef(self, *args)

    def GetSubArray(self, offset, sa_size, sa):
        return _array.doubleArray_GetSubArray(self, offset, sa_size, sa)

    def Print(self, *args):
        return _array.doubleArray_Print(self, *args)

    def Save(self, out, fmt=0):
        return _array.doubleArray_Save(self, out, fmt)

    def Load(self, *args):
        return _array.doubleArray_Load(self, *args)

    def Max(self):
        return _array.doubleArray_Max(self)

    def Min(self):
        return _array.doubleArray_Min(self)

    def Sort(self):
        return _array.doubleArray_Sort(self)

    def Unique(self):
        return _array.doubleArray_Unique(self)

    def IsSorted(self):
        return _array.doubleArray_IsSorted(self)

    def PartialSum(self):
        return _array.doubleArray_PartialSum(self)

    def Sum(self):
        return _array.doubleArray_Sum(self)

    def begin(self):
        return _array.doubleArray_begin(self)

    def end(self):
        return _array.doubleArray_end(self)

    def MemoryUsage(self):
        return _array.doubleArray_MemoryUsage(self)

    def __setitem__(self, i, v):
        return _array.doubleArray___setitem__(self, i, v)

    def __getitem__(self, i):
        return _array.doubleArray___getitem__(self, i)

    def Assign(self, *args):
        return _array.doubleArray_Assign(self, *args)

    def ToList(self):
        return [self[i] for i in range(self.Size())]


doubleArray_swigregister = _array.doubleArray_swigregister
doubleArray_swigregister(doubleArray)


def doubleSwap(*args):
    return _array.doubleSwap(*args)
doubleSwap = _array.doubleSwap

def intSwap(*args):
    return _array.intSwap(*args)
intSwap = _array.intSwap
# This file is compatible with both classic and new-style classes.



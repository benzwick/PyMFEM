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
            fp, pathname, description = imp.find_module('_sparsemat', [dirname(__file__)])
        except ImportError:
            import _sparsemat
            return _sparsemat
        if fp is not None:
            try:
                _mod = imp.load_module('_sparsemat', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _sparsemat = swig_import_helper()
    del swig_import_helper
else:
    import _sparsemat
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


import array
import vector
import operators
import matrix
import densemat

def RAP_P(A, R, ORAP):
    return _sparsemat.RAP_P(A, R, ORAP)
RAP_P = _sparsemat.RAP_P

def RAP_R(Rt, A, P):
    return _sparsemat.RAP_R(Rt, A, P)
RAP_R = _sparsemat.RAP_R
class RowNode(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RowNode, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RowNode, name)
    __repr__ = _swig_repr
    __swig_setmethods__["Value"] = _sparsemat.RowNode_Value_set
    __swig_getmethods__["Value"] = _sparsemat.RowNode_Value_get
    if _newclass:
        Value = _swig_property(_sparsemat.RowNode_Value_get, _sparsemat.RowNode_Value_set)
    __swig_setmethods__["Prev"] = _sparsemat.RowNode_Prev_set
    __swig_getmethods__["Prev"] = _sparsemat.RowNode_Prev_get
    if _newclass:
        Prev = _swig_property(_sparsemat.RowNode_Prev_get, _sparsemat.RowNode_Prev_set)
    __swig_setmethods__["Column"] = _sparsemat.RowNode_Column_set
    __swig_getmethods__["Column"] = _sparsemat.RowNode_Column_get
    if _newclass:
        Column = _swig_property(_sparsemat.RowNode_Column_get, _sparsemat.RowNode_Column_set)

    def __init__(self):
        this = _sparsemat.new_RowNode()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _sparsemat.delete_RowNode
    __del__ = lambda self: None
RowNode_swigregister = _sparsemat.RowNode_swigregister
RowNode_swigregister(RowNode)

class SparseMatrix(matrix.AbstractSparseMatrix):
    __swig_setmethods__ = {}
    for _s in [matrix.AbstractSparseMatrix]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SparseMatrix, name, value)
    __swig_getmethods__ = {}
    for _s in [matrix.AbstractSparseMatrix]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, SparseMatrix, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _sparsemat.new_SparseMatrix(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def MakeRef(self, master):
        return _sparsemat.SparseMatrix_MakeRef(self, master)

    def Size(self):
        return _sparsemat.SparseMatrix_Size(self)

    def Clear(self):
        return _sparsemat.SparseMatrix_Clear(self)

    def Empty(self):
        return _sparsemat.SparseMatrix_Empty(self)

    def GetI(self):
        return _sparsemat.SparseMatrix_GetI(self)

    def GetJ(self):
        return _sparsemat.SparseMatrix_GetJ(self)

    def GetData(self):
        return _sparsemat.SparseMatrix_GetData(self)

    def RowSize(self, i):
        return _sparsemat.SparseMatrix_RowSize(self, i)

    def MaxRowSize(self):
        return _sparsemat.SparseMatrix_MaxRowSize(self)

    def GetRowColumns(self, *args):
        return _sparsemat.SparseMatrix_GetRowColumns(self, *args)

    def GetRowEntries(self, *args):
        return _sparsemat.SparseMatrix_GetRowEntries(self, *args)

    def SetWidth(self, width_=-1):
        return _sparsemat.SparseMatrix_SetWidth(self, width_)

    def ActualWidth(self):
        return _sparsemat.SparseMatrix_ActualWidth(self)

    def SortColumnIndices(self):
        return _sparsemat.SparseMatrix_SortColumnIndices(self)

    def MoveDiagonalFirst(self):
        return _sparsemat.SparseMatrix_MoveDiagonalFirst(self)

    def Elem(self, *args):
        return _sparsemat.SparseMatrix_Elem(self, *args)

    def __call__(self, *args):
        return _sparsemat.SparseMatrix___call__(self, *args)

    def GetDiag(self, d):
        return _sparsemat.SparseMatrix_GetDiag(self, d)

    def Mult(self, x, y):
        return _sparsemat.SparseMatrix_Mult(self, x, y)

    def AddMult(self, x, y, a=1.0):
        return _sparsemat.SparseMatrix_AddMult(self, x, y, a)

    def MultTranspose(self, x, y):
        return _sparsemat.SparseMatrix_MultTranspose(self, x, y)

    def AddMultTranspose(self, x, y, a=1.0):
        return _sparsemat.SparseMatrix_AddMultTranspose(self, x, y, a)

    def PartMult(self, rows, x, y):
        return _sparsemat.SparseMatrix_PartMult(self, rows, x, y)

    def PartAddMult(self, rows, x, y, a=1.0):
        return _sparsemat.SparseMatrix_PartAddMult(self, rows, x, y, a)

    def BooleanMult(self, x, y):
        return _sparsemat.SparseMatrix_BooleanMult(self, x, y)

    def BooleanMultTranspose(self, x, y):
        return _sparsemat.SparseMatrix_BooleanMultTranspose(self, x, y)

    def InnerProduct(self, x, y):
        return _sparsemat.SparseMatrix_InnerProduct(self, x, y)

    def GetRowSums(self, x):
        return _sparsemat.SparseMatrix_GetRowSums(self, x)

    def GetRowNorml1(self, irow):
        return _sparsemat.SparseMatrix_GetRowNorml1(self, irow)

    def Inverse(self):
        return _sparsemat.SparseMatrix_Inverse(self)

    def EliminateRow(self, *args):
        return _sparsemat.SparseMatrix_EliminateRow(self, *args)

    def EliminateCol(self, col):
        return _sparsemat.SparseMatrix_EliminateCol(self, col)

    def EliminateCols(self, cols, x=None, b=None):
        return _sparsemat.SparseMatrix_EliminateCols(self, cols, x, b)

    def EliminateRowColMultipleRHS(self, rc, sol, rhs, d=0):
        return _sparsemat.SparseMatrix_EliminateRowColMultipleRHS(self, rc, sol, rhs, d)

    def EliminateRowColDiag(self, rc, value):
        return _sparsemat.SparseMatrix_EliminateRowColDiag(self, rc, value)

    def EliminateRowCol(self, *args):
        return _sparsemat.SparseMatrix_EliminateRowCol(self, *args)

    def SetDiagIdentity(self):
        return _sparsemat.SparseMatrix_SetDiagIdentity(self)

    def EliminateZeroRows(self):
        return _sparsemat.SparseMatrix_EliminateZeroRows(self)

    def Gauss_Seidel_forw(self, x, y):
        return _sparsemat.SparseMatrix_Gauss_Seidel_forw(self, x, y)

    def Gauss_Seidel_back(self, x, y):
        return _sparsemat.SparseMatrix_Gauss_Seidel_back(self, x, y)

    def GetJacobiScaling(self):
        return _sparsemat.SparseMatrix_GetJacobiScaling(self)

    def Jacobi(self, b, x0, x1, sc):
        return _sparsemat.SparseMatrix_Jacobi(self, b, x0, x1, sc)

    def DiagScale(self, b, x, sc=1.0):
        return _sparsemat.SparseMatrix_DiagScale(self, b, x, sc)

    def Jacobi2(self, b, x0, x1, sc=1.0):
        return _sparsemat.SparseMatrix_Jacobi2(self, b, x0, x1, sc)

    def Jacobi3(self, b, x0, x1, sc=1.0):
        return _sparsemat.SparseMatrix_Jacobi3(self, b, x0, x1, sc)

    def Finalize(self, *args):
        return _sparsemat.SparseMatrix_Finalize(self, *args)

    def Finalized(self):
        return _sparsemat.SparseMatrix_Finalized(self)

    def areColumnsSorted(self):
        return _sparsemat.SparseMatrix_areColumnsSorted(self)

    def GetBlocks(self, blocks):
        return _sparsemat.SparseMatrix_GetBlocks(self, blocks)

    def GetSubMatrix(self, rows, cols, subm):
        return _sparsemat.SparseMatrix_GetSubMatrix(self, rows, cols, subm)

    def SetColPtr(self, row):
        return _sparsemat.SparseMatrix_SetColPtr(self, row)

    def ClearColPtr(self):
        return _sparsemat.SparseMatrix_ClearColPtr(self)

    def _Get_(self, col):
        return _sparsemat.SparseMatrix__Get_(self, col)

    def SearchRow(self, *args):
        return _sparsemat.SparseMatrix_SearchRow(self, *args)

    def _Add_(self, *args):
        return _sparsemat.SparseMatrix__Add_(self, *args)

    def _Set_(self, *args):
        return _sparsemat.SparseMatrix__Set_(self, *args)

    def Set(self, i, j, a):
        return _sparsemat.SparseMatrix_Set(self, i, j, a)

    def SetSubMatrix(self, rows, cols, subm, skip_zeros=1):
        return _sparsemat.SparseMatrix_SetSubMatrix(self, rows, cols, subm, skip_zeros)

    def SetSubMatrixTranspose(self, rows, cols, subm, skip_zeros=1):
        return _sparsemat.SparseMatrix_SetSubMatrixTranspose(self, rows, cols, subm, skip_zeros)

    def AddSubMatrix(self, rows, cols, subm, skip_zeros=1):
        return _sparsemat.SparseMatrix_AddSubMatrix(self, rows, cols, subm, skip_zeros)

    def RowIsEmpty(self, row):
        return _sparsemat.SparseMatrix_RowIsEmpty(self, row)

    def GetRow(self, row, cols, srow):
        return _sparsemat.SparseMatrix_GetRow(self, row, cols, srow)

    def SetRow(self, row, cols, srow):
        return _sparsemat.SparseMatrix_SetRow(self, row, cols, srow)

    def AddRow(self, row, cols, srow):
        return _sparsemat.SparseMatrix_AddRow(self, row, cols, srow)

    def ScaleRow(self, row, scale):
        return _sparsemat.SparseMatrix_ScaleRow(self, row, scale)

    def ScaleRows(self, sl):
        return _sparsemat.SparseMatrix_ScaleRows(self, sl)

    def ScaleColumns(self, sr):
        return _sparsemat.SparseMatrix_ScaleColumns(self, sr)

    def __iadd__(self, B):
        val = _sparsemat.SparseMatrix___iadd__(self, B)

        val.thisown = self.thisown


        return val


    def Add(self, *args):
        return _sparsemat.SparseMatrix_Add(self, *args)

    def __imul__(self, a):
        val = _sparsemat.SparseMatrix___imul__(self, a)

        val.thisown = self.thisown


        return val


    def Print(self, *args):
        return _sparsemat.SparseMatrix_Print(self, *args)

    def PrintMatlab(self, *args):
        return _sparsemat.SparseMatrix_PrintMatlab(self, *args)

    def PrintMM(self, *args):
        return _sparsemat.SparseMatrix_PrintMM(self, *args)

    def PrintCSR(self, out):
        return _sparsemat.SparseMatrix_PrintCSR(self, out)

    def PrintCSR2(self, out):
        return _sparsemat.SparseMatrix_PrintCSR2(self, out)

    def PrintInfo(self, out):
        return _sparsemat.SparseMatrix_PrintInfo(self, out)

    def IsSymmetric(self):
        return _sparsemat.SparseMatrix_IsSymmetric(self)

    def Symmetrize(self):
        return _sparsemat.SparseMatrix_Symmetrize(self)

    def NumNonZeroElems(self):
        return _sparsemat.SparseMatrix_NumNonZeroElems(self)

    def MaxNorm(self):
        return _sparsemat.SparseMatrix_MaxNorm(self)

    def CountSmallElems(self, tol):
        return _sparsemat.SparseMatrix_CountSmallElems(self, tol)

    def CheckFinite(self):
        return _sparsemat.SparseMatrix_CheckFinite(self)

    def SetGraphOwner(self, ownij):
        return _sparsemat.SparseMatrix_SetGraphOwner(self, ownij)

    def SetDataOwner(self, owna):
        return _sparsemat.SparseMatrix_SetDataOwner(self, owna)

    def OwnsGraph(self):
        return _sparsemat.SparseMatrix_OwnsGraph(self)

    def OwnsData(self):
        return _sparsemat.SparseMatrix_OwnsData(self)

    def LoseData(self):
        return _sparsemat.SparseMatrix_LoseData(self)

    def Swap(self, other):
        return _sparsemat.SparseMatrix_Swap(self, other)
    __swig_destroy__ = _sparsemat.delete_SparseMatrix
    __del__ = lambda self: None

    def GetType(self):
        return _sparsemat.SparseMatrix_GetType(self)

    def GetIArray(self):
        return _sparsemat.SparseMatrix_GetIArray(self)

    def GetJArray(self):
        return _sparsemat.SparseMatrix_GetJArray(self)

    def GetDataArray(self):
        return _sparsemat.SparseMatrix_GetDataArray(self)
SparseMatrix_swigregister = _sparsemat.SparseMatrix_swigregister
SparseMatrix_swigregister(SparseMatrix)


def SparseMatrixFunction(S, f):
    return _sparsemat.SparseMatrixFunction(S, f)
SparseMatrixFunction = _sparsemat.SparseMatrixFunction

def Transpose(A):
    return _sparsemat.Transpose(A)
Transpose = _sparsemat.Transpose

def TransposeAbstractSparseMatrix(A, useActualWidth):
    return _sparsemat.TransposeAbstractSparseMatrix(A, useActualWidth)
TransposeAbstractSparseMatrix = _sparsemat.TransposeAbstractSparseMatrix

def MultAbstractSparseMatrix(A, B):
    return _sparsemat.MultAbstractSparseMatrix(A, B)
MultAbstractSparseMatrix = _sparsemat.MultAbstractSparseMatrix

def Mult(*args):
    return _sparsemat.Mult(*args)
Mult = _sparsemat.Mult

def RAP(*args):
    return _sparsemat.RAP(*args)
RAP = _sparsemat.RAP

def Mult_AtDA(A, D, OAtDA=None):
    return _sparsemat.Mult_AtDA(A, D, OAtDA)
Mult_AtDA = _sparsemat.Mult_AtDA

def add_sparse(*args):
    return _sparsemat.add_sparse(*args)
add_sparse = _sparsemat.add_sparse
# This file is compatible with both classic and new-style classes.



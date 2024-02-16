from typing import TYPE_CHECKING

import numpy as np

from pyvista.core._validation import validate_array
from pyvista.core._validation._array_wrapper import _ArrayLikeWrapper

# Disable text formatting / linting for this file
# fmt: off
# flake8: noqa

# CASE: Array[T] -> Array[T]
if TYPE_CHECKING:
    # scalars
    reveal_type(_ArrayLikeWrapper(1.0)._array)   # EXPECTED_TYPE: "builtins.float"
    reveal_type(_ArrayLikeWrapper(1)._array)     # EXPECTED_TYPE: "builtins.int"
    reveal_type(_ArrayLikeWrapper(True)._array)  # EXPECTED_TYPE: "builtins.bool"

    reveal_type(validate_array(1.0))   # EXPECTED_TYPE: "builtins.float"
    reveal_type(validate_array(1))     # EXPECTED_TYPE: "builtins.int"
    reveal_type(validate_array(True))  # EXPECTED_TYPE: "builtins.bool"

    # numpy arrays
    reveal_type(_ArrayLikeWrapper(np.array((1.0),dtype=float))._array)  # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.float]]"
    reveal_type(_ArrayLikeWrapper(np.array((1),dtype=int))._array)      # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.int]]"
    reveal_type(_ArrayLikeWrapper(np.array((True),dtype=bool))._array)  # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.bool]]"

    reveal_type(validate_array(np.array((1.0),dtype=float)))  # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.float]]"
    reveal_type(validate_array(np.array((1),dtype=int)))      # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.int]]"
    reveal_type(validate_array(np.array((True),dtype=bool)))  # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.bool]]"

    # lists
    reveal_type(_ArrayLikeWrapper([1.0])._array)         # EXPECTED_TYPE: "typing.Sequence[builtins.float]"
    reveal_type(_ArrayLikeWrapper([1])._array)           # EXPECTED_TYPE: "typing.Sequence[builtins.int]"
    reveal_type(_ArrayLikeWrapper([True])._array)        # EXPECTED_TYPE: "typing.Sequence[builtins.bool]"
    reveal_type(_ArrayLikeWrapper([[1.0]])._array)       # EXPECTED_TYPE: "typing.Sequence[typing.Sequence[builtins.float]]"
    reveal_type(_ArrayLikeWrapper([[1]])._array)         # EXPECTED_TYPE: "typing.Sequence[typing.Sequence[builtins.int]]"
    reveal_type(_ArrayLikeWrapper([[True]])._array)      # EXPECTED_TYPE: "typing.Sequence[typing.Sequence[builtins.bool]]"
    reveal_type(_ArrayLikeWrapper([[[1.0]]])._array)     # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.float]]"
    reveal_type(_ArrayLikeWrapper([[[1]]])._array)       # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.int]]"
    reveal_type(_ArrayLikeWrapper([[[True]]])._array)    # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.bool]]"
    reveal_type(_ArrayLikeWrapper([[[[1.0]]]])._array)   # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.float]]"
    reveal_type(_ArrayLikeWrapper([[[[1]]]])._array)     # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.int]]"
    reveal_type(_ArrayLikeWrapper([[[[True]]]])._array)  # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.bool]]"

    reveal_type(validate_array([1.0]))         # EXPECTED_TYPE: "builtins.list[builtins.float]"
    reveal_type(validate_array([1]))           # EXPECTED_TYPE: "builtins.list[builtins.int]"
    reveal_type(validate_array([True]))        # EXPECTED_TYPE: "builtins.list[builtins.bool]"
    reveal_type(validate_array([[1.0]]))       # EXPECTED_TYPE: "builtins.list[builtins.list[builtins.float]]"
    reveal_type(validate_array([[1]]))         # EXPECTED_TYPE: "builtins.list[builtins.list[builtins.int]]"
    reveal_type(validate_array([[True]]))      # EXPECTED_TYPE: "builtins.list[builtins.list[builtins.bool]]"
    reveal_type(validate_array([[[1.0]]]))     # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.float]]"
    reveal_type(validate_array([[[1]]]))       # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.int]]"
    reveal_type(validate_array([[[True]]]))    # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.bool]]"
    reveal_type(validate_array([[[[1.0]]]]))   # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.float]]"
    reveal_type(validate_array([[[[1]]]]))     # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.int]]"
    reveal_type(validate_array([[[[True]]]]))  # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.bool]]"

    # tuples
    reveal_type(_ArrayLikeWrapper((1.0,))._array)            # EXPECTED_TYPE: "typing.Sequence[builtins.float]"
    reveal_type(_ArrayLikeWrapper((1,))._array)              # EXPECTED_TYPE: "typing.Sequence[builtins.int]"
    reveal_type(_ArrayLikeWrapper((True,))._array)           # EXPECTED_TYPE: "typing.Sequence[builtins.bool]"
    reveal_type(_ArrayLikeWrapper(((1.0,),))._array)         # EXPECTED_TYPE: "typing.Sequence[typing.Sequence[builtins.float]]"
    reveal_type(_ArrayLikeWrapper(((1,),))._array)           # EXPECTED_TYPE: "typing.Sequence[typing.Sequence[builtins.int]]"
    reveal_type(_ArrayLikeWrapper(((True,),))._array)        # EXPECTED_TYPE: "typing.Sequence[typing.Sequence[builtins.bool]]"
    reveal_type(_ArrayLikeWrapper((((1.0,),),))._array)      # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.float]]"
    reveal_type(_ArrayLikeWrapper((((1,),),))._array)        # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.int]]"
    reveal_type(_ArrayLikeWrapper((((True,),),))._array)     # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.bool]]"
    reveal_type(_ArrayLikeWrapper(((((1.0,),),),))._array)   # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.float]]"
    reveal_type(_ArrayLikeWrapper(((((1,),),),))._array)     # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.int]]"
    reveal_type(_ArrayLikeWrapper(((((True,),),),))._array)  # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.bool]]"

    reveal_type(validate_array((1.0,)))            # EXPECTED_TYPE: "tuple[builtins.float]"
    reveal_type(validate_array((1,)))              # EXPECTED_TYPE: "tuple[builtins.int]"
    reveal_type(validate_array((True,)))           # EXPECTED_TYPE: "tuple[builtins.bool]"
    reveal_type(validate_array(((1.0,),)))         # EXPECTED_TYPE: "tuple[tuple[builtins.float]]"
    reveal_type(validate_array(((1,),)))           # EXPECTED_TYPE: "tuple[tuple[builtins.int]]"
    reveal_type(validate_array(((True,),)))        # EXPECTED_TYPE: "tuple[tuple[builtins.bool]]"
    reveal_type(validate_array((((1.0,),),)))      # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.float]]"
    reveal_type(validate_array((((1,),),)))        # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.int]]"
    reveal_type(validate_array((((True,),),)))     # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.bool]]"
    reveal_type(validate_array(((((1.0,),),),)))   # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.float]]"
    reveal_type(validate_array(((((1,),),),)))     # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.int]]"
    reveal_type(validate_array(((((True,),),),)))  # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.bool]]"


# CASE: Array[T1] -> Array[T2]
if TYPE_CHECKING:
    # scalars
    reveal_type(validate_array(1.0,dtype_out=int))     # EXPECTED_TYPE: "builtins.int"
    reveal_type(validate_array(1,dtype_out=bool))      # EXPECTED_TYPE: "builtins.bool"
    reveal_type(validate_array(True,dtype_out=float))  # EXPECTED_TYPE: "builtins.float"

    # numpy arrays
    reveal_type(validate_array(np.array(1.0),dtype_out=int))     # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.int]]"
    reveal_type(validate_array(np.array(1),dtype_out=bool))      # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.bool]]"
    reveal_type(validate_array(np.array(True),dtype_out=float))  # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.float]]"

    # lists
    reveal_type(validate_array([1.0],dtype_out=int))           # EXPECTED_TYPE: "builtins.list[builtins.int]"
    reveal_type(validate_array([1],dtype_out=bool))            # EXPECTED_TYPE: "builtins.list[builtins.bool]"
    reveal_type(validate_array([True],dtype_out=float))        # EXPECTED_TYPE: "builtins.list[builtins.float]"
    reveal_type(validate_array([[1.0]],dtype_out=int))         # EXPECTED_TYPE: "builtins.list[builtins.list[builtins.int]]"
    reveal_type(validate_array([[1]],dtype_out=bool))          # EXPECTED_TYPE: "builtins.list[builtins.list[builtins.bool]]"
    reveal_type(validate_array([[True]],dtype_out=float))      # EXPECTED_TYPE: "builtins.list[builtins.list[builtins.float]]"
    reveal_type(validate_array([[[1.0]]],dtype_out=int))       # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.int]]"
    reveal_type(validate_array([[[1]]],dtype_out=bool))        # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.bool]]"
    reveal_type(validate_array([[[True]]],dtype_out=float))    # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.float]]"
    reveal_type(validate_array([[[[1.0]]]],dtype_out=int))     # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.int]]"
    reveal_type(validate_array([[[[1]]]],dtype_out=bool))      # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.bool]]"
    reveal_type(validate_array([[[[True]]]],dtype_out=float))  # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.float]]"


    # tuples
    reveal_type(validate_array((1.0,),dtype_out=int))              # EXPECTED_TYPE: "tuple[builtins.int]"
    reveal_type(validate_array((1,),dtype_out=bool))               # EXPECTED_TYPE: "tuple[builtins.bool]"
    reveal_type(validate_array((True,),dtype_out=float))           # EXPECTED_TYPE: "tuple[builtins.float]"
    reveal_type(validate_array(((1.0,),),dtype_out=int))           # EXPECTED_TYPE: "tuple[tuple[builtins.int]]"
    reveal_type(validate_array(((1,),),dtype_out=bool))            # EXPECTED_TYPE: "tuple[tuple[builtins.bool]]"
    reveal_type(validate_array(((True,),),dtype_out=float))        # EXPECTED_TYPE: "tuple[tuple[builtins.float]]"
    reveal_type(validate_array((((1.0,),),),dtype_out=int))        # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.int]]"
    reveal_type(validate_array((((1,),),),dtype_out=bool))         # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.bool]]"
    reveal_type(validate_array((((True,),),),dtype_out=float))     # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.float]]"
    reveal_type(validate_array(((((1.0,),),),),dtype_out=int))     # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.int]]"
    reveal_type(validate_array(((((1,),),),),dtype_out=bool))      # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.bool]]"
    reveal_type(validate_array(((((True,),),),),dtype_out=float))  # EXPECTED_TYPE: "numpy.ndarray[Any, numpy.dtype[builtins.float]]"

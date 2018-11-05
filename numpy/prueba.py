import numpy as np
a = np.arange(15).reshape(3, 5)
a
    array([[ 0,  1,  2,  3,  4],
        [ 5,  6,  7,  8,  9],
        [10, 11, 12, 13, 14]])
a.shape
    (3, 5)
a.ndim
    2
a.dtype.name
    'int64'
a.itemsize
    8
a.size
    15
type(a)
    <type 'numpy.ndarray'>
b = np.array([6, 7, 8])
b
    array([6, 7, 8])
type(b)
    <type 'numpy.ndarray'>

#Creacion de arrays
#array
b = np.array([1,2,3,4])
#Bi-dimensional
b = np.array([(1.5,2,3), (4,5,6)])

#The type of the array can also be explicitly specified at creation time:
c = np.array( [ [1,2], [3,4] ], dtype=complex )

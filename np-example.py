import numpy as np

x = np.array([1.0, 2.0, 3.0])
print(x)
# [1. 2. 3.]
type(x)
# <class 'numpy.ndarray'>

# # # OPERATIONS # # #

x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
x+y
# array([3., 6., 9.])
x*y
# element-wise production
# array([ 2., 8., 18.])
x/y
# array([0.5, 0.5, 0.5])
y/2
# broadcast: broadcast an integer to a numpy array
# array([1., 2., 3.])

# # # N-dimensional matrix # # #

A = np.array([[1, 2], [3, 4]])
B = np.array([[3, 0], [0, 6]])
print(A)
# array([[1, 2],
#        [3, 4]])
print(A.shape)
# (2, 2) : shape of the matrix
print(A.dtype)
# dtype('int32'): type of items in the matrix
A+B
# array([[ 4,  2],
#        [ 3, 10]])
A*B
# array([[ 3,  0],
#        [ 0, 24]])
A*10
# broadcast also available for matrix
# array([[10, 20],
#        [30, 40]])

# # # BROADCAST # # #
C = np.array([10, 20])
A*C
# array([[10, 40],
#        [30, 80]])








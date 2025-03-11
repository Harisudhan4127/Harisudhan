# # import python file use the function
# import calc
# print(calc.add(1,2))

#numpy - Numerical python
''''
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
'''
'''
import numpy as np
arr = np.array([1,2.4,3,4]) # it is not allow the other data types Or Only allow numbers
print(arr) # [1 2 3 4]
print(arr.dtype) # int64
print(type(arr[2])) # <class 'numpy.float64'>
'''

"""
array is fast than list 
Because list heterogenes or multiple data type
list use any mathematics operator  is concortinate
"""
"""
# Dimentions function in NumPy
import numpy as np
arr = np.array([1,2,3,4,5])
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,0])
arr_2d = np.array([[3,4,5],
                   [7,8,9]])
print(arr1 * arr2)
print("Array size : ", arr.size)
print("arrays dimention : ", arr.ndim)
# 2D array
print(arr_2d)
print(arr_2d[1,1])
"""
"""
# Slicing function in NumPy
import numpy as np 
arr = np.array([10,20,30,40,50,60,70,80,90])
print(arr[1:7:2])
print(arr[:7:]) #only end
print(arr[::2]) #only step
print(arr[1::],"\n") #only start
M = np.array([[3,4,5],
              [7,8,9],
              [1,2,6]])
print(M[1:3,1:3]) # [R,C] R-> 1:3 = 1,2 | C-> 1:3 = 1,2
"""
"""
# Data type One data type to another data type
import numpy as np 
arr1 = np.array([1,2.4,3,4,5])
arr2 = np.array([6,7,8,9,0])
arr = arr1 + arr2
# print("Normal :",arr)
print("Using astype :",arr.astype('i')) # float to int
a = np.array([1,0,3])
print(a.astype(bool)) # int to boolean
"""

''''
import numpy as np 
range_arr = np.arange(10,100,10)
print(range_arr)

lin_arr = np.linspace(10,100,10) # Divid equal part 
print(lin_arr)

'''
import numpy as np
ones = np.ones((5,5), dtype = 'i')
zeros = np.zeros((3,3), dtype='i')
ones[1:4,1:4]= zeros
ones[2,2] = 8
print(ones)
print(ones.min())
print(ones.max())
print(ones.sum())
print(ones.std())
print(ones.shape)

import numpy as np

#1

arr=np.array([range(4), range(10,14)])

print np.shape(arr)             #shape of array, ie (2,4)
print np.size(arr)              # size of array (# elements)
print arr.max(), np.max(arr)    #2 different ways of doing the same thing
print arr.min(), np.min(arr)    #finding max/min value of the array

# array is:
#  0  1  2  3  
#  10 11 12 13

#2

print np.reshape(arr, (2,2,2))    #reshapes into the new dimensions
print np.transpose(arr)           #transposes array
print np.ravel(arr)               #unravels array into 1D

b=arr.astype(np.float32)          #changes type of array to floats
print b


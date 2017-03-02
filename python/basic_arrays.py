#playing with numpy arrays

import numpy as np   #MUST DO!!! and run as python 2.7 from now on

#1

x=range(1,11)
a1=np.array(x, dtype=np.int32)     #create array from x (1D) type integers 
a2=np.array(x, dtype=np.float32)   #as above, now type floats

#print a1.dtype, a2.dtype

#2

zero=np.zeros((2,3,4))    #create 0 array with given dimensions
one=np.ones((2,3,4))      #create array containing 1's
sequence=np.arange(1000)  #creates 1D array from 0-999 (could do (0,1000))

#print zero[0,1,3], one[1,2,1], sequence[654]

#3

a=np.array([2, 3.2, 5.5, -6.4, -2.2, 2.4])
print a[1]
print a[1:4]

b=np.array([[2, 3.2, 5.5, -6.4, -2.2, 2.4], [1, 22, 4, 0.1, 5.3, -9], [3, 1, 2.1, 21, 1.1, -2]])
print b[:,3]         #for all rows, the 3rd indexed value (4th element)
print b[1:4, 0:4]    #for rows 2-4, elements 1-4
print b[1: , 2]      #for rows 2 onwards, 3rd element

#this array looks like: 
# 2  3.2  5.5  -6.4  -2.2  2.4
# 1  22    4    0.1   5.3  -9
# 3   1   2.1   21    1.1  -2 



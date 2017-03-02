
import numpy as np

#1

import numpy.ma as MA

a=MA.masked_array(data=range(10), fill_value=-999) #creates array a, no masking
                                                   #yet, but will have a fill 
                                                   #value as given
print a
print a.fill_value

a[2]=MA.masked             #mask 3rd value of a
print a
print a.mask

b=MA.masked_greater(a, 6)  #create b, which is a copy of a, with values <7 
                           #masked
print b
print b.fill_value

c=MA.filled(b)             #fills masked array b with fill value where there
print c                    #were bad values
print type(c)

#2

m1=MA.masked_array(data=range(1,9), fill_value=999) #create masked array
m2=np.reshape(m1, (2,4)) #reshape array

m3=MA.masked_where(m2>6, m2) #mask any values > 6
print m3

print m3*100

ones=np.ones((2,4))  #create array same shape as m3 made up of 1's

print m3-ones        
print type(m3-ones)  #shows it is a masked array still


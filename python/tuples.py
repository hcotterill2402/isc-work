#tuples are like lists but you can't edit elements
#they are created with () rather than []

#1

t=(5,)
print t[-1] #print last element in t

t2=tuple(range(100,201)) #creating tuple from 100-200 - tuple() turns range into tuple
print t2[0], t2[-1]

#2

mylist=[23, "hi", 2.4e-10]
for (i,value) in enumerate(mylist): #prints the index and the value for each element
    print i, value

#3

(first, middle, last)=mylist #reassigning values of mylist
print first, middle, last
(first, middle, last) = (middle, last, first) #reassigning the values
print first, middle, last

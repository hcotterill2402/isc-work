#Lists and Slicing excercises

#1

mylist=[1,2,3,4,5]

print mylist.index(1) #index actually finds the index number 1 is in the list
print mylist[1] # selects the 2nd item in the list
print mylist[-2]
print mylist[0:100] # can also write mylist[:] for entire list
print mylist[1:4]
print len(mylist) #prints the length of the list, 5 in this case

#2

one_to_ten=range(1,11)
print one_to_ten[:]

one_to_ten[0]=10 #change first element to 10
print one_to_ten[:]

one_to_ten.insert(10,11) #insert number 11 as 10th element
print one_to_ten[:]

list2=range(12,15)
one_to_ten.extend(list2) # add the values of list2 to the original list
print one_to_ten[:]

#3

forward=[]
backward=[]
values=["a","b","c"]
for i in values:
    forward.append(i)
    backward.insert(0,i)

forward.reverse()

print forward[:] #could also check these are the same using truth statements
print backward[:] #eg print forward == backward
print forward == backward

#4

countries=["uk","usa","uk","uae"]
#in python shell:
#dir(countries) tells you what things you can do to the list
#help(countries.count) tells you what the count command does and the syntax
print countries.count("uk")


 



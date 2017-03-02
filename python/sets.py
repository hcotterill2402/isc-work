#playing with sets

#1

a={0,1,2,3,4,5} #creating a set
b={2,4,6,8}

print a.union(b) #prints all numbers in both sets (not repeating values)
print a.intersection(b) #prints numbers common to both

#both the above print as a set with the numbers as a list:
#print a.union(b) = set([0,1,2,3,4,5,6,7,8])

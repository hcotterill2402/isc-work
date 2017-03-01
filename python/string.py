#Playing with strings :)

#1

s='I love to write python'
for c in s:
    print c, #, means no new lines
print ' ' #otherwise next line is on same line as above...
print s[4] #5th element - including spaces
print s[-1] #last element
print len(s) #length
print s[0][0]

#2

split_s=s.split() #creates a list, each element is a word of the string
print split_s 

for word in split_s:
    if word.find("p") > -1: #testing truth - will be true if i is in word
        print "I found 'p' in '{0}'" .format(word) #case sensitive!!!
#need {0} since we don't seem to be running 2.7+

#3

something="Completely Different"

print something.count("t") #count how many times t appears
print something.find("plete") #prints first position of "plete"

print something.split("e") #splitting up the string at the letter e
                           #returns ['Compl','t','ly Diff','r','nt]

thing2=something.replace("Different", "Silly")
print thing2 

something[0]='B' #produces error as strings are imutable

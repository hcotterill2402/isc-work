#playing with dictionaries

#2

band=["mel","geri","victoria","mel","emma"]
counts={} #create empty dictionary

for member in band:           #looping over all items in band
    if member not in counts:  #adding to counts, with a certain value
        counts[member]=1
    else:
        counts[member]+=1

for member in counts:             #looping over keys in counts
    print member, counts[member]  #printing the key and the value

#3

if {}: print 'hi' #testing truth of empyt dict. - not true!

d={"maggie":"uk", "ronnie":"usa"}
        
print d.items()   #[('maggie', 'uk'), ('ronnie', 'usa')]
print d.keys()    #['maggie', 'ronnie']
print d.values()  #['uk', 'usa']

print '%s' % d.get('bob','nowhere')    
#if bob doesn't exist as a key, returns 'nowhere'
print '%s' % d.get('maggie','nowhere') 
#returns value since maggie exists as a key

d.setdefault('me','uk')
print d.items()


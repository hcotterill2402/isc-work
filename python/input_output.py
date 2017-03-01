#inputing and outputing files

#1

#read in weather data into variable called data
#with open('weather.csv', 'r') as reader: #opens file to read
#    data=reader.read() #reads into variable
#
#print data

#2

#with open('weather.csv', 'r') as reader: #opens file to read
#    line = reader.readline() #reading in the data one line at a time
#    while line:            # could read in all in one go, but need this to prin#t
#        print line         # each line as you go along
#        line = reader.readline()
#
#print "It's over"

#A few notes and variations!
#with open('weather.csv', 'r') as reader: #opens file to read
#    line = reader.readlines()[:4] #reading only first 4 lines
#    line = reader.readlines() #reads in all lines in one go

#3

with open('weather.csv', 'r') as reader: #opens file to read
#    line = reader.readline() #reading in the data one line at a time    
    rain=[]
    for line in reader.readlines():            
        print line         
        line = reader.readline()




    


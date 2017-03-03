from datetime import datetime
import serial, io

outfile='temp_data.tsv'

ser = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)

#all these fully specified values are standard ones, so could just write:
#ser=serial.Serial(port='/dev/ttyUSB0', baudrate=9600,)

sio=io.TextIOWrapper(io.BufferedRWPair(ser, ser, 1), encoding='ascii', newline='\r')

#This is setting the new line character as something different, so we can
#use readline() to read in the thermometer data

#\t = tab, \n = new line

# no. 8 here is specific to the Papuch thermometer device
#telling it to read in 8 bytes at a time, which is what the thermometer gives
#rather than new lines each time

#1 byte = 1 character

with open(outfile, 'a') as f: #appends to an existing file
    while ser.isOpen():
#    datastring=ser.read(size=8) #could use this, but can use readline() now
        datastring=sio.readline()
        f.write(datetime.utcnow().isoformat() + '\t' + datastring + '\n')
        f.flush() #included to force system to write to disk
#        print datetime.utcnow().isoformat(), datastring

#could put a thing in to close the loop...eg if you only want 10 entries or something...

ser.close()

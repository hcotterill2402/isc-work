#reading data and converting format
#read as .csv file

import csv
import time
from netCDF4 import Dataset
from datetime import datetime, timedelta
from netCDF4 import num2date, date2num
import numpy as np

#with open('temp_data.tsv', 'rb') as f:
#    reader = csv.reader(f, delimiter='\t')
#    for row in reader:
#        print row


#CHANGE ALL OF THIS TO UPDATED CODE ON GITHUB!!!!!!
#grab data from infile
INFILE='../example_data/sample-serial-temperature-2h.tsv'
from csv import reader

variable_metadata = {
    "var_id": "temp",
    "long_name": "Temperature of sensor (K)",
    "units": "K",
    "standard_name": "air_temperature"}

global_metadata = {
    "Conventions": "CF-1.6",
    "institution": "Leeds Uni",
    "title": "My first CF-netCDF file",
    "history": "%s: Written with script: write_sensor_data_to_netcdf.py" % (datetime.now().strftime("%x %X"))}


#now we want to change around the data to make it
def convert_time(tm):
    tm = datetime.strptime(tm, "%Y-%m-%dT%H:%M:%S.%f") #the format of the time
    return tm

def convert_temp(temp):
    value = temp.strip("+").strip("C").lstrip("0")#strips +, C and leading 0 
    return float(value) - 273.15 # converts to K

# Parse the data into python lists
times = []
temps = []

for row in rows:
    tm, temp = row.strip().split()
    times.append(convert_time(tm))
    temps.append(convert_temp(temp))

for row in rows:
    tm, temp = row.strip().split()
    times.append(convert_time(tm))
    temps.append(convert_temp(temp))

# Set reference time and convert datetime values to offset values from reference time
base_time = datetime(2017, 3, 3, 11, 9, 52)
time_values = []

for t in times:
    value = t - base_time
    ts = value.total_seconds()
    time_values.append(ts)

time_units = "seconds since 2017-03-03 11:09:52"

# Create the output file (NetCDF dataset)
output_file = "sensor_data.nc"
dataset = Dataset(output_file, "w", format='NETCDF4_CLASSIC')

# Create the time dimension - with unlimited length
time_dim = dataset.createDimension("time", None)

# Create the time variable
time_var = dataset.createVariable("time", np.float64, ("time",))
time_var[:] = time_values
time_var.units = time_units
time_var.standard_name = "time"
time_var.calendar = "standard"

# Create the temp variable
temp = dataset.createVariable("temp", np.float32, ("time",))
temp[:] = temps

# Set the variable attributes
for (attr, value) in variable_metadata.items():
    setattr(temp, attr, value)

# Set the global attributes
for (attr, value) in global_metadata.items():
    setattr(dataset, attr, value)

# Write the file
dataset.close()

print "Wrote: %s" % output_file
print "Try: ncdump %s" % output_file



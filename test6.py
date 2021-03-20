import numpy as nm
import pandas as pd
import matplotlib.pyplot as plt
#Load data
stationData = pd.read_csv('suttonboningtondata_moodle.csv',skiprows=3)
print("############################################################################")
print("Total number of items (rows x columns) are  : " + str(stationData.shape))
tmin= stationData["tmin"]
del(tmin[0])
min=min(tmin,key=lambda x:float(x)) 
print("The min value of minimum temperature is     : " + str(min)) 
##The Sun column is currently in hours. Recalculate this column so the values are in days (assume a day is 24 hours).
#Re-save this file as a new filename– you may want to use numpy.savetxt, but you don’t have to.*
del((stationData["sun"][0]))
stationData["sun"]=stationData["sun"].map(lambda sun: float(sun)/24.0)
outputfile="output.csv"
print("Sun column in days &saving to file          : " + outputfile) 
nm.savetxt(outputfile, stationData.values, fmt='%s', delimiter=',',header=" yyyy,  mm,  tmax, tmin, af, rain, sun")
print("############################################################################")
#Plot max temperatures of 2017
print("Max temperatures of year 2017") 
counter=1
plt.figure()  
for index in stationData.values:
    if index[0]==2017.0:        
       print (index[0], index[2])
       plt.scatter(counter,float(index[2]),lw=2, linestyle='--', color='red')
       counter+=1
plt.xlabel('Measurement sequence')
plt.ylabel('TMAX')
plt.title('Maximum Temperatures in 2017')
plt.show()
print("############################################################################")


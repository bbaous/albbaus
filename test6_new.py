from typing import List
import numpy as nm
import pandas as pd
import matplotlib.pyplot as plt
#Load data (and skip the first 3 rows i.e the header)
stationData = pd.read_csv('suttonboningtondata_moodle.csv',skiprows=3)
print("############################################################################")
print("Total number of items (rows x columns) are  : " + str(stationData.shape))
#Find the min of the tmin comumn
tmin= stationData["tmin"]
del(tmin[0])
min=min(tmin,key=lambda x:float(x)) 
print("The min value of minimum temperature is     : " + str(min)) 
#Convert Sun column in days and saved in the output file
del((stationData["sun"][0]))
stationData["sun"]=stationData["sun"].map(lambda sun: float(sun)/24.0)
outputfile="output.csv"
print("Sun column in days &saving to file          : " + outputfile) 
nm.savetxt(outputfile, stationData.values, fmt='%s', delimiter=',',header=" yyyy,  mm,  tmax, tmin, af, rain, sun")
print("############################################################################")
#Plot max temperatures of 2017
print("Max temperatures of year 2017") 
#Create the plot 
list=[]
counterList=[]
#plt.figure()  
for index in stationData.values:
    if index[0]==2017.0:        
       print (index[0], index[2])
       list.append( index[2])
       counterList.append(index[1])
plt.plot(counterList,list, color='blue',  marker='o')
plt.xlabel('Measurement sequence')
plt.ylabel('TMAX')
plt.title('Maximum Temperatures in 2017') 
plt.grid(True)
plt.show()
print("############################################################################")

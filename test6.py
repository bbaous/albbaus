import numpy as nm
import pandas as pd
import matplotlib.pyplot as plt

stationData = pd.read_csv('suttonboningtondata_moodle.csv',skiprows=3)
stationData.shape.index
print("Total number of items (rows x columns) are  : " + str(stationData.shape))
tmin= stationData["tmin"]
del(tmin[0])
min=min(tmin,key=lambda x:float(x)) 
print("The min value of minimum temperature is     : " + str(min)) 
sun=stationData["sun"]

year= stationData["yyyy"]
del(year[0])
tmax=stationData["tmax"]
del(tmax[0])
yearMax=()
print("Max temperatures of year 2017") 
for index in stationData.values:
    if index[0]==2017.0:
       yearMax=(index[0], index[2])
       print (index[0], index[2])


plt.figure()  
plt.plot(yearMax, color='red', lw=2, label='Tmax')
    

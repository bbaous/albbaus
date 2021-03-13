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
#TODO -This the only part missing
##The Sun column is currently in hours. Recalculate this column so the values are in days (assume a day is 24 hours).
#Re-save this file as a new filename– you may want to use numpy.savetxt, but you don’t have to.*
print(stationData["sun"])
##Change date 


#Plot max temperatures of 2017
print("Max temperatures of year 2017") 
counter=1
plt.figure()  
for index in stationData.values:
    if index[0]==2017.0:
       print (index[0], index[2])
       plt.scatter(counter,float(index[2]),lw=2, linestyle='--', color='red')
       counter+=1
plt.xlabel('T')
plt.ylabel('TMAX')
plt.title('Maximum Temperatures in 2017')
plt.show()

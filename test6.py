import numpy as nm
import pandas as pd
from pandas.core.indexes.range import RangeIndex
from datetime import datetime
from time import time

#stationData = nm.loadtxt('./suttonboningtondata_moodle-org.csv',comments='#',delimiter=",", skiprows=3)
#stationData.shape
stationData = pd.read_csv('suttonboningtondata_moodle.csv',skiprows=3)
stationData.shape
print(stationData.shape)
tmin= stationData["tmin"]

#print(tmin[:10]) 

print(tmin.min())
#rain = stationData["rain"]
#year= stationData["yyyy"]
#mm=stationData["mm"]
#sun=stationData["tmin"]



#stationData["sun"]= pd.to_datetime(stationData["sun"], format='%Y%m%d')  
  
# printing dataframe  
#print(stationData["sun"]) 

#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import math

peakLoad = 59.662 # kW
baseLoad = 6.3 # kW
peakLoad = peakLoad-baseLoad
peakPeriod = 20 # Earth Hours
basePeriod = 4 # Earth Hours
specEnergy = .02 # kW/kg 
DoD = .6 #Depth of Discharge, %/100

#applies 20% margin
peakLoad = peakLoad*1.2
baseLoad = baseLoad*1.2

#initializes values
numKRUSTY = 0
batteries = True

#determines minimun number of KRUSTYs needed
n = 1
while True:
    pEff = n*10-baseLoad
    energyReq = (peakLoad-pEff)*peakPeriod
    if peakLoad-pEff <= 0:
        numKRUSTY = n
        batteries = False
        break
    elif n*10*basePeriod >= energyReq:
        numKRUSTY = n
        break
    else:
        n+=1

print("For a maximum load of:", math.ceil(peakLoad), "kW", "Running for:", peakPeriod, "Earth Hours")

#determines total system mass
if batteries == True:
    batteryMass = ((peakLoad-(numKRUSTY*10-baseLoad))/DoD)/specEnergy
    totalMass = 2105+1863*(numKRUSTY-1)+batteryMass
    totalMassKRUSTY = (math.ceil(peakLoad/10))*1863+2105
    if totalMass/totalMassKRUSTY >= 1.1: #rejects the battery system if efficiency is below threshold
        print("Batteries present", "Number of KRUSTYs:", numKRUSTY, "Total System Mass:", totalMass, 
              "Battery Mass:", batteryMass)
    else:
        #print(batteryMass)
        #print(totalMass)
        oldMass = totalMass
        totalMass = 2105+1863*(numKRUSTY)
        dif = totalMass-oldMass
        totalVolume = 5.3*(numKRUSTY+1)
        print("No batteries", "Number of KRUSTYs:", numKRUSTY+1, 
              "Total System Mass:", totalMass, "kg", "Total Volume:", totalVolume, "m^3")
        #print(dif)
        
else:
    totalMass = 2105+1863*(numKRUSTY-1)
    print("No batteries", "Number of KRUSTYs:", numKRUSTY, "Total System Mass:", totalMass, "kg")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





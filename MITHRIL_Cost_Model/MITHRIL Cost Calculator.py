#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

print("This script calculates the price for the MITHRIL ISRU.",
      "The calculator will ask for several inputs corrosponding to cost assumptions, e.g. the cost of the launch system.",
     "Type in 'low' for the low estimate, 'high' for the more expensive one, or 'mean' for the average.",
     "The calculator will automatically return the total cost, inflation is taken into account.")

#initializes cost catagories
operations_pro = np.zeros(20)
operations_total = 0

services_pro = np.zeros(20)
services_total = 0

design_pro = np.zeros(20)
design_total = 0

fabrication_pro = np.zeros(20)
fabrication_total = 0

total_cost = 0

#fixed price values
STARSHIP_LAUNCH_COST = 11*10**6 #10 launches multiplied by the quotes price of $1,000,000
SLS_LAUNCH_COST = 4.1*10**9 #1 launch at the IG price of $4.1 Billion

DRILL_PRICE = 663000

OP_COST_BASELINE = 1.5*10**8

AMOUNT_METHANE = 11086 #kg
AMOUNT_LOX = 39130 #kg

STORAGE_TANK_SIZE = 34 #m^3

ATHLETE_PRICE = 3*10**9 #based on the price of the Perserverance Rover

DSN_HOURS = 450
DSN_BASE_RATE = 1792 #The Rb quoted price from the DSN Mission Support Definition and Commitments Office.
TTC_COST = 300000
NETWORK_ACCESS_FEE = 2700*12
MIM_COST = 290000
RF_TEST_COST = 120000

mars_factor = (80000000/28000)

#determines price of communications
services_pro[10]+=MIM_COST+RF_TEST_COST+NETWORK_ACCESS_FEE
services_pro[11]+=NETWORK_ACCESS_FEE+TTC_COST
for i in range(12,20): #determines the total yearly cost for DSN usaged based on a 2% inflation rate
    af = DSN_BASE_RATE*(.9+10/10)
    yearly_cost = DSN_HOURS*af+NETWORK_ACCESS_FEE
    services_pro[i]+=yearly_cost

#determines the cost to develope software
CS_LABOR_COST = 110140 + 100000 #average salary from BLS + a bunch for other costs
NUM_CS_WORKERS = 30 #number of engineers on the task
total_software_cost = CS_LABOR_COST*NUM_CS_WORKERS*5
total_software_cost_pro = total_software_cost/8
for i in range(8):
    design_pro[i]+=total_software_cost_pro
    
#determines the cost for operations
op_cost_modifier = 1.8
for i in range(12,20):
    operations_pro[i] = OP_COST_BASELINE*op_cost_modifier
    op_cost_modifier = op_cost_modifier-.1

#determines the launch costs
launch_cost = 0
launch_vehicle = input('SLS is estimated to cost $4.1 Billion while Starship is presumed to cost $10 Million.')
launch_vehicle = launch_vehicle.upper()
if launch_vehicle == "LOW":
    launch_cost = STARSHIP_LAUNCH_COST
    print("Using the LOW estimate.")
elif launch_vehicle ==  "HIGH":
    launch_cost = SLS_LAUNCH_COST
    print("Using the HIGH estimate.")
else:
    launch_cost = (STARSHIP_LAUNCH_COST+SLS_LAUNCH_COST)/2
    print("Using the MEAN cost.")


resupply_choice = input('Accept Resupply Missions? (add extra launches, reply yes or no)')
resupply_choice = resupply_choice.upper()
if resupply_choice == 'YES':
    num_launches_choice = input('How many additional launches?')
    num_launches = int(num_launches_choice)
    launch_cost += launch_cost*num_launches
    print("Sending ", num_launches, "resupply missions.")
else:
    print("No resupply missions.")
launch_cost_pro = launch_cost/3
services_total+=launch_cost
for i in range(9,12):
    services_pro[i]+=launch_cost_pro 

#determines cost of KRUSTY
krusty_price = 5500*10
krusty_total_cost = 0
krusty_choice =  input('The estimated range for power is between $880 Million and $1.3 Billion.')
krusty_choice = krusty_choice.upper()
if krusty_choice == "HIGH":
    krusty_total_cost =  7*krusty_price*mars_factor*1.2
    print("Using the HIGH estimate.")
elif krusty_choice ==  "LOW":
    krusty_total_cost =  7*krusty_price*mars_factor*.8
    print("Using the LOW estimate.")
else:
    krusty_total_cost = 7*krusty_price*mars_factor
    print("Using the MEAN cost.")
krusty_total_cost_fab = krusty_total_cost*.75
krusty_total_cost_design = krusty_total_cost*.25
krusty_total_cost_fab_pro = krusty_total_cost_fab/8
krusty_total_cost_design_pro = krusty_total_cost_design/6
for i in range(8):
    design_pro[i]+=krusty_total_cost_design_pro
for i in range (6,12):
    fabrication_pro[i] += krusty_total_cost_fab_pro

#determines SABER cost
price_per_barrel_oil = 25000
price_per_gallon_oil = price_per_barrel_oil/42
price_per_kg_oil = price_per_gallon_oil*3.45
price_per_kg_methalox = price_per_kg_oil*(1.55/.82)
saber_price_base = price_per_kg_methalox*(AMOUNT_METHANE+AMOUNT_LOX)/300*mars_factor
saber_price_low = .8*saber_price_base
saber_price_high = 1.2*saber_price_base

saber_cost = 0
saber_choice = input('The price points for SABER are between $1.5 and $2.3 Billion.')
saber_choice = saber_choice.upper()
if saber_choice == "HIGH":
    saber_cost_design = saber_price_high*(1057/1656)
    saber_cost_fab = saber_price_high*(619/1656)
    print("Using the HIGH estimate.")
elif saber_choice ==  "LOW":
    saber_cost_design = saber_price_low*(1057/1656)
    saber_cost_fab = saber_price_low*(619/1656)
    print("Using the LOW estimate.")
else:
    saber_cost_design = (saber_price_high+saber_price_low)/2*(1037/1656)
    saber_cost_fab = (saber_price_high+saber_price_low)/2*(619/1656)
    print("Using the MEAN cost.")
saber_cost_design_pro = saber_cost_design/8
saber_cost_fab_pro = saber_cost_fab/6
for i in range(8):
    design_pro[i]+=saber_cost_design_pro
for i in range(6,12):
    fabrication_pro[i]+=saber_cost_fab_pro

#determines storage cost
storage_tank_gallons = 2*STORAGE_TANK_SIZE*8981.85
tank_cost_per_gallon = 1380000/835958
storage_cost = storage_tank_gallons*tank_cost_per_gallon*mars_factor
storage_choice =  input('The costs for storage are $2.3 and $3.5 Billion respectivaly.')
storage_choice = storage_choice.upper()
if storage_choice == "HIGH":
    storage_cost_design = storage_cost*(1057/1656)*1.2
    storage_cost_fab = storage_cost*(619/1656)*1.2
    print("Using the HIGH estimate.")
elif storage_choice ==  "LOW":
    storage_cost_design = storage_cost*(1037/1656)*.8
    storage_cost_fab = storage_cost*(619/1656)*.8
    print("Using the LOW estimate.")
else:
    storage_cost_design = storage_cost*(1037/1656)
    storage_cost_fab = storage_cost*(619/1656)
    print("Using the MEAN cost.")
storage_cost_design_pro = storage_cost_design/8
storage_cost_fab_pro = storage_cost_fab/6
for i in range(8):
    design_pro[i]+=storage_cost_design_pro
for i in range(6,12):
    fabrication_pro[i]+=storage_cost_fab_pro

#determines STING cost
sting_cost = DRILL_PRICE*mars_factor
sting_choice = input('STING is estimated to cost between $1.5 and $2.3 Billion.')
sting_choice = sting_choice.upper()
if sting_choice == "HIGH":
    sting_cost_design = sting_cost*(1105/1739)*1.2
    sting_cost_fab = sting_cost*(634/1739)*1.2
    print("Using the HIGH estimate.")
elif sting_choice ==  "LOW":
    sting_cost_design = sting_cost*(1105/1739)*.8
    sting_cost_fab = sting_cost*(634/1739)*.8
    print("Using the LOW estimate.")
else:
    sting_cost_design = sting_cost*(1105/1739)
    sting_cost_fab = sting_cost*(634/1739)
    print("Using the MEAN cost.")
sting_cost_design_pro = sting_cost_design/8
sting_cost_fab_pro = sting_cost_fab/6
for i in range(8):
    design_pro[i]+=sting_cost_design_pro
for i in range(6,12):
    fabrication_pro[i]+=sting_cost_fab_pro    
    
#determines ATHLETE cost
athlete_cost_design = ATHLETE_PRICE*.5
athlete_cost_fab = ATHLETE_PRICE*.5
athlete_cost_design_pro = athlete_cost_design/8
athlete_cost_fab_pro = athlete_cost_fab/6
for i in range(8):
    design_pro[i]+= athlete_cost_design_pro
for i in range(6,12):
    fabrication_pro[i]+=athlete_cost_fab_pro
    
#applies a 2% inflation factor
for i in range(20):
    inf_factor = 1.02**i
    design_pro[i] = design_pro[i]*inf_factor
    fabrication_pro[i] = fabrication_pro[i]*inf_factor
    services_pro[i] = services_pro[i]*inf_factor
    operations_pro[i] = operations_pro[i]*inf_factor

#determines total cost in each category
operations_total = sum(operations_pro)
services_total = sum(services_pro)
design_total = sum(design_pro)
fabrication_total = sum(fabrication_pro)
total_cost = operations_total+services_total+design_total+fabrication_total
total_cost_pro = design_pro+fabrication_pro+services_pro+operations_pro



print("The total calculated cost for MITHRIL is: ", "$","{:,}".format(np.round(total_cost)))


# 

# 

# 

# In[ ]:





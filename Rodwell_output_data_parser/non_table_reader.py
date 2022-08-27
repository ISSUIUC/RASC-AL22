# NON TABLE DATA
import numpy as np 
import pandas as pd 
import numpy.linalg as la 
import matplotlib.pyplot as plt
from io import StringIO
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

# Helper Functions 
def minusparse(line):
    newline = ""
    for i in range(len(line)):
        if(line[i] == '-'):
            newline += " " + line[i]
        else:
            newline += line[i]
    return newline

def equalparse(line):
    temp = [x.strip().replace('\t','') for x in line.split("=")]
    temp[-1] = temp[-1][:-1]
    return temp 
# END HELPER FUNCTIONS

# Open file 
cnt = 0 
f = open("output.txt", "r")
data = ""
features = [str(i) for i in range(0, 14)]

# Get non-tables 
for _ in range(22):
    prevline1 = ""
    prevline2 = ""
    line = f.readline()
    
    # get position
    if(len(line.split()) == 0):
        line = 'NONE'
    while(line.split()[0] != "TOTAL"):
        prevline2 = prevline1
        prevline1 = line
        line = f.readline()
        if(len(line.split()) == 0):
            line = 'NONE'
   
    # get hours 
    prevline2 = minusparse(prevline2)
    hours = [x for x in prevline2.split(",") if x != ''][0]
    
    # get non-table 
    newline = minusparse(line)
    newline = equalparse(newline)
    data += str(hours)
    while newline[0] != '':
        # add to data 
        data += "," + newline[1]

        # update 
        newline = minusparse(f.readline())
        newline = equalparse(newline)
        
    cnt += 1
    data += '\n'

# Convert to pandas object 
TESTDATA = StringIO(data)
df = pd.read_csv(TESTDATA, header=None)
df.columns = features

# DF mapping 
'''
  0 - hours 
  1 - TOTAL ENERGY INPUT BTU 
  2 - SEASONAL ENERGY INPUT BTU 
  3 - SEASONAL ENERGY INPUT GAL FUEL 
  4 - SEASONAL ENERGY RATE BTU/HR
  5 - TOTAL ENERGY INPUT GAL FUEL 
  6 - AVERAGE LB. WATER PER LB. FUEL
  7 - SEASONAL LB. WATER PER LB. FUEL
  8 - ENERGY FROM AIR TO ICE BTU
  9 - SEASONAL ENERGY LOSS, AIR TO ICE BTU 
  10 - TOTAL WATER WITHDRAWN GAL
  11 - SEASONAL WATER WITHDRAWN GAL 
  12 - TOTAL WATER LOSS GAL
  13 - SEASONAL WATER LOSS GAL
'''

# Graph data for each column vs hours 
for name in features: 
    plt.scatter(df["0"], df[name])
    plt.xlabel("hours")
    plt.ylabel(name)
    plt.title(name + " vs. hours")
    plt.show()


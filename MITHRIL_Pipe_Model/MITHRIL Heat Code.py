# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 17:34:44 2022

@author: Grant Davis and the University of Illinois RASCAL Team
Krusty Heat Loss Code
Thermo Bible - Heat Transfer: A practical approach, first edition by Yunus Cengel
Page 417 has a worked example of a pipe.
Assumptions list
Steady operating conditions
- cold winter night on mars
- air is an ideal gas
- local atmospheric pressure is as stated
- Using cold measures of mars from Alec's website' - assuming behavior around 60N latitude
- specific heat of mars air is a big assumption - Used gas mix from https://ntrs.nasa.gov/api/citations/19700003481/downloads/19700003481.pdf
Excess heat entering the rodwell will create extra melted water- will make rodwell wider, but will not have a significant performance impact
"""
import math
TMars = 222 #In Kelvin, equal to -60 Fahrenheit, check with mining to insure this stays constant
e = math.e
pi = math.pi

#inputs
pipeLengthSurface = 10 #change this at will
pipeLengthSting = 60 #change this at will; represents maximum heat loss in Sting
tempKrustyWater = 305 #in kelvin, ~32 Celcius, this variable should be changed at will as long as it is feasible for transfer from KRUSTY (Beneath 50C)
massflowrate = .0832 #kg/s, from mining
thermAtKrusty = massflowrate * 191.83 # kW, from Fundamentals of Engineering Thermodynamics
#Step 1; pipe from krusty to sting
#properties of mars
tempMars = 150 #In kelvin, from Mars Climate Database with coldest temperature; 
tempRodwell = 211 # converted from fahrenheit in rodwell code
tempSky = 100 # In kelvin, from Preliminary Thermal Surface Design of the Mars 2020 Rover
pressureMars = 0.00750062 #atm, or .760 kPa from Mars Climate Database, near 45 lat
gMars = 3.721 #m/s
rhoMars = 2.4 * 10**(-3) #From Mars Climate Database, corresponds to atmosphere
cpMars = 37.35 # J/mol K, assuming same as specific heat of CO2 as a gas
heatTransferGround = 697.333 * 10*(-4) # from Note on thermal properties of Mars, converted into watts per meter squared
kMarsAir = .01 #From the effect of bulk density and particle size sorting on the thermal conductivity of particulate materials under Martian atmospheric pressures
densityWater = 3.7854 #kilograms per gallon
pressureRodwell = .5 #atm
rhoRodwell = (pressureRodwell/pressureMars) * rhoMars

#calculating Rayleigh number for convection
x = 1/39.37 #meters, characteristic length/outer diameter of pipe
#gMars is already defined
beta = 1/tempMars #thermal expansion coefficient, ideal gas assumption
tempDif = tempKrustyWater - tempMars
#calculating rayleigh number to understand heat loss in pipe
grashof = gMars * beta * (tempDif)*x**3
prandtl = .7 #from Transport Properties at High Temperatures
rayleigh = grashof * prandtl
#from Heat Transfer
nusselt = (0.6 + (.387*rayleigh**(1/6))/(1+(0.559/prandtl)**(9/16))**(8/27))**2
h1 = kMarsAir / x * nusselt
A1 = pi * x * pipeLengthSurface
QConv1 = h1*A1*tempDif
print("The heat lost from convection in the outer stretch of pipe per second is")
print(QConv1)

#Calculating heat lost from radiation
stefanBoltzmann = 5.67 * 10**(-8)
epsilonTitanium = .5 #https://www.omega.co.uk/literature/transactions/volume1/emissivitya.html, rough estimate for a titanium alloy
QRad1 = epsilonTitanium * A1 * stefanBoltzmann * (tempKrustyWater**4 - tempSky**4)
print("The heat lost from radiation in the outer stretch of pipe per second is")
print(QRad1)
#this number is the largest of heat losses, it could be reduced further by adding an aerogel or other material with low emissivity to the outer shell.

tempStingWater = tempKrustyWater - 2 # this requires manual adjustment based on above values with a chart of water heat. This is roughly the amount of thermal energy lost (Engineering Thermodynamics) and the corresponding temperature

#Heat Transfer in upper part of sting in worst case scenario
#calculating new Rayleigh
x = 1/39.37 #meters, characteristic length/outer diameter of pipe
#gMars is already defined
beta = 1/tempRodwell #thermal expansion coefficient, ideal gas assumption
tempDif = tempStingWater - tempRodwell
#calculating rayleigh number to understand heat loss in pipe
grashof = gMars * beta * (tempDif)*x**3
prandtl = .65 #from Transport Properties at High Temperatures
rayleigh = grashof * prandtl
#from thermo book
nusselt = (0.6 + (.387*rayleigh**(1/6))/(1+(0.559/prandtl)**(9/16))**(8/27))**2
h1 = kMarsAir / x * nusselt
A2 = pi * x * pipeLengthSting
QConv2 = h1*A2*tempDif
print("The heat lost from convection inside of Sting pipe at full extension per second is")
print(QConv2)

#Calculating heat lost from radiation in Sting
stefanBoltzmann = 5.67 * 10**(-8)
epsilonTitanium = .5 #https://www.omega.co.uk/literature/transactions/volume1/emissivitya.html, rough estimate for a titanium alloy
QRad2 = epsilonTitanium * A2 * stefanBoltzmann * (tempKrustyWater**4 - tempRodwell**4)
print("The heat lost from radiation in the Sting pipe per second is")
print(QRad2)
print("Total heat lost in worst case, watts")
print(QConv1 + QConv2 + QRad1 + QRad2)
#This analysis predicts a maximum of 1132 watts of heat loss, which is 15% of the heat needed to power the rodwell, but only 3.77% of the total energy used by KRUSTY.
#Additionally, over 82% of this heat loss is in the Rodwell, where a fraction of it will be used to expand the rodwell.
#The final consideration is the effects of adding a water storage tank associated with KRUSTY, and any conduction that might occur between the pipes and the ground of Mars.
"""
Works Cited
Çengel, Y., 2006. Heat transfer. 2nd ed. New York: McGraw-Hill Higher Education.
MORAN, M., 2020. FUNDAMENTALS OF ENGINEERING THERMODYNAMICS. [S.l.]: WILEY.
Percy, J. and Bobbitt, L., 1969. TRANSPORT PROPERTIES AT HIGH TEMPERATURES OF C0,-N,-0,-Ar GAS MIXTURES FOR PLANETARY ENTRY APPLICATIONS. [online] Available at: <https://ntrs.nasa.gov/api/citations/19700003481/downloads/19700003481.pdf>.
Leovy, C., 1965. NOTE ON THERMAL PROPERTIES OF MARS. [online] Available at: <https://ntrs.nasa.gov/api/citations/19650016474/downloads/19650016474.pdf>.
Novak, K., Kampenaar, J., Redmond, M. and Bhandari, P., 2015. Preliminary Surface Thermal Design of the Mars 2020 Rover. [online] Available at: <https://ttu-ir.tdl.org/bitstream/handle/2346/64407/ICES_2015_submission_134.pdf>.
Millour, E., “The Mars Climate Database (MCD version 5.3)”, p. 12247, 2017.
Presley, M. A., and P. R. Christensen (1997), The effect of bulk density and particle size sorting on the thermal conductivity of particulate materials under Martian atmospheric pressures, J. Geophys. Res., 102(E4), 9221–9229.
"""
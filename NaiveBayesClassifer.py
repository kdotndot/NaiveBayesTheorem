import numpy as np

f = open("testing.txt", "r")


loc = {}
mintemp =[]
maxtemp =[]
rainfall =[]
evap =[] 
sunshine =[]
windgusdir = {}
windgusspeed =[]
winddir9am = {}
winddir3pm = {}
windspeed9am =[]
windspeed3pm =[]
hum9am =[]
hum3pm =[]
press9am =[]
press3pm =[]
cloud9am =[]
cloud3pm =[]
temp9am =[]
temp3pm =[]
raintoday =[]

f = open("testing.txt", "r")

def addCategorical(dict, val):
    #Checking if val exists
    if val in dict:
        dict[val] += 1
    #Value doesn't exist
    else:
        dict[val] = 1


Lines = f.readlines()

for line in Lines:
    x = line.split(", ")
    addCategorical(loc,x[0])
    mintemp.append(x[1])
    maxtemp.append(x[2])
    rainfall.append(x[3])
    evap.append(x[4])
    sunshine.append(x[5])
    addCategorical(windgusdir,x[6])
    windgusspeed.append(x[7])
    addCategorical(winddir9am,x[8])
    addCategorical(winddir3pm,x[9])
    windspeed9am.append(x[10])
    windspeed3pm.append(x[11])
    hum9am.append(x[12])
    hum3pm.append(x[13])
    press9am.append(x[14])
    press3pm.append(x[15])
    cloud9am.append(x[16])
    cloud3pm.append(x[17])
    temp9am.append(x[18])
    temp3pm.append(x[19])
    rainfall.append(x[20])

print(winddir9am)
    
    




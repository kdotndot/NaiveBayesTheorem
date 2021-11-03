import numpy as np
import statistics as stat

f = open("testing.txt", "r")



numericalDict = {
    "mintemp" : 1,
    "maxtemp" : 2,
    "rainfail" : 3,
    "evap" : 4,
    "sunshine" : 5,
    "windgusspeed" : 7,
    "windspeed9am" : 10,
    "windspeed3pm" : 11,
    "hum9am" : 12,
    "hum3pm" : 13,
    "press9am" : 14,
    "press3pm" : 15,
    "cloud9am" : 16,
    "cloud3pm" : 17,
    "temp9am" : 18,
    "temp3pm" : 19,
}


featuresMean = {
    "mintemp" : 0,
    "maxtemp" : 0,
    "rainfail" : 0,
    "evap" : 0,
    "sunshine" : 0,
    "windgusspeed" : 0,
    "windspeed9am" : 0,
    "windspeed3pm" : 0,
    "hum9am" : 0,
    "hum3pm" : 0,
    "press9am" : 0,
    "press3pm" : 0,
    "cloud9am" : 0,
    "cloud3pm" : 0,
    "temp9am" : 0,
    "temp3pm" : 0,
}


loc = {}
mintemp = [0,0]
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
raintoday ={}

f = open("testing.txt", "r")

def addCategorical(dict, val, label):
    #Checking if val exists
    
    if val in dict:
        if label == 'Yes\n':
            dict[val][0] += 1
        else:
            dict[val][1] += 1
    #Value doesn't exist
    else:
        if label == 'Yes\n':
            dict[val] = [1,0]
        else:
            dict[val] = [0,1]

def numericalSplit(list, label):
    if label == 'Yes\n':
        list[0] += 1
    else:
        list[1] += 1


def GiniFinder(labels):
        tot = 0
        gini = 1
        for i in range(0,len(labels)):
            tot += labels[i]
        if tot == 0:
            return 1
        for i in range(0,len(labels)):
            gini -= (labels[i]/tot)**2
        return gini


Lines = f.readlines()

for line in Lines:
    x = line.split(", ")
    
    addCategorical(loc,x[0], x[21])
    #numericalSplit(mintemp,x[21])
    mintemp.append(float(x[1]))
    maxtemp.append(float(x[2]))
    rainfall.append(float(x[3]))
    evap.append(float(x[4]))
    sunshine.append(float(x[5]))
    addCategorical(windgusdir, x[6], x[21])
    windgusspeed.append(float(x[7]))
    addCategorical(winddir9am, x[8], x[21])
    addCategorical(winddir3pm, x[9], x[21])
    windspeed9am.append(float(x[10]))
    windspeed3pm.append(float(x[11]))
    hum9am.append(float(x[12]))
    hum3pm.append(float(x[13]))
    press9am.append(float(x[14]))
    press3pm.append(float(x[15]))
    cloud9am.append(float(x[16]))
    cloud3pm.append(float(x[17]))
    temp9am.append(float(x[18]))
    temp3pm.append(float(x[19]))
    addCategorical(raintoday,x[20],x[21])



    




import numpy as np
import statistics as stat

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

def addCategorical(dict, val, label):
    #Checking if val exists
    
    if val in dict:
        if label == 'Yes\n':
            dict[val][0] += 1
        else:
            dict[val][1] += 1
    #Value doesn't exist
    else:
        dict[val] = [0,0]

def numericalSplit(list):
    mean = stat.mean(list)
    stddev = stat.stdev(list)
    print(mean)
    print(stddev)


Lines = f.readlines()

for line in Lines:
    x = line.split(", ")
    
    addCategorical(loc,x[0], x[21])
    
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
    rainfall.append(float(x[20]))

print(numericalSplit(mintemp))
    
    




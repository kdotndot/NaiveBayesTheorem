import numpy as np
import statistics as stat

f = open("testing.txt", "r")



numDict = {
    "loc" : 0,
    "mintemp" : 1,
    "maxtemp" : 2,
    "rainfall" : 3,
    "evap" : 4,
    "sunshine" : 5,
    "windgusdir" : 6,
    "windgusspeed" : 7,
    "winddir9am" : 8,
    "winddir3pm" : 9,
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
    "raintoday" : 20
}

featuresHold = {
    "loc" : {},
    "mintemp" : [],
    "maxtemp" : [],
    "rainfall" : [],
    "evap" : [],
    "sunshine" : [],
    "windgusdir" : {},
    "windgusspeed" : [],
    "winddir9am" : {},
    "winddir3pm" : {},
    "windspeed9am" : [],
    "windspeed3pm" : [],
    "hum9am" : [],
    "hum3pm" : [],
    "press9am" : [],
    "press3pm" : [],
    "cloud9am" : [],
    "cloud3pm" : [],
    "temp9am" : [],
    "temp3pm" : [],
    "raintoday" : {}
}

featuresMean = {
    "mintemp" : 0,
    "maxtemp" : 0,
    "rainfall" : 0,
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


f = open("training.txt", "r")

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
    a = line.split(", ")
    
    for x in numDict:
        if x == "loc":
            addCategorical(featuresHold[x], a[0], a[21])
        elif x == "windgusdir":
            addCategorical(featuresHold[x], a[6], a[21])
        elif x == "winddir9am":
            addCategorical(featuresHold[x], a[8], a[21])
        elif x == "winddir3pm":
            addCategorical(featuresHold[x], a[9], a[21])
        elif x == "raintoday":
            addCategorical(featuresHold[x], a[20], a[21]) 
        else:
            featuresHold[x].append(float(a[numDict[x]]))

for x in featuresHold:

    if x != "loc" and x != "windgusdir" and x != "winddir9am" and x != "winddir3pm" and x != "raintoday":
        featuresMean[x] = (stat.mean(featuresHold[x]))
        featuresHold[x] = [[0,0], [0,0]]


#Rereads file
f.close()
f = open("training.txt", "r")
Lines = f.readlines()

for line in Lines:
    a = line.split(", ")
    for x in featuresMean:

        if float(a[numDict[x]]) <= (featuresMean[x]):
            
            numericalSplit(featuresHold[x][0], a[21])
        else:
            
            numericalSplit(featuresHold[x][1], a[21])
        
for x in featuresMean:
    print(featuresHold[x])





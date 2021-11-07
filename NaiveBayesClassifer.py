import numpy as np
import statistics as stat
import math
import sys

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

def run_train_test(traindata, testdata):
    f = open(traindata, "r")
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
    f = open(traindata, "r")
    Lines = f.readlines()

    for line in Lines:
        a = line.split(", ")
        for x in featuresMean:

            if float(a[numDict[x]]) <= (featuresMean[x]):
                
                numericalSplit(featuresHold[x][0], a[21])
            else:
                
                numericalSplit(featuresHold[x][1], a[21])
            



    f = open(testdata,"r")
    Lines = f.readlines()
    finalprob = 0
    count = 0
    answer = []
    for line in Lines:
        count += 1
        a = line.split(", ")
        probYes = float(0)
        probNo = float(0)
        for x in featuresMean:
            if float(a[numDict[x]]) <= (featuresMean[x]):
                probYes += math.log( featuresHold[x][0][0] / (featuresHold[x][0][0] + featuresHold[x][0][1]) )
                probNo += math.log( featuresHold[x][0][1] / (featuresHold[x][0][0] + featuresHold[x][0][1]) )
            else:
        
                probYes += math.log( featuresHold[x][1][0] / (featuresHold[x][1][0] + featuresHold[x][1][1]) )
                probNo += math.log( featuresHold[x][1][1] / (featuresHold[x][1][0] + featuresHold[x][1][1]) )
        #For loc
        probYes += math.log(featuresHold["loc"][a[0]][0] / (featuresHold["loc"][a[0]][0] + featuresHold["loc"][a[0]][1]) )
        probNo += math.log(featuresHold["loc"][a[0]][1] / (featuresHold["loc"][a[0]][0] + featuresHold["loc"][a[0]][1]) )
        #For windgusdir
        probYes += math.log(featuresHold["windgusdir"][a[6]][0] / (featuresHold["windgusdir"][a[6]][0] + featuresHold["windgusdir"][a[6]][1]) )
        probNo += math.log(featuresHold["windgusdir"][a[6]][1] / (featuresHold["windgusdir"][a[6]][0] + featuresHold["windgusdir"][a[6]][1]) )
        #For winddir9am
        probYes += math.log(featuresHold["winddir9am"][a[8]][0] / (featuresHold["winddir9am"][a[8]][0] + featuresHold["winddir9am"][a[8]][1]) )
        probNo += math.log(featuresHold["winddir9am"][a[8]][1] / (featuresHold["winddir9am"][a[8]][0] + featuresHold["winddir9am"][a[8]][1]) )
        #For winddir3pm
        probYes += math.log(featuresHold["winddir3pm"][a[9]][0] / (featuresHold["winddir3pm"][a[9]][0] + featuresHold["winddir3pm"][a[9]][1]) )
        probNo += math.log(featuresHold["winddir3pm"][a[9]][1] / (featuresHold["winddir3pm"][a[9]][0] + featuresHold["winddir3pm"][a[9]][1]) )
        #For raintoday
        probYes += math.log(featuresHold["raintoday"][a[20]][0] / (featuresHold["raintoday"][a[20]][0] + featuresHold["raintoday"][a[20]][1]) )
        probNo += math.log(featuresHold["raintoday"][a[20]][1] / (featuresHold["raintoday"][a[20]][0] + featuresHold["raintoday"][a[20]][1]) )


        if probYes > probNo:
            answer.append(1)
            if 'Yes\n' == a[21]:
                finalprob += 1
        else:
            answer.append(0)
            if 'No\n' == a[21]:
                finalprob += 1

    print(float(finalprob/count))



if __name__ == "__main__":
    
    testingdata = sys.argv[1]
    traindata = sys.argv[2]
    run_train_test(testingdata,traindata)








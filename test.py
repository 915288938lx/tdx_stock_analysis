import math


def cacShannonEnt(dataset):
    numEntries = len(dataset)
    labelCounts = {}
    for featVec in dataset:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1

    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * math.log(prob, 2)
    return shannonEnt


def CreateDataSet():
    dataset = [[1, 56, 'yes'],
               [1, 1, 'yas'],
               [1, 3, 'yes'],
               [1, 2, 'yes'],
               [1, 1, 'yes']
               ]
    labels = ['no surfacing', 'flippers']
    return dataset, labels


myDat, labels = CreateDataSet()
print(cacShannonEnt(myDat))
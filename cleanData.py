import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("datasets3_csv.csv", sep=";", skipinitialspace=True)

# ---------- Clean data ---------- #

dataClean = data.copy()

workclassVar, workclassCount = np.unique(data['Workclass'].astype(str), return_counts = True)
occupationVar, occupationCount = np.unique(data['Occupation'].astype(str), return_counts = True)
countryVar, countryCount = np.unique(data['Native country'].astype(str), return_counts = True)

mostFreqWorkclass = workclassVar[np.argmax(workclassCount, axis = 0)]
mostFreqOccupation = occupationVar[np.argmax(occupationCount, axis = 0)]
mostFreqCountry = countryVar[np.argmax(countryCount, axis = 0)]

dataClean.loc[dataClean['Workclass'].astype(str) == '?', 'Workclass'] = 'Other'
dataClean.loc[dataClean['Occupation'].astype(str) == '?', 'Occupation'] = 'Other'
dataClean.loc[dataClean['Income'].astype(str) == '>50K', 'Income'] = '1'
dataClean.loc[dataClean['Income'].astype(str) == '<=50K', 'Income'] = '0'
dataClean.loc[dataClean['Native country'].astype(str) == '?', 'Native country'] = mostFreqCountry

dataClean.drop(dataClean[dataClean['Occupation'].astype(str).str.isdigit()].index, inplace=True)
dataClean.drop(dataClean.tail(1).index, inplace=True)

dataClean.to_csv("data_clean/dataclean.csv")

# ---------- Plot data ---------- #

plotArray = ["Workclass", "Age", "Occupation", "Work hours per week"]
for item in plotArray:
    var, count = np.unique(dataClean[f'{item}'], return_counts = True)
    plt.figure(figsize=(32, 8))
    plt.title(f'{item} plot')
    plt.bar(var, count)
    plt.savefig(f'plot/{item}.png')

workclassVar, workclassCount = np.unique(dataClean['Workclass'].astype(str), return_counts = True)
plt.figure(figsize=(15, 10))
plt.title('Workclass plot')
plt.bar(workclassVar, workclassCount)
for index, value in enumerate(workclassCount):
    plt.text(index, value,
             str(value))

plt.savefig('plot/workclass.png')
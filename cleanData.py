import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("datasets3_csv.csv", sep=";", skipinitialspace=True)
dataClean = data.copy()

workclassVar, workclassCount = np.unique(data['Workclass'].astype(str), return_counts = True)
occupationVar, occupationCount = np.unique(data['Occupation'].astype(str), return_counts = True)
countryVar, countryCount = np.unique(data['Native country'].astype(str), return_counts = True)

mostFreqWorkclass = workclassVar[np.argmax(workclassCount, axis = 0)]
mostFreqOccupation = occupationVar[np.argmax(occupationCount, axis = 0)]
mostFreqCountry = countryVar[np.argmax(countryCount, axis = 0)]

dataClean.loc[dataClean['Workclass'].astype(str) == '?', 'Workclass'] = mostFreqWorkclass
dataClean.loc[dataClean['Occupation'].astype(str) == '?', 'Occupation'] = mostFreqOccupation
dataClean.loc[dataClean['Native country'].astype(str) == '?', 'Native country'] = mostFreqCountry

dataClean.to_csv("data_clean/workclass.csv")
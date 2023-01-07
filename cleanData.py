import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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
dataClean.loc[dataClean['Native country'].astype(str) == '?', 'Native country'] = mostFreqCountry

dataClean.drop(dataClean[dataClean['Occupation'].astype(str).str.isdigit()].index, inplace=True)
dataClean.dropna(inplace=True)

dataClean.to_csv("data_clean/dataclean.csv")

# ---------- Plot data ---------- #

hasBinaryLabel = ["Property owner", "Other asset", "Gender", "Income"]
hasExtraHeight = ["Native country"]
hasVerticalLabel = ["Native country"]
hasCount = ["Workclass", "Race", "Work hours per week", "Other asset"]
histPlot = ["Age"]

for item in dataClean.columns.values:

    if (item in hasBinaryLabel):
        var, count = np.unique(dataClean[f'{item}'].astype(str), return_counts = True)
    else:
        var, count = np.unique(dataClean[f'{item}'], return_counts = True)

    # Set size of the plot
    if (item in histPlot):
        figSize=(20,9)
    elif (item in hasBinaryLabel):
        figSize=(7, 7)
    elif (item in hasExtraHeight): 
        figSize=(12, 19)
    else:
        figSize=(16, 9)

    sns.set_palette("Set2")

    # Common
    fig, ax = plt.subplots(figsize=figSize)
    ax.set_title(f'{item} plot')

    if (item in histPlot):
        ax.bar(var, count)
    else:
        sns.barplot(x=var, y=count)

    # Conditional addition

    if (item in hasVerticalLabel):
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90)

    if (item in hasCount):
        for index, value in enumerate(count):
            plt.text(index, value, str(value))

    # Save to image
    fig.savefig(f'plot/{item}.png')

# workclassVar, workclassCount = np.unique(dataClean['Workclass'].astype(str), return_counts = True)
# plt.figure(figsize=(15, 10))
# plt.title('Workclass plot')
# plt.bar(workclassVar, workclassCount)
# for index, value in enumerate(workclassCount):
#     plt.text(index, value,
#              str(value))

# plt.savefig('plot/workclass.png')
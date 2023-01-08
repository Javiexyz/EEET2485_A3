import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("datasets3_csv.csv", sep=";", skipinitialspace=True)

# ---------- Clean data ---------- #

dataClean = data.copy()

# Drop
dataClean.dropna(inplace=True)
dataClean.drop(dataClean[dataClean['Occupation'].astype(str).str.isdigit()].index, inplace=True)

# Replace
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

dataClean['Martial status'] = dataClean['Martial status'].replace(",", "", regex = True)

dataClean.to_csv("data_clean/dataclean.csv")

# ---------- Plot data ---------- #

# Set style for plot
sns.set_theme(style="darkgrid")
sns.set_palette("Set2")

useHistplot = ["Age", 'Work hours per week']
hasBinaryLabel = ["Property owner", "Other asset", "Gender", "Income"]
hasExtraHeight = ["Native country"]
hasVerticalLabel = ["Native country"]
hasCount = ["Workclass", "Race", "Other asset"]

for item in dataClean.columns.values:

    # if (item in hasBinaryLabel):
    #     var, count = np.unique(dataClean[f'{item}'].astype(str), return_counts = True)
    # else:
    var, count = np.unique(dataClean[f'{item}'], return_counts = True)

    # Set size of the plot
    if (item in hasBinaryLabel):
        figSize=(7, 7)
    elif (item in hasExtraHeight): 
        figSize=(12, 19)
    else:
        figSize=(16, 9)

    # Common
    fig, ax = plt.subplots(figsize=figSize)
    ax.set_title(f'{item} plot')

    if (item in useHistplot):
        if (item == 'Work hours per week'):
            binWidth = 10
            kde = False
        else:
            binWidth = 1
            kde = True
        sns.histplot(data=dataClean[f'{item}'], binwidth=binWidth, kde=kde)
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

dataClean_categorical = dataClean.select_dtypes(exclude=['float'])

sns.set_theme(style="darkgrid")
sns.set_palette("Set2")

for col in dataClean_categorical.columns:
    g = sns.catplot(x=col, hue='Income',
                data=dataClean, kind="count",
                height=8, aspect=1.7)
    g.fig.set_size_inches(15, 8)
    
    for ax in g.axes.ravel():
    # add annotations
        for c in ax.containers:
            labels = [f'{(v.get_height() / 1000):.1f}K' for v in c]
            ax.bar_label(c, labels=labels, label_type='edge')
            ax.margins(y=0.2)

    plt.savefig(f'plotIncome/{col}.png')


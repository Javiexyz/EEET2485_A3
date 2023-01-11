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
hasVerticalLabel = ["Native country", "Occupation"]
hasCount = ["Workclass", "Race", "Other asset"]

for item in dataClean.columns.values:

    if (item in hasBinaryLabel):
        var, count = np.unique(dataClean[f'{item}'].astype(str), return_counts = True)
    else:
        var, count = np.unique(dataClean[f'{item}'], return_counts = True)

    # Set size of the plot
    if (item in hasBinaryLabel):
        figSize=(7, 7)
    elif (item in hasExtraHeight): 
        figSize=(12, 19)
    else:
        figSize=(16, 15)

    # Common
    fig, ax = plt.subplots(figsize=figSize)
    ax.set_title(f'{item} plot', fontsize=35)

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
    plt.close()

# ---------- Categorical plot ---------- #

dataClean_categorical = dataClean.select_dtypes(exclude=['float'])

for col in dataClean_categorical.columns:
    g = sns.catplot(x=col, hue='Income',
                data=dataClean, kind="count",
                height=8, aspect=1.7)
    g.fig.set_size_inches(16, 9)
    
    for ax in g.axes.ravel():
    # add annotations
        for c in ax.containers:
            labels = [f'{(v.get_height() / 1000):.1f}K' for v in c]
            ax.bar_label(c, labels=labels, label_type='edge')
            ax.margins(y=0.2)

    plt.title(col + " versus income")
    plt.savefig(f'plot_cat_income/{col}.png')
    plt.close()

# ---------- Box plot ---------- #

data_boxplot = dataClean[['Age', 'Work hours per week']].astype(int)
for item in data_boxplot.columns:
    plt.figure(figsize=(16, 9))
    sns.boxplot(x=dataClean['Income'], y=f'{item}', data=data_boxplot)
    plt.title(col + " versus income (boxplot)")
    plt.savefig(f'plot_box_income/{item}.png')
    plt.close()

    plt.figure(figsize=(16, 9))
    sns.boxplot(x=dataClean['Income'], y=f'{item}', data=data_boxplot, hue=dataClean['Gender'])
    plt.title(col + "versus income for each gender")
    plt.savefig(f'plot_box_income_gender/{item}.png')
    plt.close()

# ---------- Preprocessing categorical data (Extra) ---------- #

dataExtra = dataClean.copy()

dataExtra['Education'].replace("Preschool", "Dropout", regex=True, inplace=True)
dataExtra['Education'].replace("10th", "Dropout",regex=True, inplace=True)
dataExtra['Education'].replace("11th", "Dropout",regex=True, inplace=True)
dataExtra['Education'].replace("12th", "Dropout",regex=True, inplace=True)
dataExtra['Education'].replace("1st-4th", "Dropout",regex=True, inplace=True)
dataExtra['Education'].replace("5th-6th", "Dropout",regex=True, inplace=True)
dataExtra['Education'].replace("7th-8th", "Dropout",regex=True, inplace=True)
dataExtra['Education'].replace("9th", "Dropout",regex=True, inplace=True)
dataExtra['Education'].replace("HS-Grad", "HighGrad",regex=True, inplace=True)
dataExtra['Education'].replace("HS-grad", "HighGrad",regex=True, inplace=True)
dataExtra['Education'].replace("Some-college", "CommunityCollege",regex=True, inplace=True)
dataExtra['Education'].replace("Assoc-acdm", "CommunityCollege",regex=True, inplace=True)
dataExtra['Education'].replace("Assoc-voc", "CommunityCollege",regex=True, inplace=True)
dataExtra['Education'].replace("Bachelors", "Bachelors",regex=True, inplace=True)
dataExtra['Education'].replace("Masters", "Masters",regex=True, inplace=True)
dataExtra['Education'].replace("Prof-school", "Masters",regex=True, inplace=True)
dataExtra['Education'].replace("Doctorate", "Doctorate",regex=True, inplace=True)

dataExtra.to_csv("data_clean/dataextra.csv")

# ---------- Extra plot ---------- #

var, count = np.unique(dataExtra['Education'], return_counts = True)

fig, ax = plt.subplots(figsize=(16, 9))
ax.set_title('Education extra plot')
sns.barplot(x=var, y=count)
fig.savefig('plot/Education_extra.png')
plt.close()

g = sns.catplot(x='Education', hue='Income',
                data=dataExtra, kind="count",
                height=8, aspect=1.7)
g.fig.set_size_inches(16, 9)
    
for ax in g.axes.ravel():
    # add annotations
    for c in ax.containers:
        labels = [f'{(v.get_height() / 1000):.1f}K' for v in c]
        ax.bar_label(c, labels=labels, label_type='edge')
        ax.margins(y=0.2)

plt.savefig('plot_cat_income/Education_extra.png')
plt.close()
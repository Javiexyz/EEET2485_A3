import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as ss
import random

data = pd.read_csv("datasets3_csv.csv", sep=";", skipinitialspace=True)

# ---------- Clean data ---------- #

dataClean = data.copy()

# Drop
dataClean.dropna(inplace=True)
dataClean.drop(dataClean[dataClean['Occupation'].astype(str).str.isdigit()].index, inplace=True)
#dataClean.drop(dataClean[dataClean['Workclass'].astype(str) == '?'].index, inplace=True)

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

# Plot for categorical data only (with Income)
# dataClean_categorical = dataClean.select_dtypes(exclude=['float'])
# dataClean_categorical.insert(0,'Education (Year)',dataClean['Education (Year)'])

# for col in dataClean_categorical.columns:
#     if (col != 'Income'):
#         g = sns.catplot(x=col, hue='Income',
#                     data=dataClean, kind="count",
#                     height=8, aspect=1.7)
#         g.fig.set_size_inches(15, 8)
        
#         for ax in g.axes.ravel():
#         # add annotations
#             for c in ax.containers:
#                 labels = [f'{(v.get_height() / 1000):.1f}K' for v in c]
#                 ax.bar_label(c, labels=labels, label_type='edge')
#                 ax.margins(y=0.2)

#         plt.savefig(f'plotIncome/{col}.png')

## Chi-square test
from scipy.stats import chi2_contingency
from scipy.stats import chi2

# # Income vs Workclass +
# #data_cont = pd.crosstab(dataClean['Workclass'].sample(frac=0.005, replace=True, random_state=1),dataClean['Income'].sample(frac=0.005, replace=True, random_state=1),margins = False)
# data_cont = pd.crosstab(dataClean['Workclass'], dataClean['Income'], margins = False)
# print(data_cont)
# stat, p, dof, expected = chi2_contingency(data_cont)
# print('dof=%d' % dof)
# print('p_value', p)
# print(expected)
# # interpret test-statistic
# prob = 0.95
# critical = chi2.ppf(prob, dof)
# print('probability=%.3f, critical=%.3f, stat=%.3f' % (prob, critical, stat))
# if abs(stat) >= critical:
#     print('Dependent (reject H0)')
# else:
#     print('Independent (fail to reject H0)')

# # Property vs Marital
# #data_cont = pd.crosstab(dataClean['Martial status'].sample(frac=0.005, replace=True, random_state=1),dataClean['Property owner'].sample(frac=0.005, replace=True, random_state=1),margins = False)
# data_cont = pd.crosstab(dataClean['Education'], dataClean['Education (Year)'], margins = False)
# print(data_cont)
# stat, p, dof, expected = chi2_contingency(data_cont)
# print('dof=%d' % dof)
# print('p_value', p)
# print(expected)
# # interpret test-statistic
# prob = 0.95
# critical = chi2.ppf(prob, dof)
# print('probability=%.3f, critical=%.3f, stat=%.3f' % (prob, critical, stat))
# if abs(stat) >= critical:
#     print('Dependent (reject H0)')
# else:
#     print('Independent (fail to reject H0)')


## Independent sample T-test
from scipy.stats import ttest_ind


data_test = dataClean[['Age','Work hours per week','Income']].astype(int)

#Age vs Income
group_income1 = data_test[data_test['Income']==1]['Age']
group_income0 = data_test[data_test['Income']==0]['Age']

group_income0 = random.sample(sorted(group_income0), 7000)
group_income1 = random.sample(sorted(group_income1), 7000)

ttest,pval = ttest_ind(group_income1,group_income0,equal_var = False)
print("ttest",ttest)
print('p value',pval)
if pval <0.05:
    print("we reject null hypothesis")
else:
    print("we accept null hypothesis")

# #Working hours vs Income
# group_income1 = data_test[data_test['Income']==1]['Work hours per week']
# group_income0 = data_test[data_test['Income']==0]['Work hours per week']

# group_income0 = random.sample(sorted(group_income0), 7000)
# group_income1 = random.sample(sorted(group_income1), 7000)

# ttest,pval = ttest_ind(group_income1,group_income0,equal_var = False)
# print("ttest",ttest)
# print('p value',pval)
# if pval <0.05:
#     print("we reject null hypothesis")
# else:
#     print("we accept null hypothesis")
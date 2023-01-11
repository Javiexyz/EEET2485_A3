import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import random

dt = pd.read_csv("datasets3_csv.csv", sep=";", skipinitialspace=True)
data = pd.read_csv('data_clean/dataclean.csv')

# ---------- Clean data ---------- #

dataClean = dt.copy()

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
dataClean_categorical = dataClean.select_dtypes(exclude=['float'])
dataClean_categorical.insert(0,'Education (Year)',dataClean['Education (Year)'])

for col in dataClean_categorical.columns:
    if (col != 'Income'):
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

# Chi-square test
from scipy.stats import chi2_contingency
from scipy.stats import chi2

chi_vars_income= ['Gender', 'Race', 'Workclass', 'Education', 'Occupation', 'Martial status', 'Family Role', 'Property owner', 'Other asset']

for var in chi_vars_income:
    data_cont = pd.crosstab(dataClean[var], dataClean['Income'], margins=False)
    stat, p, dof, expected = chi2_contingency(data_cont)
    print('degree of freedom =', dof, ' and p_value = ', p)
    # interpret test-statistic
    prob = 0.95
    critical = chi2.ppf(prob, dof)
    if abs(stat) >= critical:
        print('Income is dependent (reject H0) to ' + var + '\n')
    else:
        print('Income is independent (fail to reject H0) to ' + var + '\n')

chi_vars_prop= ['Gender', 'Race', 'Workclass', 'Education', 'Occupation', 'Martial status', 'Family Role', 'Income', 'Other asset']

for var in chi_vars_prop:
    data_cont = pd.crosstab(dataClean[var], dataClean['Income'], margins=False)
    stat, p, dof, expected = chi2_contingency(data_cont)
    print('degree of freedom =', dof, ' and p_value = ', p)
    # interpret test-statistic
    prob = 0.95
    critical = chi2.ppf(prob, dof)
    if abs(stat) >= critical:
        print('Property owner is dependent (reject H0) to ' + var + '\n')
    else:
        print('Property owner is independent (fail to reject H0) to ' + var + '\n')

chi_vars_asset= ['Gender', 'Race', 'Workclass', 'Education', 'Occupation', 'Martial status', 'Family Role', 'Property owner', 'Income']

for var in chi_vars_asset:
    data_cont = pd.crosstab(dataClean[var], dataClean['Income'], margins=False)
    stat, p, dof, expected = chi2_contingency(data_cont)
    print('degree of freedom =', dof, ' and p_value = ', p)
    # interpret test-statistic
    prob = 0.95
    critical = chi2.ppf(prob, dof)
    if abs(stat) >= critical:
        print('Other asset is dependent (reject H0) to ' + var + '\n')
    else:
        print('Other asset is independent (fail to reject H0) to ' + var + '\n')

# Independent sample T-test
from scipy.stats import ttest_ind
data_test = dataClean[['Age','Work hours per week','Income', 'Saving (Cash)']].astype(int)

t_test_income = ['Age', 'Work hours per week', 'Saving (Cash)']
for t in t_test_income:
    group_income1 = data_test[data_test['Income'] == 1][t]
    group_income0 = data_test[data_test['Income'] == 0][t]

    group_income0 = random.sample(sorted(group_income0), 7000)
    group_income1 = random.sample(sorted(group_income1), 7000)

    ttest, pval = ttest_ind(group_income1, group_income0, equal_var=False)
    print("T coefficient", ttest)
    print('p value', pval)
    if pval < 0.05:
        print('reject null hypothesis -> ', t, ' and income are dependent \n')
    else:
        print('accept null hypothesis -> ', t, ' and income are independent \n')

t_test_prop = ['Age', 'Work hours per week', 'Saving (Cash)']
for t in t_test_prop:
    group_income1 = data_test[data_test['Income'] == 1][t]
    group_income0 = data_test[data_test['Income'] == 0][t]

    group_income0 = random.sample(sorted(group_income0), 7000)
    group_income1 = random.sample(sorted(group_income1), 7000)

    ttest, pval = ttest_ind(group_income1, group_income0, equal_var=False)
    # print("T coefficient", ttest)
    # print('p value', pval)
    if pval < 0.05:
        print('reject null hypothesis -> ', t, ' and property owner are dependent \n')
    else:
        print('accept null hypothesis -> ', t, ' and property owner are independent \n')

# Anova Test: Average working hours versus education level
# Q10:  What is the difference in average working hours among types of edu levels? - ANOVA
statistic, pvalue = stats.f_oneway(data['Work hours per week'][data['Education'] == 'Preschool'].sample(50, replace=False),
                                   data['Work hours per week'][data['Education'] == '1st-4th'].sample(50, replace=False),
                                   data['Work hours per week'][data['Education'] == '5th-6th'].sample(50, replace=False),
                                   data['Work hours per week'][data['Education'] == '7th-8th'].sample(50, replace=False),
                                   data['Work hours per week'][data['Education'] == '9th'].sample(50, replace=False),
                                   data['Work hours per week'][data['Education'] == '10th'].sample(50, replace=False),
                                   data['Work hours per week'][data['Education'] == '11th'].sample(50, replace=False),
                                   data['Work hours per week'][data['Education'] == '12th'].sample(50, replace=False),
                                   data['Work hours per week'][data['Education'] == 'HS-grad'].sample(50, replace=False),
                                   data['Work hours per week'][data['Education'] == 'Bachelors'].sample(50, replace=False),
                                   data['Work hours per week'][data['Education'] == 'Assoc-acdm'].sample(50, replace=False),
                                   data['Work hours per week'][data['Education'] == 'Assoc-voc'].sample(50, replace=False),
                                   data['Work hours per week'][data['Education'] == 'Prof-school'].sample(50, replace=False),
                                   data['Work hours per week'][data['Education'] == 'Some-college'].sample(50, replace=False),
                                   data['Work hours per week'][data['Education'] == 'Masters'].sample(50, replace=False),
                                   data['Work hours per week'][data['Education'] == 'Doctorate'].sample(50, replace=False))
print('Q10:  What is the difference in average working hours among types of edu levels? - ANOVA')
print("f-statistic:" + str(statistic))
print("p-value:" + str(pvalue))

# # Plotting for ANOVA Test
# edus = data['Education'].unique()
# for edu in edus:
#     stats.probplot(data[data['Education'] == edu]['Work hours per week'].sample(50, replace=False), dist="norm", plot=plt)
#     plt.title("Probability Plot - " +  edu)
#     plt.savefig(f'anova_plot_wh_eduLevel/{edu}.png')
#     plt.show()



import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import random
from scipy.stats import chi2_contingency
from scipy.stats import chi2

# ---------- Clean data ---------- #
data = pd.read_csv("datasets3_csv.csv", sep=";", skipinitialspace=True)
dataClean = data.copy()

# Drop
dataClean.dropna(inplace=True)
dataClean.drop(dataClean[dataClean['Occupation'].astype(str).str.isdigit()].index, inplace=True)

# Replace
workclassVar, workclassCount = np.unique(data['Workclass'].astype(str), return_counts=True)
occupationVar, occupationCount = np.unique(data['Occupation'].astype(str), return_counts=True)
countryVar, countryCount = np.unique(data['Native country'].astype(str), return_counts=True)

mostFreqWorkclass = workclassVar[np.argmax(workclassCount, axis=0)]
mostFreqOccupation = occupationVar[np.argmax(occupationCount, axis=0)]
mostFreqCountry = countryVar[np.argmax(countryCount, axis=0)]

dataClean.loc[dataClean['Workclass'].astype(str) == '?', 'Workclass'] = 'Other'
dataClean.loc[dataClean['Occupation'].astype(str) == '?', 'Occupation'] = 'Other'
dataClean.loc[dataClean['Income'].astype(str) == '>50K', 'Income'] = '1'
dataClean.loc[dataClean['Income'].astype(str) == '<=50K', 'Income'] = '0'
dataClean.loc[dataClean['Native country'].astype(str) == '?', 'Native country'] = mostFreqCountry

dataClean['Martial status'] = dataClean['Martial status'].replace(",", "", regex=True)

dataClean.to_csv("data_clean/dataclean.csv")

factors = ['Age', 'Education', 'Workclass', 'Occupation', 'Gender', 'Race', 'Work hours per week', 'Martial status']
long_factors = ['Age', 'Education', 'Workclass', 'Occupation', 'Work hours per week']
evaluate = ['Income', 'Saving (Cash)', 'Property owner', 'Other asset']

"""---Create lists to contain figures in right order!!!---"""

# Plot for categorical data only (with Income)
dataClean_categorical = dataClean.select_dtypes(exclude=['float'])
dataClean_categorical.insert(0, 'Education (Year)', dataClean['Education (Year)'])

# Plotting diagram
for e in evaluate:
    for f in factors:
        g = sns.catplot(x=f, hue=e,
                        data=dataClean, kind='count',
                        height=8, aspect=2)
        g.fig.set_size_inches(30, 15)
        sns.set(font_scale=3)

        for ax in g.axes.ravel():
            # add annotations
            for c in ax.containers:
                if (f == 'Income'):
                    labels = [f'{(v.get_height() / 10):.1f}K' for v in c]
                    ax.bar_label(c, labels=labels, label_type='edge')
            if (f in long_factors):
                ax.set_xticklabels(ax.get_xticklabels(), rotation=90)

        plt.title(f'{f} vs {e} plot')
        plt.tick_params(axis='both', which='major', labelsize=14)
        plt.savefig(f'evaluateFactor/{f} vs {e}.png')

# Question Testing

dataExtra = dataClean.copy()

dataExtra['Education'].replace("Preschool", "Dropout", regex=True, inplace=True)
dataExtra['Education'].replace("10th", "Dropout",regex=True, inplace=True)
dataExtra['Education'].replace("11th", "Dropout",regex=True, inplace=True)
dataExtra['Education'].replace("12th", "Dropout",regex=True, inplace=True)
dataExtra['Education'].replace("1st-4th", "Dropout",regex=True, inplace=True)
dataExtra['Education'].replace("5th-6th", "Dropout",regex=True, inplace=True)
dataExtra['Education'].replace("7th-8th", "Dropout",regex=True, inplace=True)
dataExtra['Education'].replace("9th", "Dropout",regex=True, inplace=True)
dataExtra['Education'].replace("Some-college", "CommunityCollege",regex=True, inplace=True)
dataExtra['Education'].replace("Assoc-acdm", "CommunityCollege",regex=True, inplace=True)
dataExtra['Education'].replace("Assoc-voc", "CommunityCollege",regex=True, inplace=True)
dataExtra['Education'].replace("Bachelors", "Bachelors",regex=True, inplace=True)
dataExtra['Education'].replace("Masters", "Postgrad",regex=True, inplace=True)
dataExtra['Education'].replace("Prof-school", "Postgrad",regex=True, inplace=True)
dataExtra['Education'].replace("Doctorate", "Postgrad",regex=True, inplace=True)

evaluate_no_saving = ['Income', 'Property owner', 'Other asset']
t_test_factors = ['Age', 'Work hours per week']

for e in evaluate_no_saving:
    for f in factors:
        if f in t_test_factors:
            if e == 'Income':
                group_1 = dataClean[dataClean[e] == '1'][f]
                group_0 = dataClean[dataClean[e] == '0'][f]
            else:
                group_1 = dataClean[dataClean[e] == 1][f]
                group_0 = dataClean[dataClean[e] == 0][f]

            group_1 = random.sample(sorted(group_1), 7000)
            group_0 = random.sample(sorted(group_0), 7000)

            ttest, pval = stats.ttest_ind(group_1, group_0, equal_var=False)
            print("T coefficient", ttest)
            print('p value', pval)

            if pval < 0.05:
                print('Reject null hypothesis --> ' + f + ' and ' + e + ' are dependent\n')
            else:
                print('Accept null hypothesis --> ' + f + ' and ' + e + ' are independent\n')
        else:
            data_cont = pd.crosstab(dataClean[f], dataClean[e], margins=False)
            stat, p, dof, expected = chi2_contingency(data_cont)
            print('degree of freedom =', dof, ' and p_value = ', p)
            # interpret test-statistic
            prob = 0.95
            critical = chi2.ppf(prob, dof)
            if abs(stat) >= critical:
                print('Reject null hypothesis --> ' + f + ' and ' + e + ' are dependent\n')
            else:
                print('Accept null hypothesis --> ' + f + ' and ' + e + ' are independent\n')

# Testing for saving:
for f in factors:
    # ANOVA test
    if f in t_test_factors:
        group_0 = dataClean[dataClean['Saving (Cash)'] == 0][f]
        group_1 = dataClean[dataClean['Saving (Cash)'] == 1][f]
        group_2 = dataClean[dataClean['Saving (Cash)'] == 2][f]
        group_3 = dataClean[dataClean['Saving (Cash)'] == 3][f]
        group_4 = dataClean[dataClean['Saving (Cash)'] == 4][f]
        group_5 = dataClean[dataClean['Saving (Cash)'] == 5][f]
        # print(group_0.size, group_1.size, group_2.size, group_3.size, group_4.size, group_5.size)

        group_0 = random.sample(sorted(group_0), 5000)
        group_1 = random.sample(sorted(group_1), 5000)
        group_2 = random.sample(sorted(group_2), 5000)
        group_3 = random.sample(sorted(group_3), 5000)
        group_4 = random.sample(sorted(group_4), 5000)
        group_5 = random.sample(sorted(group_5), 5000)

        f_statistics, p_value = stats.f_oneway(group_5, group_4, group_3, group_2, group_1, group_0)
        print("F coefficient", f_statistics)
        print('p value', p_value)

        if pval < 0.05:
            print('Reject null hypothesis --> ' + f + ' and Saving (Cash) are dependent\n')
        else:
            print('Accept null hypothesis --> ' + f + ' and Saving (Cash) are independent\n')
    else:
        data_cont = pd.crosstab(dataClean[f], dataClean['Saving (Cash)'], margins=False)
        stat, p, dof, expected = chi2_contingency(data_cont)
        print('degree of freedom =', dof, ' and p_value = ', p)
        # interpret test-statistic
        prob = 0.95
        critical = chi2.ppf(prob, dof)
        if abs(stat) >= critical:
            print('Reject null hypothesis --> ' + f + ' and Saving (Cash) are dependent\n')
        else:
            print('Accept null hypothesis --> ' + f + ' and Saving (Cash) are independent\n')

# Anova Test: Average working hours versus education level
# Q10:  What is the difference in average working hours among types of edu levels? - ANOVA

# Group Education levels in 5 categories
dropout = dataExtra['Work hours per week'][dataExtra['Education'] == 'Dropout'].head(2000)
hsgrad = dataExtra['Work hours per week'][dataExtra['Education'] == 'HS-grad'].head(2000)
community = dataExtra['Work hours per week'][dataExtra['Education'] == 'CommunityCollege'].head(2000)
bachelors = dataExtra['Work hours per week'][dataExtra['Education'] == 'Bachelors'].head(2000)
postgrad = dataExtra['Work hours per week'][dataExtra['Education'] == 'Postgrad'].head(2000)
# Save them to csv file to test in jamovi
dropout.to_csv('data_clean/dropout.csv')
hsgrad.to_csv('data_clean/hsgrad.csv')
community.to_csv('data_clean/com.csv')
bachelors.to_csv('data_clean/bsc.csv')
postgrad.to_csv('data_clean/postgrad.csv')
# test ANOVA using Python library package scipy.stats
statistic, pvalue = stats.f_oneway(dataExtra['Work hours per week'][dataExtra['Education'] == 'Dropout'].head(2000),
                                    dataExtra['Work hours per week'][dataExtra['Education'] == 'HS-grad'].head(2000),
                                    dataExtra['Work hours per week'][dataExtra['Education'] == 'CommunityCollege'].head(2000),
                                    dataExtra['Work hours per week'][dataExtra['Education'] == 'Bachelors'].head(2000),
                                    dataExtra['Work hours per week'][dataExtra['Education'] == 'Postgrad'].head(2000))
print('Q10:  What is the difference in average working hours among types of edu levels? - ANOVA')
print("f-statistic:" + str(statistic))
print("p-value:" + str(pvalue))

# Plotting for ANOVA Test
edus = dataClean['Education'].unique()
for edu in edus:
    stats.probplot(dataClean[dataClean['Education'] == edu]['Work hours per week'].sample(50, replace=False), dist="norm", plot=plt)
    plt.title("Probability Plot - " +  edu)
    plt.savefig(f'anova_plot_wh_eduLevel/{edu}.png')
    # plt.show()


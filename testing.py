import random

import pandas as pd
import numpy as np
import scipy.stats as stats
import researchpy as rp
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols

data = pd.read_csv("data_clean/dataclean.csv")

# t-test: Is there familiar between middle age and young age employees in their income? - 2 sample T-test
u40 = data[(data['Age'] < 40) & (data['Age'] >= 25)]['Income']
f40 = data[(data['Age'] >= 40) & (data['Age'] <= 65)]['Income']

u40 = u40.values.tolist()
u40 = random.sample(u40, 600)
f40 = f40.values.tolist()
f40 = random.sample(f40, 600)

ttest,pval = stats.ttest_ind(u40,f40,equal_var = False)
print("ttest",ttest)
print('p value',format(pval, '.70f'))

if pval <0.05:
    print("we reject null hypothesis")
else:
    print("we accept null hypothesis")

# Q2: Is there any association between mean working hours and income? - 2-sample T-test
m50 = data[data['Income'] == 1]['Work hours per week']
l50 = data[data['Income'] == 0]['Work hours per week']

m50 = m50.values.tolist()
m50 = random.sample(m50, 600)
l50 = l50.values.tolist()
l50 = random.sample(l50, 600)

ttest,pval = stats.ttest_ind(m50,l50,equal_var = False)
print("ttest",ttest)
print('p value',format(pval, '.70f'))

if pval <0.05:
    print("we reject null hypothesis")
else:
    print("we accept null hypothesis")

# Anova Test: Average working hours versus education level
# print(rp.summary_cont(data['Work hours per week']))
# print(rp.summary_cont(data['Work hours per week'].groupby(data['Education'])))

print(data['Work hours per week'][data['Education'] == 'Preschool'].sample(50, replace=False))

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

print("f-statistic:" + str(statistic))
print("p-value:" + str(pvalue))










import random

import pandas as pd
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("data_clean/dataclean.csv")

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

# Plotting for ANOVA Test
edus = data['Education'].unique()
for edu in edus:
    stats.probplot(data[data['Education'] == edu]['Work hours per week'].sample(50, replace=False), dist="norm", plot=plt)
    plt.title("Probability Plot - " +  edu)
    plt.savefig(f'anova_plot_wh_eduLevel/{edu}.png')
    plt.show()










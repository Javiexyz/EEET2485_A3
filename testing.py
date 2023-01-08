import random

import pandas as pd
from scipy.stats import ttest_ind

data = pd.read_csv("data_clean/dataclean.csv")

u40 = data[(data['Age'] < 40) & (data['Age'] >= 25)]['Income']
f40 = data[(data['Age'] >= 40) & (data['Age'] <= 65)]['Income']

u40 = u40.values.tolist()
u40 = random.sample(u40, 600)
f40 = f40.values.tolist()
f40 = random.sample(f40, 600)

ttest,pval = ttest_ind(u40,f40,equal_var = False)
print("ttest",ttest)
print('p value',format(pval, '.70f'))

if pval <0.05:
    print("we reject null hypothesis")
else:
    print("we accept null hypothesis")










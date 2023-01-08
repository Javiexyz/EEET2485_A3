import numpy as np
import pandas as pd
import researchpy as rp
from scipy import stats

# Fix req: covert to boolean number for income col


# U40 group (25 -> 39)
data = pd.read_csv("data_clean/dataclean.csv")
data.drop(data[(data['Age'] >= 40) | (data['Age'] < 25)].index, inplace=True)
df_under40 = data["Income"]
under40 = np.array(df_under40)
mean_under40 = under40.mean()
# print(np.round(mean_under40, 3))
n_under40 = len(str(mean_under40))
print(n_under40)

# From 40 (40 -> 65)
dt = pd.read_csv("data_clean/dataclean.csv")
dt.drop(dt[(dt['Age'] > 65) | (dt['Age'] < 40)].index, inplace=True)
df_from40 = dt["Income"]
from40 = np.array(df_from40)
mean_from40 = from40.mean()
# print(np.round(mean_from40, 3))
n_from40 = len(str(mean_from40))
print(n_from40)

var_under40, var_from40 = np.var(under40, ddof=1.0), np.var(from40, ddof=1.0)

# variance
var = (((n_under40 - 1)*var_under40) + ((n_from40 - 1)*var_from40)) / (n_under40 + n_from40 - 2)

# standard error
std_err = np.sqrt(var * (1.0 / n_under40 + 1.0 / n_from40))

# print result
print("under 40 mean:", np.round(mean_under40, 4))
print("from 40 mean:", np.round(mean_from40, 4))
print("variance of under 40:", np.round(var_under40, 4))
print("variance of from 40:", np.round(var_from40, 4))
print("pooled sample variance:", np.round(var, 4))
print("standard error:", np.round(std_err, 4))

# calculate t statistics
t = abs(mean_under40 - mean_from40) / std_err

print('t static:', t)
# two-tailed critical value at alpha = 0.05
t_c = stats.t.ppf(q=0.975, df=18)
print("Critical value for t two tailed:", np.round(t_c, 4))

# one-tailed critical value at alpha = 0.05
t_c = stats.t.ppf(q=0.95, df=18)
print("Critical value for t one tailed:", np.round(t_c, 4))

# get two-tailed p value
p_two = 2 * (1 - stats.t.cdf(x=t, df=18))
print("p-value for two tailed:", np.round(p_two, 4))

# get one-tailed p value
p_one = 1 - stats.t.cdf(x=t, df=18)
print("p-value for one tailed:", np.round(p_one, 4))











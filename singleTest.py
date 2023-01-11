# # Q2: Is there a dependency between mean age in the two income group?
# group_income1 = data_test[data_test['Income']==1]['Age']
# group_income0 = data_test[data_test['Income']==0]['Age']
#
# group_income0 = random.sample(sorted(group_income0), 7000)
# group_income1 = random.sample(sorted(group_income1), 7000)
#
# ttest,pval = ttest_ind(group_income1,group_income0,equal_var = False)
# print('Q2: Is there a dependency between mean age in the two income group?')
# print("T coefficient",ttest)
# print('p value',pval)
# if pval <0.05:
#     print("we reject null hypothesis -> independent")
# else:
#     print("we accept null hypothesis -> dependent")
#
# # Working hours vs Income
# # Q1: Is there any association between mean working hours and income?
# group_income1 = data_test[data_test['Income']==1]['Work hours per week']
# group_income0 = data_test[data_test['Income']==0]['Work hours per week']
#
# group_income0 = random.sample(sorted(group_income0), 7000)
# group_income1 = random.sample(sorted(group_income1), 7000)
#
# ttest,pval = ttest_ind(group_income1,group_income0,equal_var = False)
# print('Q1: Is there any association between mean working hours and income?')
# print("T coefficient",ttest)
# print('p value',pval)
# if pval <0.05:
#     print("we reject null hypothesis \n")
# else:
#     print("we accept null hypothesis \n")
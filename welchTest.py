# # Welch's ANOVA test
# dataTest = dataClean['Work hours per week'][dataClean['Education'] == 'Preschool'].head(50),\
#     dataClean['Work hours per week'][dataClean['Education'] == '1st-4th'].head(50),\
#     dataClean['Work hours per week'][dataClean['Education'] == '5th-6th'].head(50),\
#     dataClean['Work hours per week'][dataClean['Education'] == '7th-8th'].head(50),\
#     dataClean['Work hours per week'][dataClean['Education'] == '9th'].head(50),\
#     dataClean['Work hours per week'][dataClean['Education'] == '10th'].head(50),\
#     dataClean['Work hours per week'][dataClean['Education'] == '11th'].head(50),\
#     dataClean['Work hours per week'][dataClean['Education'] == '12th'].head(50),\
#     dataClean['Work hours per week'][dataClean['Education'] == 'HS-grad'].head(50),\
#     dataClean['Work hours per week'][dataClean['Education'] == 'Bachelors'].head(50),\
#     dataClean['Work hours per week'][dataClean['Education'] == 'Assoc-acdm'].head(50),\
#     dataClean['Work hours per week'][dataClean['Education'] == 'Assoc-voc'].head(50),\
#     dataClean['Work hours per week'][dataClean['Education'] == 'Prof-school'].head(50),\
#     dataClean['Work hours per week'][dataClean['Education'] == 'Some-college'].head(50),\
#     dataClean['Work hours per week'][dataClean['Education'] == 'Masters'].head(50),\
#     dataClean['Work hours per week'][dataClean['Education'] == 'Doctorate'].head(50)
# print(stats.bartlett(dataClean['Work hours per week'][dataClean['Education'] == 'Preschool'].head(50),
#                     dataClean['Work hours per week'][dataClean['Education'] == '1st-4th'].head(50),
#                     dataClean['Work hours per week'][dataClean['Education'] == '5th-6th'].head(50),
#                     dataClean['Work hours per week'][dataClean['Education'] == '7th-8th'].head(50),
#                     dataClean['Work hours per week'][dataClean['Education'] == '9th'].head(50),
#                     dataClean['Work hours per week'][dataClean['Education'] == '10th'].head(50),
#                     dataClean['Work hours per week'][dataClean['Education'] == '11th'].head(50),
#                     dataClean['Work hours per week'][dataClean['Education'] == '12th'].head(50),
#                     dataClean['Work hours per week'][dataClean['Education'] == 'HS-grad'].head(50),
#                     dataClean['Work hours per week'][dataClean['Education'] == 'Bachelors'].head(50),
#                     dataClean['Work hours per week'][dataClean['Education'] == 'Assoc-acdm'].head(50),
#                     dataClean['Work hours per week'][dataClean['Education'] == 'Assoc-voc'].head(50),
#                     dataClean['Work hours per week'][dataClean['Education'] == 'Prof-school'].head(50),
#                     dataClean['Work hours per week'][dataClean['Education'] == 'Some-college'].head(50),
#                     dataClean['Work hours per week'][dataClean['Education'] == 'Masters'].head(50),
#                     dataClean['Work hours per week'][dataClean['Education'] == 'Doctorate'].head(50)))
# dt = []
# for t in dataTest:
#     print(t)
#     test = t.astype('int')
#     dt.append(test)
#     # print(len(dt))
#     # print(t.size, len(dataTest))
# # print(dt)
# edu_list = ['Preschool', '1st-4th', '5th-6th', '7th-8th', '9th', '10th', '11th', '12th', 'HS-grad',
#             'Bachelors', 'Assoc-acdm', 'Assoc-voc', 'Prof-school', 'Some-college', 'Masters', 'Doctorate']
# df = pd.DataFrame({'data':dt, 'group':(edu_list)})
# print(type(dt))
# # print(pg.welch_anova(dv='data', between='group', data=df))
import pandas as pd
# import numpy as np

data = pd.read_csv("datasets3_csv.csv", sep=";")

"""
Write as text file - Example

ages_dataframe = pd.DataFrame({'Age': age, 'Counts': count, 'Percent': percent})
np_ages = ages_dataframe.to_numpy()
np.savetxt("data_record/ages.txt", np_ages, fmt="%s", delimiter=',\t')

"""


# 1 - AGES
ages = data["Age"]
for column in ages:
    print("Ages")
    count = ages.value_counts()
    percent = ages.value_counts(normalize=True).mul(100).round(2).astype(str) + '%'
    ages_dataframe = pd.DataFrame({'Counts': count, 'Percent': percent})
    ages_dataframe.to_csv('data_record/ages.csv')
    print(pd.DataFrame({'Counts': count, 'Percent': percent}))
    print('--------------------------------')
    break

# 2 - WORKCLASS
workclass = data["Workclass"]
for column in data["Workclass"]:
    print("Workclass")
    count = workclass.value_counts()
    percent = workclass.value_counts(normalize=True).mul(100).round(2).astype(str) + '%'
    works_dataframe = pd.DataFrame({'Counts': count, 'Percent': percent})
    works_dataframe.to_csv('data_record/workclass.csv')
    print(pd.DataFrame({'Counts': count, 'Percent': percent}))
    print('--------------------------------')
    break

# 3 - EDUCATION LEVEL
education_level = data["Education"]
for column in education_level:
    print("Education Level")
    count = education_level.value_counts()
    percent = education_level.value_counts(normalize=True).mul(100).round(2).astype(str) + '%'
    edus_dataframe = pd.DataFrame({'Counts': count, 'Percent': percent})
    edus_dataframe.to_csv('data_record/education_level.csv')
    print(pd.DataFrame({'Counts': count, 'Percent': percent}))
    print('--------------------------------')
    break

# 4 - EDUCATION YEAR
education_year = data["Education (Year)"]
for column in education_year:
    print("Education Level")
    count = education_year.value_counts()
    percent = education_year.value_counts(normalize=True).mul(100).round(2).astype(str) + '%'
    edus_yr_dataframe = pd.DataFrame({'Counts': count, 'Percent': percent})
    edus_yr_dataframe.to_csv('data_record/education_yr.csv')
    print(pd.DataFrame({'Counts': count, 'Percent': percent}))
    print('--------------------------------')
    break

# 5 - MARTIAL STATUS
martial_status = data["Martial status"]
for column in martial_status:
    print("Martial status")
    count = martial_status.value_counts()
    percent = martial_status.value_counts(normalize=True).mul(100).round(2).astype(str) + '%'
    status_dataframe = pd.DataFrame({'Counts': count, 'Percent': percent})
    status_dataframe.to_csv('data_record/martial_status.csv')
    print(pd.DataFrame({'Counts': count, 'Percent': percent}))
    print('--------------------------------')
    break

# 6 - OCCUPATION
occupation = data["Occupation"]
for column in occupation:
    print("Occupation")
    count = occupation.value_counts()
    percent = occupation.value_counts(normalize=True).mul(100).round(2).astype(str) + '%'
    jobs_dataframe = pd.DataFrame({'Counts': count, 'Percent': percent})
    jobs_dataframe.to_csv('data_record/occupation.csv')
    print(pd.DataFrame({'Counts': count, 'Percent': percent}))
    print('--------------------------------')
    break

# 7 - FAMILY ROLE
frole = data["Family Role"]
for column in frole:
    print("Martial status")
    count = frole.value_counts()
    percent = frole.value_counts(normalize=True).mul(100).round(2).astype(str) + '%'
    roles_dataframe = pd.DataFrame({'Counts': count, 'Percent': percent})
    roles_dataframe.to_csv('data_record/family_role.csv')
    print(pd.DataFrame({'Counts': count, 'Percent': percent}))
    print('--------------------------------')
    break

# 8 - RACE
race = data["Race"]
for column in race:
    print("Race")
    count = race.value_counts()
    percent = race.value_counts(normalize=True).mul(100).round(2).astype(str) + '%'
    race_dataframe = pd.DataFrame({'Counts': count, 'Percent': percent})
    race_dataframe.to_csv('data_record/race.csv')
    print(pd.DataFrame({'Counts': count, 'Percent': percent}))
    print('--------------------------------')
    break

# 9 - GENDER
genders = data["Gender"]
for column in race:
    print("Gender")
    count = genders.value_counts()
    percent = genders.value_counts(normalize=True).mul(100).round(2).astype(str) + '%'
    gender_dataframe = pd.DataFrame({'Counts': count, 'Percent': percent})
    gender_dataframe.to_csv('data_record/gender.csv')
    print(pd.DataFrame({'Counts': count, 'Percent': percent}))
    print('--------------------------------')
    break

# 10 - WORKING HOURS
hours = data["Work hours per week"]
for column in hours:
    print("Gender")
    count = hours.value_counts()
    percent = hours.value_counts(normalize=True).mul(100).round(2).astype(str) + '%'
    hour_dataframe = pd.DataFrame({'Counts': count, 'Percent': percent})
    hour_dataframe.to_csv('data_record/working_hour.csv')
    print(pd.DataFrame({'Counts': count, 'Percent': percent}))
    print('--------------------------------')
    break

# 11 - NATIVE COUNTRY
native = data["Native country"]
for column in native:
    print("Native country")
    count = native.value_counts()
    percent = native.value_counts(normalize=True).mul(100).round(2).astype(str) + '%'
    nat_dataframe = pd.DataFrame({'Counts': count, 'Percent': percent})
    nat_dataframe.to_csv('data_record/native_country.csv')
    print(pd.DataFrame({'Counts': count, 'Percent': percent}))
    print('--------------------------------')
    break

#  PROPERTIES
prop = data[["Income", "Saving (Cash)"]]
for column in prop:
    print("Property")
    # props = prop.value_counts().index
    count = prop.value_counts()
    percent = prop.value_counts(normalize=True).mul(100).round(2).astype(str) + '%'
    # 'Properties': props,
    prop_dataframe = pd.DataFrame({'Counts': count, 'Percent': percent})
    prop_dataframe.to_csv('data_record/properties_saving.csv')
    print(pd.DataFrame({'Counts': count, 'Percent': percent}))
    print('--------------------------------')
    break

#  PROPERTIES
pro = data[["Age", "Income", "Saving (Cash)", "Property owner", "Other asset"]]
for column in prop:
    print("Property")
    pros = pro.value_counts().index
    count = pro.value_counts()
    percent = pro.value_counts(normalize=True).mul(100).round(2).astype(str) + '%'
    pro_dataframe = pd.DataFrame({'Counts': count, 'Percent': percent})
    # save to .csv file
    pro_dataframe.to_csv('data_record/properties_extra.csv')
    print(pd.DataFrame({'Counts': count, 'Percent': percent}))
    print('--------------------------------')
    break






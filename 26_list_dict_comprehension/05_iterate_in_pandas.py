import pandas as pd

student_dict = {
    "student": ["Angela", "James", "lily"],
    "score": [56,76,98]
}

#loop through dicts
for (key,value) in student_dict.items():
    print(value)


student_dataframe = pd.DataFrame(student_dict)

#loop through df
for (key,value) in student_dataframe.items():
    print(key)

#loop through rows

for (index, row) in student_dataframe.iterrows():
    if row.student == "Angela":
        print(row.score)

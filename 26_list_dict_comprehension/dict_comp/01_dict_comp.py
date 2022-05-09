#new_dict = {new_key:new_value for item in list}
#new_dict = {new_key:new_value for (key:value) in dict.items()}
#new_dict = {new_key:new_value for (key:value) in dict.items() if test}


import random 
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Fred"]
student_scores = {student:random.randint(1,100) for student in names}

print(student_scores)


passed_students = {name:grade for name,grade in student_scores.items() if grade > 60}

print(passed_students)
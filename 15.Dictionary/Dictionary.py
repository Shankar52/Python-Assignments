dict = {'Student Name': 'Mercy', 'Student Id': 476423, 'Student Course': 'Accounting', 'Student Address':'Hyderabad', 'Student College':'Raghavendra college'}

print(dict)

dict["Student Grade"] = 8.8

print(dict)

dict["Student Name"] = "Shankar"

print(dict)

x = dict["Student Course"]

print(x)

del dict["Student Id"]

print(dict)

students = {1: {'name': 'John', 'age': '27'},
          2: {'name': 'Marie', 'age': '22'}}


print(students)

print(students[1]['name'])

print(students[1]['age'])

print(students.keys())

print(dict.keys())

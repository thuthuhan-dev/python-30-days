# Exercises: Day 8
#1. Create an empty dictionary called dog
dog = {}
#2. Add name, color, breed, legs, age to the dog dictionary
#dog = {'name': 'Bo Phyu', 'color': 'white', 'breed': 'Husky', 'legs': 4, 'age': 3}
dog['name'] = 'Bo Phyu'
dog['color'] = 'white'
dog['breed'] = 'Husky'
dog['legs'] = 4
dog['age'] = 3
print(dog)
#3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {'first_name': 'Thu', 'last_name': 'Thu', 'gender': 'female', 'age': 25, 'marital_status': 'Single', 'skills': ['Python', 'JavaScript'], 'country': 'Finland', 'city': 'Helsinki', 'address': '133 Street'}
print(student)
#4. Get the length of the student dictionary
print(len(student))
#5. Get the value of skills and check the data type, it should be a list
print(student['skills'])
print(type(student['skills']))
#6. Modify the skills values by adding one or two skills
student['skills'].append('React')
student['skills'].append('Node.js')
print(student['skills'])
#7. Get the dictionary keys as a list
keys = list(student.keys())
print(keys)
#8. Get the dictionary values as a list
values = list(student.values())
print(values)
#9. Change the dictionary to a list of tuples using items() method
items = list(student.items()) 
print(items)
#10. Delete one of the items in the dictionary
student.pop('marital_status')
print(student)
print(len(student))
#11. Delete one of the dictionaries
del dog
# print(dog) This will raise a NameError since dog has been deleted
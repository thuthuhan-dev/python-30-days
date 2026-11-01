#Day 2: 30 Days of python programming
first_name = "Thu"
last_name = "Thu Han"
full_name = first_name + " " + last_name
country = "Myanmar"
city = "Mandalay"
age = 21
year = 2026
is_married = False
is_true = True
is_light_on = True
x, y, z = 10, 20, 30

print(type(first_name)) # str
print(type(last_name)) # str
print(type(full_name)) # str
print(type(country)) # str
print(type(city)) # str
print(type(age)) # int
print(type(year)) # int
print(type(is_married)) # bool
print(type(is_true)) # bool
print(type(is_light_on)) # bool
print(type(x)) # int
print(type(y)) # int
print(type(z)) # int

print(len(first_name)) # 3
print(len(first_name) > len(last_name)) # False
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two
print(total, diff, product, division, remainder, exp, floor_division)

radius = 30
area_of_circle = 3.14 * radius ** 2
circum_of_circle = 2 * 3.14 * radius
print(area_of_circle, circum_of_circle)

user_radius = int(input("Enter radius: "))
area = 3.14 * user_radius ** 2
print("Area:", area)

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = int(input("Enter your age: "))

help('keywords')
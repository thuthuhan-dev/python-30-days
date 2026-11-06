# 1. Create an empty tuple
empty_tuple = ()

# 2. Create tuples with sisters and brothers (imaginary siblings are fine)
sisters = ('Mya Mya', 'Hla Hla')
brothers = ('Kyaw Kyaw', 'Zaw Zaw')

# 3. Join them into siblings
siblings = brothers + sisters
print(siblings)

# 4. How many siblings do I have?
num_siblings = len(siblings)
print(num_siblings)   

# 5. Add father and mother (a tuple can't change, so make a new one)
parents = ('U Thaung', 'Daw Myint')
family_members = siblings + parents
print(family_members)

#Level 2
#1. Unpack siblings and parents from family_members
*siblings, father, mother = family_members
print(siblings)   
print(father, mother)

#2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('milk', 'eggs', 'meat')
food_stuff_tp = fruits + vegetables + animal_products
print("Food Stuff:", food_stuff_tp)

#3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print("Food Stuff (List):", food_stuff_lt)

#4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_index = len(food_stuff_tp) // 2
middle_items = food_stuff_tp[middle_index]
print("Middle Item:", middle_items)

#5. Slice out the first three items and the last three items from food_staff_lt list
first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]
print("First Three Items:", first_three_items)
print("Last Three Items:", last_three_items)

#6. Delete the food_staff_tp tuple completely
del food_stuff_tp

#7. Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
if 'Estonia' in nordic_countries:
    print("Estonia is a Nordic country.")
else:
    print("Estonia is not a Nordic country.")
if 'Iceland' in nordic_countries:
    print("Iceland is a Nordic country.")
else:
    print("Iceland is not a Nordic country.")

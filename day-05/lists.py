from countries import countries

# 1. Declare an empty list
empty_list = []

# 2. Declare a list with more than 5 items
my_favourite_things = [
    "Python",
    "Coffee",
    "Books",
    "Music",
    "Technology",
    "Travel",
    "Sleep"
]

# 3. Find the length of your list
print(len(my_favourite_things))

# 4. Get the first, middle and last items
print("First:", my_favourite_things[0])
print("Middle:", my_favourite_things[len(my_favourite_things) // 2])
print("Last:", my_favourite_things[-1])

# 5. Declare mixed_data_types
mixed_data_types = [
    "Thu Thu Han",  # Name
    21,             # Age
    160.5,          # Height (example in cm)
    False,          # Marital status
    "Mandalay"      # Address
]

print(mixed_data_types)

# 6. Declare it_companies
it_companies = [
    "Facebook",
    "Google",
    "Microsoft",
    "Apple",
    "IBM",
    "Oracle",
    "Amazon"
]

# 7. Print the list
print(it_companies)

# 8. Print the number of companies
print(len(it_companies))

# 9. Print first, middle and last companies
print("First:", it_companies[0])
print("Middle:", it_companies[len(it_companies) // 2])
print("Last:", it_companies[-1])

# 10. Modify one company
it_companies[0] = "Meta"
print(it_companies)

# 11. Add an IT company
it_companies.append("Samsung")
print(it_companies)

# 12. Insert an IT company in the middle
middle_index = len(it_companies) // 2
it_companies.insert(middle_index, "Intel")
print(it_companies)

# 13. Change one company to uppercase (IBM excluded)
it_companies[0] = it_companies[0].upper()
print(it_companies)

# 14. Join companies with '#;  '
print("#;  ".join(it_companies))

# 15. Check if a company exists
print("Google" in it_companies)
print("Tesla" in it_companies)

# 16. Sort the list
it_companies.sort()
print(it_companies)

# 17. Reverse the list
it_companies.reverse()
print(it_companies)

# 18. Slice out the first 3 companies
print(it_companies[:3])

# 19. Slice out the last 3 companies
print(it_companies[-3:])

# 20. Slice out the middle IT company or companies
middle_index = len(it_companies) // 2

if len(it_companies) % 2 == 0:
    print(it_companies[middle_index - 1:middle_index + 1])
else:
    print(it_companies[middle_index])

# 21. Remove the first IT company
it_companies.pop(0)
print(it_companies)

# 22. Remove the middle IT company or companies
middle_index = len(it_companies) // 2

if len(it_companies) % 2 == 0:
    del it_companies[middle_index - 1:middle_index + 1]
else:
    del it_companies[middle_index]

print(it_companies)

# 23. Remove the last IT company
it_companies.pop()
print(it_companies)

# 24. Remove all IT companies
it_companies.clear()
print(it_companies)

# 25. Destroy the IT companies list
del it_companies

# Uncommenting the next line will cause a NameError
# print(it_companies)

# 26. Join the following lists
front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]

joined_list = front_end + back_end

print(joined_list)

# 27. Copy the joined list and insert Python and SQL after Redux

full_stack = joined_list.copy()

redux_index = full_stack.index("Redux")
full_stack.insert(redux_index + 1, "Python")
full_stack.insert(redux_index + 2, "SQL")

print(joined_list)   # unchanged, no Python or SQL
print(full_stack)    # has Python and SQL


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()

min_age = min(ages)
max_age = max(ages)

print("Sorted ages:", ages)
print("Minimum age:", min_age)
print("Maximum age:", max_age)

ages.append(min_age)
ages.append(max_age)

print(ages)

ages.sort()

n = len(ages)
middle = n // 2

if n % 2 == 0:
    median_age = (ages[middle - 1] + ages[middle]) / 2
else:
    median_age = ages[middle]

print("Median age:", median_age)

average_age = sum(ages) / len(ages)

print("Average age:", average_age)

age_range = max(ages) - min(ages)

print("Age range:", age_range)

min_average_difference = abs(min(ages) - average_age)
max_average_difference = abs(max(ages) - average_age)

print("Minimum age difference:", min_average_difference)
print("Maximum age difference:", max_average_difference)

print("Are they equal?", min_average_difference == max_average_difference)


# Find the middle country or countries

middle = len(countries) // 2

if len(countries) % 2 == 0:
    print(countries[middle - 1:middle + 1])
else:
    print(countries[middle])

# Divide the countries list into two equal lists.
# If odd, the first half gets one extra country.
middle = (len(countries) + 1) // 2

first_half = countries[:middle]
second_half = countries[middle:]

print("First half:", first_half)
print("Second half:", second_half)

nordic_list = [
    "China",
    "Russia",
    "USA",
    "Finland",
    "Sweden",
    "Norway",
    "Denmark"
]
# Unpack the first three countries and the rest as scandic countries
first_country, second_country, third_country, *scandic_countries = nordic_list

print("First country:", first_country)
print("Second country:", second_country)
print("Third country:", third_country)
print("Scandic countries:", scandic_countries)
# Exercises: Day 7
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


#vExercises: Level 1
#1. Find the length of the set it_companies
print(len(it_companies))

#2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

#3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['LinkedIn', 'Snapchat'])
print(it_companies)
#4. Remove one of the companies from the set it_companies
it_companies.remove('Facebook')
print(it_companies)
#5. What is the difference between remove and discard
print("The 'remove' method will raise a KeyError if the element is not found, while the 'discard' method will not raise an error.")
it_companies.remove('Nokia')     # KeyError: 'Nokia'
it_companies.discard('Nokia')    # not in the set, no error
#Exercises: Level 2
#1. Join A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
C = A.union(B)
print(C)
#2. Find A intersection B
D = A.intersection(B)
print(D)
#3. Is A subset of B
E = A.issubset(B)
print(E)
#4. Are A and B disjoint sets
F = A.isdisjoint(B)
print(F)
#5. Join A with B and B with A
G = A.union(B)
H = B.union(A)
print(G)
print(H)
#6. What is the symmetric difference between A and B
I = A.symmetric_difference(B)
print(I)
#7. Delete the sets completely
del A
del B
#Exercises: Level 3
#1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age)
print("Length of the list:", len(age))
print("Length of the set:", len(age_set))
if len(age) > len(age_set):
    print("The list is bigger.")
else:
    print("The set is bigger.")
#2. Explain the difference between the following data types: string, list, tuple and set
print("A string is an ordered, immutable sequence of characters.")
print("A list is an ordered, mutable sequence of elements.")
print("A tuple is an ordered, immutable sequence of elements.")
print("A set is an unordered, mutable collection of unique elements.")
#3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words)
print("Number of unique words:", len(unique_words))
print("Unique words:", unique_words)
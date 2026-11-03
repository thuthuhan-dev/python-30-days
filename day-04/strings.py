#Day 4 - strings

a = 'Thirty'
b = 'Days'
c = 'Of'
d = 'Python'
challenge = a + ' ' + b + ' ' + c + ' ' + d
print(challenge)

a = 'Coding'
b = 'For'
c = 'All'
print(f"{a} {b} {c}")


company = "Coding For All"
print(company)

print(len(company))

print(company.upper())

print(company.lower())

print(company.capitalize())
print(company.title())
print(company.swapcase())

print(company[7:])

print('Coding' in company)
print(company.index('Coding'))
print(company.find('Coding'))

print(company.replace('Coding', 'Python'))

text = 'Python for Everyone'
print(text.replace('Everyone', 'All'))

print(company.split(' '))

companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(companies.split(', '))

print(company[0])

print(len(company) - 1)

print(repr(company[10]))   

name = 'Python For Everyone'
words = name.split()
acronym = ''.join(word[0] for word in words)
print(acronym)

name = 'Coding For All'
words = name.split()
acronym = words[0][0] + words[1][0] + words[2][0]
print(acronym)

print(company.index('C'))

print(company.index('F'))

text = 'Coding For All People'
print(text.rfind('l'))

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

print(sentence.rindex('because'))

start = sentence.index('because')
end = sentence.index(' is a conjunction')
print(sentence[start:end])

print(sentence.find('because'))

print(sentence[sentence.index('because'):sentence.index(' is a conjunction')])

print(company.startswith('Coding'))

print(company.endswith('coding'))

text = '   Coding For All     '
print(text.strip())

print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = '# '.join(libraries)
print(result)

print('I am enjoying this challenge.\nI just wonder what is next.')

print('Name\t\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

radius = 10
area = 3.14 * radius ** 2

print(f'The area of a circle with radius {radius} is {area:.0f} meters square.')

a = 8
b = 6

print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')
age = 55
height = 5.5
complex_num = 4 - 4j

base = int(input("Enter base: "))
triangle_height = int(input("Enter height: "))
area = 0.5 * base * triangle_height
print("The area of the triangle is:", area)


side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))
perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is:", perimeter)

length = int(input("Enter length: "))
width = int(input("Enter width: "))
area = length * width
print("The area of the rectangle is:", area)
perimeter = 2 * (length + width)
print("The perimeter of the rectangle is:", perimeter)

radius = int(input("Enter radius: "))
pi = 3.14
area = pi * radius * radius
print("The area of the circle is:", area)
circumference = 2 * pi * radius
print("The circumference of the circle is:", circumference)

print("Slope = 2")
print("x-intercept = 1")
print("y-intercept = -2")

x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)
print("The slope of the line is:", slope)
euclidean_distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("The Euclidean distance between the points is:", euclidean_distance)

print(2 == slope)

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x = 0
print("x =", x, "y =", x**2 + 6*x + 9)   # 9
x = -1
print("x =", x, "y =", x**2 + 6*x + 9)   # 4
x = -2
print("x =", x, "y =", x**2 + 6*x + 9)   # 1
x = -3
print("x =", x, "y =", x**2 + 6*x + 9)   # 0
y = x**2 + 6*x + 9
print("When x =", x, ", y =", y)

print(len('python') != len('dragon'))

print('on' in 'python' and 'on' in 'dragon')

print('jargon' in 'I hope this course is not full of jargon')

print('on' not in 'python' and 'on' not in 'dragon')

print(str(float(len('python'))))

print('Even' if int(input("Enter a number: ")) % 2 == 0 else 'Odd')

print(7 // 3 == int(2.7))

print(type('10') == type(10))

print(int(float('9.8')) == 10)

hours = int(input("Enter hours: "))
rate = int(input("Enter rate per hour: "))
print("Your weekly earning is", hours * rate)

year = int(input("Enter number of years you have lived: "))
seconds_lived = year * 365 * 24 * 60 * 60
print("You have lived for", seconds_lived, "seconds.")

for i in range(1, 6):
    print(i, 1, i, i**2, i**3)
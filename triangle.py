import math

# Prompt to input the lengths of the triangle's sides
a = float(input("Please enter the length of side A of the triangle (in meters): "))
b = float(input("Please enter the length of side B of the triangle (in meters): "))
c = float(input("Please enter the length of side C of the triangle (in meters): "))

# Calculate the perimeter of the triangle
perimeter = a + b + c

# Calculate the semi-perimeter
s = perimeter / 2

# Calculate the area of the triangle using Heron's formula
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

# Print the perimeter and area of the triangle with specific formatting
print("The perimeter of the triangle is", f"{perimeter:.1f}m")
print("The area of the triangle is", f"{area:.2f}m^2")

# Check for the type of triangle
if a**2 + b**2 == c**2:
    print("It is a Right Triangle.")
elif a**2 + b**2 > c**2:
    print("It is an Acute Triangle.")
else:
    print("It is an Obtuse Triangle.")

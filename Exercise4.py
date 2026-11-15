# Python Program to find the Area and Circumference of the circle.

# Area of circle is := area = pi * radius²
# circuference of the circle is := 2 *pi * radius

# Area of Circle
import math
radius = float(input("Enter the Radius :"))

area = round(math.pi * (radius *  radius))

print(f"The area of the circle is : {area}")

#Circumference of the circle

rad = float(input("Enter the Radius of cicle :"))

cir = round(2*(math.pi * rad))

print(f"The Circumference of the Circle  is  : {cir}")
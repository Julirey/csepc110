import math
print()
square_side_length = float(input("What is the length of the side of the square in centimeters? "))
square_area = square_side_length * square_side_length
square_area_meters = square_area / 10000
print(f"The area of the square in centimeters squared is: ", square_area)
print(f"The area of the square in meters squared is: ", square_area_meters)
print()

rectangle_side_length = float(input("What is the length of the rectangle in centimeters? "))
rectangle_side_width = float(input("What is the width of the rectangle in centimeters? "))
rarea = rectangle_side_length * rectangle_side_width
rarea_meters = rarea / 10000
print(f"The area of the rectangle in centimeters squared is: ", rarea)
print(f"The area of the rectangle in meters squared is: ", rarea_meters)
print()

clength = float(input("What is the radius of the circle in centimeters? "))
carea = math.pi * clength ** 2
carea_meters = carea / 10000
print(f"The area of the circle in centimeters squared is: ", carea)
print(f"The area of the circle in meters squared is: ", carea_meters)
print()


length = float(input("What is the length? "))
square_area = length * length
print("The area of a square with this length is: ", square_area)
carea = math.pi * length ** 2
print("The area of a circle with this length is: ", carea)
cubevolume = length ** 3
print("The volume of a cube with this length is: ", cubevolume)
fourthirds = 4 / 3
spherevolume = fourthirds * math.pi * length ** 3
print("The volume of a sphere with this length is: ", spherevolume)
print()
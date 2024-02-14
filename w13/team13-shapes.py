import math
shape = ''
area = 0

def compute_area_square(square_length):
    print('(square function)')
    square_area = compute_area_rectangle(square_length, square_length)
    return square_area

def compute_area_rectangle(rectangle_length, rectangle_width):
    print('(rectangle function)')
    rectangle_area = rectangle_length * rectangle_width
    return rectangle_area

def compute_area_circle(circle_radius):
    print('(cicle function)')
    circle_area = math.pi * (circle_radius **2)
    return circle_area

def compute_area(shape, value, value2=0):
    print('area function')
    if shape == 'square':
        area = compute_area_square(value)
    elif shape == 'circle':
        area = compute_area_circle(value)
    elif shape == 'rectangle':
        area = compute_area_rectangle(value, value2)
    return area

while shape != 'quit':
    print()
    shape = input('What shape do you have? ')
    print()

    if shape.lower() == 'square':
        square_input = float(input('What is the length of the side of the square? '))

        square_area = compute_area(shape, square_input)
        print()
        print(f'The area of the square is {square_area}')
        print()

    elif shape.lower() == 'rectangle':
        rectangle_width_input = float(input('What is the width of the rectangle? '))
        rectangle_lenth_input = float(input('What is the length of the rectangle? '))

        rectangle_area = compute_area(shape, rectangle_lenth_input, rectangle_width_input)
        print()
        print(f'The area of the rectangle is {rectangle_area}')
        print()

    elif shape.lower() == 'circle':
        circle_radius_input = float(input('What is the radius of the circle? '))

        circle_area = compute_area(shape, circle_radius_input)
        print()
        print(f'The area of the circle is {circle_area}')
        print()

    elif shape.lower() == 'quit':
        print('Goodbye')
        print()
    else:
        print('Please enter rectangle, square, or circle.')
        print()
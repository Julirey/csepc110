numbers = []
input_number = None
sum = 0
average = 0

print('Enter a list of numbers, type 0 when finished.')

while input_number != 0:
    input_number = int(input('Enter a number: '))
    if input_number != 0:
        numbers.append(input_number)

for number in numbers:
    sum += number

print(f'The sum is: {sum}')

average = sum / len(numbers)
print(f'The average is: {average}')

numbers.sort()
print('The largest number:', numbers[-1])

# The group's solution:
small_number = 9999

print('The sorted list is: ')
for number in numbers:
    if number < small_number and number > 0:
        small_number = number
    print(number)

print(f'The smallest positive number is: {small_number}')

# My solution:
# numbers_positive = []

# for number in numbers: 
#     if number > 0:
#         numbers_positive.append(number)

# print (f'The smallest positive number is: {numbers_positive[0]}')
# word = 'Commitment'

# letter_chosen = input('What letter do you want to highlight? - ')
# for letter in word:
#     if letter.lower() == letter_chosen.lower():
#         print(f'{letter.upper()}', end='')
#     else:
#         print(letter.lower(), end='')

# print()
# letter_chosen = input('What letter do you want to highlight? - ')
# for letter in word:
#     if letter.lower() == letter_chosen.lower():
#         print(f'_', end='')
#     else:
#         print(letter.lower(), end='')

quote = 'In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost.'

repeat = 'yes'
print()
while repeat.lower() == 'yes':
    n = int(input('Please enter a number - '))
    print()
    for i, letter in enumerate(quote):
        if i % n == 0:
            print(f'{letter.upper()}', end='')
        else:
            print(letter.lower(), end='')
    print()
    print()
    repeat = input('Would you like to enter another number? [Yes / No] - ')
    print()
    
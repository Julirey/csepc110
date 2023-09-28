import random

play_again = 'yes'

while play_again.lower() == 'yes':
    number = random.randint(1, 100)

    print()
    #print(f'The magic number is {number}')
    guess = 0
    guess = int(input('What is your guess? '))
    attempts = 1

    while guess != number:
        print()
        if guess > number:
            print('Lower')
        elif guess < number:
            print('Highter')
        print()
        guess = int(input('What is your guess? '))
        attempts = attempts + 1

    print()
    print('You got it!')
    print()
    print(f'Number of attempts: {attempts}')
    print()
    play_again = input('Do you want to play again [Yes or No]? ')
    print()

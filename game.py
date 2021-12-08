# """A number-guessing game."""

import random
def check_if_int(initguess):
    while type(initguess) != "int":
        try:
            x = int(initguess)
        except:
            print(initguess + ' isn\'t a number')
            initguess = input('Your guess?')
        else:
            initguess = int(initguess)
            break
    guess = initguess
    return guess


name = input("Hi, whats your name?")
print('hello,  {name}')
number = random.randint(1,100)
print(number)
print(name + ', I\'m thinking of a number between 1 and 100.')
print('Try to guess my number.')

initguess = input('Your guess?')

guess = check_if_int(initguess)

if guess == number:
    print('Great job, ' + name + '! You got it on the first try')
else:
    if guess < 1 or guess > 100:
        print('Your number is out of range')
    elif(guess > number):
        print('Your guess is too high! Please try again!')
    elif(guess < number):
        print('Your guess is too low! Please try again.')
    guesses = 1
    while(guess != number):
        guess = input('Your guess?')
        guess = check_if_int(guess)

        guesses += 1
        if guess <1 or guess > 100:
            print('Your number is out of range')
        elif guess == number:
            guesses = str(guesses)
            print('Good job, ' + name + '! You found the number in ' + guesses + ' tries!')
        else:
            if(guess > number):
                print('Your guess is too high! Please try again')
            elif(guess < number):
                print('Your guess is too low! Please try again!')

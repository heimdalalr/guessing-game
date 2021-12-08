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
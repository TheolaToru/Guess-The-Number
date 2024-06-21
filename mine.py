from random import choice
import math


def secret_word():
    options = ["flake", "prank", "haste", "cower", "shake", "treat", "sight", "about", "brain", "bread", "cream",
               "crime", "carry", "crowd", "mount", "motor", "chase", "cling", "lower", "loose", "mixed"]
    return choice(options).lower()


def letter_guesser() -> str:
    while True:
        user = input("Enter a letter: ")
        if user.isalpha():
            if len(user) == 0:
                print("Enter valid letter")
            elif len(user) > 1:
                print("Enter only 1 letter")
            else:
                return user.lower()
        else:
            print("Enter valid letter")


def play_again():
    while True:
        select = input("Do you want to play again? Y/N ")
        select = select.upper()
        if select == "Y" or select == "N":
            break
        else:
            print("Enter a valid yours")
    if select == "Y":
        return select
    else:
        print("Goodbye!")
        return


def span():
    while True:
        x, y = input("Enter your minimum range: "), input("Enter maximum range: ")
        if (x.isdigit() and y.isdigit()) and (y > x):
            return x, y
        print("Enter a valid range!")


def number_guesser():
    while True:
        guesses = (input("Enter a number: "))
        if guesses.isdigit():
            return int(guesses)
        else:
            print("Enter valid number")



def word_guesser():
    while True:
        yours = input("Enter your guess: ")
        if yours.isalpha():
            yours = list(yours.lower())
            break
        else:
            print(f"Please enter a valid guess")
    return yours

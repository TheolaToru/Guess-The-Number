from mine import span, number_guesser, play_again
import math
from random import choice


def main():
    print("Welcome! Please enter the range of values") 
    a, b = span()
    tries = round(math.log((int(b) - int(a)), 2))
    correct = choice(range(int(a), int(b)))
    while tries > 0:
        print(f"Tries left = {tries}")
        yours = number_guesser()
        tries = tries - 1
        if yours == correct:
            print("You win!")
            break
        elif yours < correct:
            print("You guessed too low")
        elif yours > correct:
            print("You guessed too high")
    if yours != correct:
        print("You lost! haha skill issue")
    again = play_again()
    if again:
        main()

"""Just checking"""

main()

from random import choice
from mine import letter_guesser, number_guesser


def rps():
    while True:
        user = letter_guesser().upper()
        if user == "R" or user == "P" or user == "S":
            return user
        else:
            print("Enter valid choice")


def main():
    print("Welcome! Enter R for Rock, P for Paper and S for Scissors")
    print("Please set the number of rounds")
    rounds = int(number_guesser())
    actions = ["R", "P", "S"]
    your_count = 0
    comp_count = 0
    inside = []

    while rounds > 0:
        computer = choice(actions)
        yours = rps()
        inside.append(computer)
        inside.append(yours)
        if "R" and "P" in inside:
            if computer == "P":
                comp_count += 1
            else:
                your_count += 1
        elif "R" and "S" in inside:
            if computer == "R":
                comp_count += 1
            else:
                your_count += 1
        elif "S" and "P" in inside:
            if computer == "S":
                comp_count += 1
            else:
                your_count += 1
        elif computer == yours:
            pass
        rounds = rounds - 1
        print(f"Computer played {computer}")
        print(f"You {your_count}-{comp_count} Computer")
    if your_count > comp_count:
        print("You win!")
    else:
        print("Better luck next time! dweeb")


main()

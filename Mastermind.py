from random import choice
from mine import number_guesser


def user():
    while True:
        you = number_guesser()
        if 999 < you < 10000:
            return you
        else:
            print("Enter a 4 digit number")


def play_1():
    computer = (choice(range(1000, 9999)))
    computer_list = list(str(computer))
    print(computer)
    answer = list(str("_" * 4))
    your_tries = 0
    correct = []

    while True:
        your_tries += 1
        yours = user()
        yours_list = list(str(yours))

        if yours_list == computer_list:
            print(" ".join(yours_list))
            print("You are right!")
            return your_tries

        else:
            for i in range(0, 4):
                if yours_list[i] in computer_list:
                    if yours_list[i] == computer_list[i]:
                        answer[i] = yours_list[i]
                        correct.append(yours_list[i])
                        if answer.count(yours_list[i]) > computer_list.count(yours_list[i]):
                            for j in range(0, 4):
                                if answer[j] == yours_list[j]:
                                    continue
                                else:
                                    answer[j] = "_"
                    elif answer.count(yours_list[i]) < computer_list.count(yours_list[i]):
                        answer[i] = yours_list[i]
                else:
                    answer[i] = "_"

            print(" ".join(answer))
            if correct:
                if len(correct) == 1:
                    print(f"{correct[0]} is correct")
                else:
                    together = " and ".join(correct)
                    print(f"{together} are correct")
            correct.clear()

            while True:
                if your_tries >= 5:
                    cont = input("Do you want to keep playing? Y/N ").upper()
                    if cont == "Y":
                        break
                    elif cont == "N":
                        print("You gave up, player 2 wins!")
                        return "F"
                else:
                    break


def play_2():
    you = user()
    your_list = list(str(you))
    print(you)
    answer = list(str("_" * 4))
    comp_tries = 0
    correct = []

    while True:
        comp_tries += 1
        computer = (choice(range(1000, 9999)))
        comp_list = list(str(computer))

        if comp_list == your_list:
            print(" ".join(comp_list))
            print("Comp is right!")
            return comp_tries

        else:
            for i in range(0,4):
                if comp_list[i] in your_list:
                    if comp_list[i] == your_list[i]:
                        answer[i] = comp_list[i]
                        correct.append(comp_list[i])
                        if answer.count(comp_list[i]) > your_list.count(comp_list[i]):
                            for j in range(0,4):
                                if answer[j] == your_list[j]:
                                    continue
                                else:
                                    answer[j] = "_"
                    elif answer.count(comp_list[i]) < your_list.count(comp_list[i]):
                            


def main():
    comp_tries = 0


play_2()
print("Hii")

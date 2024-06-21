from mine import word_guesser, secret_word, play_again


def main():
    print("You have 5 tries to guess the word, goodluck!")
    today_word = secret_word()  # Word to be found
    print(f"The length of the word is {len(today_word)}")
    today = list(today_word.lower())  # Turned the word to a list
    compare = list(today_word.upper())  # Because the final answer list will be in caps
    count = 5  # Number of tries the player will have
    under = ""
    answer = list(str("_" * len(today_word)))  # Initial way the answer looks like

    while count > 0:
        while True:  # Settings for the user input
            guess = word_guesser()
            if len(guess) == len(today_word):
                break
            elif len(guess) > len(today_word):
                print("Too long")
            else:
                print("Too short")

        count = count - 1
        for i in range(0, 5):
            if guess[i] in today:
                if guess[i] == today[i]:
                    answer[i] = guess[i].upper()
                    under = "".join(answer).lower()
                    if under.count(guess[i]) > today.count(guess[i]):
                        for j in range(0, 5):
                            if answer[j] == compare[j]:
                                continue
                            else:
                                answer[j] = "_"
                elif under.count(guess[i]) < today.count(guess[i]):
                    answer[i] = guess[i]
            else:
                answer[i] = "_"
        if answer == compare:
            break
        else:
            output = " ".join(answer)
            print(output)

        print(f"You have {count} chance(s) left")

    output = " ".join(answer)
    if answer == compare:
        print(output)
        print(f"Congratulations, you got the word of today: {today_word}! in {5 - count} round(s)")
    else:
        print(f"Unfortunately you were wrong, the word of today is {today_word}!")
    again = play_again()
    if again:
        main()


main()

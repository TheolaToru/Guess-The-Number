import mine


def main():
    word = mine.secret_word()
    word_list = list(word)
    correct = list(word.upper())
    answer = str("_" * len(word))
    answer_list = list(answer)
    tries = len(word) + 2

    while tries > 0:
        guess = mine.letter_guesser()
        tries = tries - 1
        for i in range(len(word_list)):
            if guess == word_list[i]:
                answer_list[i] = guess.upper()
        output = " ".join(answer_list)
        print(output)
        if answer_list == correct:
            print("You win!")
            break
    if answer != correct:
        print(f"Better luck next time! The word was {word.upper()}, dweeb")
    again = mine.play_again()
    if again:
        main()


main()

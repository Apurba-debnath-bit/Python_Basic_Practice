n = 18
numberOfGuess = 1
numberOfGuessTotal = 9

while numberOfGuess <= numberOfGuessTotal:
    guess_number = int(input("Guess the number: "))
    print("Number of guess you took: ", numberOfGuess)
    if guess_number > n:
        print("Sorry!! Largest number, plz enter again\n")
    elif guess_number < n:
        print("Sorry!! smallest number, plz enter again\n")
    elif guess_number == n:
        print("You win.\n")
        break

    numberOfGuess = numberOfGuess + 1


print("Game over")
print(f"No_of_total_guess_taken: {numberOfGuessTotal}" )
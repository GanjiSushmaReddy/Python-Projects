import random
randNo = random.randint(1,100)
# print(randNo)
guessNo = 0

userGuess=""
while userGuess != randNo:
    userGuess = int(input("Enter your guess: "))
    guessNo =guessNo+1

    if userGuess == randNo:
        print(f"Correct guess is {userGuess}")
        print(f"You gussed correctly in {guessNo} guesses.")
    else:
        if userGuess<randNo:
            print("you guessed wrong, Higher no. please")
        elif userGuess>randNo:
            print("You guessed wrong, Lower no. please")

with open("guesses.txt","w") as f:
    f.write(str(guessNo))




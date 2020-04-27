import random

#Function that capitalize the name entered if it is not
def cap(name):
    if name != name.title():
        capi = name.title()
        return capi
    else:
        return name

def worddic():
    word = random.choice(["dog", "cat", "cow", "horse", "pokemon", "banana", "avocado", "tiger", "orange", "avengers"])
    validLetters = 'abcdefghijklmnopqrstuvwxyzABCEDFGHIJKLMNSOPQRSTUVWXYZ'
    guessMade = ''
    count = 0
    while len(word) > 0:
        main = ""
        for letter in word:
            if letter in guessMade:
                main = main + letter
            else:
                main = main + "_" + " "

        if main == word:
            print ("The word was: ", main)
            print("Congratulations, you won the game!")
            break
        print("Guess the word: ", main)
        print("Enter guess: ")
        guess = input()

        if guess in validLetters:
            converUpper = guess.lower()
            print("Good guess")
            guessMade = guessMade + converUpper

        while guess not in validLetters:
            print("Enter a valid character!")
            guess = input()
        guessMade = guessMade + guess

        if guess.lower() not in word:
            count = count + 1
            if count == 1:
                print("WRONG!")
                print("   O   ")
            if count == 2:
                print("WRONG!")
                print("   O  ")
                print("   |  ")
            if count == 3:
                print("WRONG!")
                print("   O  ")
                print("   |  ")
                print("  /   ")
            if count == 4:
                print("WRONG!")
                print("   O  ")
                print("   |  ")
                print("  / \ ")
            if count == 5:
                print("WRONG!")
                print(" \ O  ")
                print("   |  ")
                print("  / \ ")
            if count == 6:
                print("WRONG!")
                print(" \ O /")
                print("   |  ")
                print("  / \ ")
            if count == 7:
                print("WRONG!")
                print(" \ O|/")
                print("   |  ")
                print("  / \ ")
            if count == 8:
                print("WRONG!")
                print(" \ O_|/")
                print("   |   ")
                print("  / \  ")
            if count == 8:
                print("WRONG! Last chance")
                print(" \ O_||/")
                print("   |   ")
                print("  / \  ")
            if count == 9:
                print("WRONG! A kind man just die!")
                print("   O_||")
                print(" / | \  ")
                print("  / \  ")
                print("The word wanted was:", word)
                print("Better luck next time")
                break
name = input("Enter your name: ")
print("Welcome,", cap(name))
print("Les't play Hangman!")
print("----------------------------------------")
print("Guess the word before the man is hanged.")
print("----------------------------------------")
worddic()

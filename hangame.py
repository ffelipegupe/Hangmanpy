import random
import requests


#Function that capitalize the name entered if it is not
def cap(name):
    if name != name.title():
        capi = name.title()
        return capi
    else:
        return name

def worddic():
    word = requests.get("https://random-word-api.herokuapp.com/word?lang=en").json()[0]
    #word = random.choice(["dog", "cat", "cow", "horse", "pokemon", "banana", "avocado", "tiger", "orange", "avengers"])
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
            print("----------------------------------------")
            print ("The word was: * " +  main + " *")
            print("Congratulations, you won the game!")
            print("----------------------------------------")
            break
        print("Guess the word: ", main)
        print("Enter guess: ")
        guess = input()

        if guess in validLetters and guess in word:
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
                print("----------------------------------------")
                print("WRONG!")
                print("   O   ")
                print("----------------------------------------")
            if count == 2:
                print("----------------------------------------")
                print("WRONG!")
                print("   O  ")
                print("   |  ")
                print("----------------------------------------")
            if count == 3:
                print("----------------------------------------")
                print("WRONG!")
                print("   O  ")
                print("   |  ")
                print("  /   ")
                print("----------------------------------------")
            if count == 4:
                print("----------------------------------------")
                print("WRONG!")
                print("   O  ")
                print("   |  ")
                print("  / \ ")
                print("----------------------------------------")
            if count == 5:
                print("----------------------------------------")
                print("WRONG!")
                print(" \ O  ")
                print("   |  ")
                print("  / \ ")
                print("----------------------------------------")
            if count == 6:
                print("----------------------------------------")
                print("WRONG!")
                print(" \ O /")
                print("   |  ")
                print("  / \ ")
                print("----------------------------------------")
            if count == 7:
                print("----------------------------------------")
                print("WRONG!")
                print(" \ O|/")
                print("   |  ")
                print("  / \ ")
                print("----------------------------------------")
            if count == 8:
                print("----------------------------------------")
                print("WRONG!")
                print(" \ O_|/")
                print("   |   ")
                print("  / \  ")
                print("----------------------------------------")
            if count == 8:
                print("----------------------------------------")
                print("WRONG! Last chance")
                print(" \ O_||/")
                print("   |   ")
                print("  / \  ")
                print("----------------------------------------")
            if count == 9:
                print("----------------------------------------")
                print("WRONG! A kind man just die!")
                print("   O_||")
                print(" / | \  ")
                print("  / \  ")
                print("The word wanted was:", word)
                print("Better luck next time")
                print("----------------------------------------")
                break
name = input("Enter your name: ")
print("---")
print("Welcome,", cap(name))
print("Les't play Hangman!")
print("----------------------------------------")
print("Guess the word before the man is hanged.")
print("----------------------------------------")
print("----------------------------------------")
worddic()

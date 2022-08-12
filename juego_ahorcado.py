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
    word = requests.get("https://random-word-api.herokuapp.com/word?lang=es").json()[0]
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
            print ("La palabra era: * " +  main + " *")
            print("Felicitationces, ¡Ganaste el juego!")
            print("----------------------------------------")
            break
        print("Adivina la palabra: ", main)
        print("                      ")
        print("Ingresa un caracter: ")
        guess = input()

        if guess in validLetters and guess in word:
            converUpper = guess.lower()
            print("¡Buen intento!")
            guessMade = guessMade + converUpper

        while guess not in validLetters:
            print("¡Escribe un caracter válido!")
            guess = input()
        guessMade = guessMade + guess

        if guess.lower() not in word:
            count = count + 1
            if count == 1:
                print("----------------------------------------")
                print("¡ERROR!")
                print("   O   ")
                print("----------------------------------------")
            if count == 2:
                print("----------------------------------------")
                print("¡ERROR!")
                print("   O  ")
                print("   |  ")
                print("----------------------------------------")
            if count == 3:
                print("----------------------------------------")
                print("¡ERROR!")
                print("   O  ")
                print("   |  ")
                print("  /   ")
                print("----------------------------------------")
            if count == 4:
                print("----------------------------------------")
                print("¡ERROR!")
                print("   O  ")
                print("   |  ")
                print("  / \ ")
                print("----------------------------------------")
            if count == 5:
                print("----------------------------------------")
                print("¡ERROR!")
                print(" \ O  ")
                print("   |  ")
                print("  / \ ")
                print("----------------------------------------")
            if count == 6:
                print("----------------------------------------")
                print("¡ERROR!")
                print(" \ O /")
                print("   |  ")
                print("  / \ ")
                print("----------------------------------------")
            if count == 7:
                print("----------------------------------------")
                print("¡ERROR!")
                print(" \ O|/")
                print("   |  ")
                print("  / \ ")
                print("----------------------------------------")
            if count == 8:
                print("----------------------------------------")
                print("¡ERROR!")
                print(" \ O_|/")
                print("   |   ")
                print("  / \  ")
                print("----------------------------------------")
            if count == 8:
                print("----------------------------------------")
                print("¡ERROR! Last chance")
                print(" \ O_||/")
                print("   |   ")
                print("  / \  ")
                print("----------------------------------------")
            if count == 9:
                print("----------------------------------------")
                print("¡ERROR! Acabas de morir")
                print("   O_||")
                print(" / | \  ")
                print("  / \  ")
                print("La palabra buscada era:", word)
                print("Más suerte la próxima vez")
                print("----------------------------------------")
                break
name = input("Escribe tu nombre: ")
print("---")
print("Bienvenido,", cap(name))
print("¡Juguemos al ahoracado!")
print("----------------------------------------")
print("Adivina la palabra antes de que te ahorquen")
print("----------------------------------------")
print("----------------------------------------")
worddic()
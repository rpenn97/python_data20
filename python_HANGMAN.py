from hangman_words import word_list
import random

def word():
    word = random.choice(word_list).lower()
    temp = []
    badtemp = []
    life = 10
    print (word)
    cont = True
    while cont is True and life > 0:
        ask = input("Guess a letter")
        if ask.lower() not in word:
            life = life - 1
            badtemp.append(ask)
            print(f"Nope! {life} lives remaining")
        else:
            temp.append(ask)
            print(f"Yes! {life} lives remaining")
        if len(set(word)) == len(set(temp)):
            print(f"game won! the word was {word}")
            break
    else:
        cont = False
        print('Game over')
    return temp

print(word())




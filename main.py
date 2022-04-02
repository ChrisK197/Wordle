from termcolor import *
import colorama
import sys
from english_words import english_words_lower_alpha_set
from datetime import date
import random

def getWordList():
    list = []
    for i in english_words_lower_alpha_set:
        if len(i) == 5:
            list.append(i)
    return sorted(list)

def getScore(str, word):
    score = ""
    letters = []
    for i in word:
        letters.append(i)

    for i in range(len(str)):
        if str[i] == word[i]:
            score += (colored(str[i], "green"))
            letters.remove(str[i])
        elif str[i] in letters:
            score += (colored(str[i], "yellow"))
            if str[i] in letters:
                letters.remove(str[i])
        else:
            score += str[i]
    return score

def getWord(list):
    today = str(date.today())
    string = ""
    for i in today:
        if i != "-":
            string += i
    random.seed(string)
    word = list[random.randint(0, len(list)-1)]
    return word

def main():
    list = getWordList()
    word = getWord(list)
    print("Input your first guess")
    for i in range(0, 5):
        print("Guess " + str(i+1) + ": ")
        guess = input()
        while len(guess) != 5:
            print("Improper number of letters. Try guess " + str(i+1) + " again: ")
            guess = input()
        while guess not in list:
            print("Not a word. Try guess " + str(i + 1) + " again: ")
            guess = input()
        print(getScore(guess, word))
        if guess == word:
            print("Congrats!")
            break
        elif i == 4:
            print("The word was: " + word)

if __name__ == '__main__':
    sys.exit(main())
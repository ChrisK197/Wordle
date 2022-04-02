from termcolor import *
import colorama
import sys
from english_words import english_words_lower_alpha_set
from datetime import date
import random

skip = 0

def getWordList():
    list = []
    for i in english_words_lower_alpha_set:
        if len(i) == 5:
            list.append(i)
    return sorted(list)

def getScore(str, word):
    score = ""
    scoreU = ""
    letters = []
    for i in word:
        letters.append(i)

    for i in range(len(str)):
        if str[i] == word[i]:
            score += (colored(str[i], "green"))
            scoreU += str[i]
            if str[i] not in letters:
                for j in range(len(scoreU)):
                    print(j)
                    if scoreU[j] == str[i]:
                        score = 1
                        return getScore(str, word)
        elif str[i] in letters and score == 0:
            score += (colored(str[i], "yellow"))
            scoreU += str[i]
            if str[i] in letters:
                letters.remove(str[i])
        else:
            score += str[i]
            scoreU += str[i]
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
        score = 0
        if guess == word:
            print("Congrats!")
            break
        elif i == 4:
            print("The word was: " + word)

if __name__ == '__main__':
    sys.exit(main())
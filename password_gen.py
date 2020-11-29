import pandas as pd
import random
import sys, getopt

def main(argv):

    main.numberDiceRolls = ""

    try:
        opts, arg = getopt.getopt(argv,"hn:", ["help", "number="])
    except getopt.GetoptError:
        print("Error!")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("Please run as: password_gen.py -n 4\n")
            print("If you do not specify the number of words via -n the default number will run")
            sys.exit()
        elif opt in ("-n", "--number"):
            main.numberDiceRolls = int(arg)

def randRoll():

    systemRandom = random.SystemRandom()

    diceRoll_1 = systemRandom.randint(1,6)
    diceRoll_2 = systemRandom.randint(1,6)
    diceRoll_3 = systemRandom.randint(1,6)
    diceRoll_4 = systemRandom.randint(1,6)
    diceRoll_5 = systemRandom.randint(1,6)

    diceRoll = diceRoll_1, diceRoll_2, diceRoll_3, diceRoll_4, diceRoll_5
    randRoll.diceRoll = int("".join(map(str, diceRoll)))

def genRandWords():
    if main.numberDiceRolls == "":
        numberOfRolls = 4
    else:
        numberOfRolls = main.numberDiceRolls

    wordArray = []

    for rolls in range(numberOfRolls):
        randRoll()
        wordlist = pd.read_csv('eff_large_wordlist.txt', sep="\t")
        for row in wordlist.index:
            if wordlist["Dice"][row] == randRoll.diceRoll:
                word = wordlist["Word"][row].capitalize()
                wordArray.append(word)
    print(str("".join(map(str, wordArray))))

#userInput()
#genRandWords()

if __name__ == "__main__":
    main(sys.argv[1:])
    genRandWords()
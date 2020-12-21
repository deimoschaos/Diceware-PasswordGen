import pandas as pd
import secrets
import sys, getopt
import argparse

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('-n', '--number', type=int, default=4, help="This sets the number of words. If not used default number is 4.")
    parser.add_argument('-s', '--source', type=str, default="eff_large_wordlist.txt", choices=["eff", "heartsucker"], help="This sets which word list is used. Use 'eff' or 'heartsucker'. EFF is the default used.")

    args = parser.parse_args()

    main.numberOfRolls = args.number

    main.sourceList = args.source

    if args.source == 'eff':
        main.sourceList = 'eff_large_wordlist.txt'
    elif args.source == 'heartsucker':
        main.sourceList = 'heartsucker-wordlist.txt'

def randRoll():

    secretRandom = secrets.SystemRandom()

    diceRoll_1 = secretRandom.randint(1,6)
    diceRoll_2 = secretRandom.randint(1,6)
    diceRoll_3 = secretRandom.randint(1,6)
    diceRoll_4 = secretRandom.randint(1,6)
    diceRoll_5 = secretRandom.randint(1,6)

    diceRoll = diceRoll_1, diceRoll_2, diceRoll_3, diceRoll_4, diceRoll_5
    randRoll.diceRoll = int("".join(map(str, diceRoll)))
    print(randRoll.diceRoll)

def genRandWords():
        
    wordArray = []

    for rolls in range(main.numberOfRolls):
        randRoll()
        wordlist = pd.read_csv(main.sourceList, sep="\t")
        for row in wordlist.index:
            if wordlist["Dice"][row] == randRoll.diceRoll:
                word = wordlist["Word"][row].capitalize()
                wordArray.append(word)
    print(str("".join(map(str, wordArray))))

#userInput()
#genRandWords()

if __name__ == "__main__":
    main()
    genRandWords()
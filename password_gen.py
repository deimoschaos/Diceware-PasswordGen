import pandas as pd
import secrets
import argparse
import string
import random

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

def genRandLetters():

    secretRandom = secrets.SystemRandom()

    ascii_lowercase = string.ascii_lowercase
    ascii_uppercase = string.ascii_uppercase
    ascii_digits = string.digits
    ascii_punctuation = string.punctuation
    uppercase_count = 2
    digits_count = 2
    punctuation_count = 2
    special_count = uppercase_count + digits_count + punctuation_count
    lowercase_count = 16 - special_count
    x = 0
    lowercase_total = (''.join(secrets.choice(ascii_lowercase) for i in range(lowercase_count)))
    uppercase_total = (''.join(secrets.choice(ascii_uppercase) for i in range(digits_count)))
    digit_total = (''.join(secrets.choice(ascii_digits) for i in range(digits_count)))
    puncuation_total = (''.join(secrets.choice(ascii_punctuation) for i in range(punctuation_count)))

    random_password = lowercase_total + uppercase_total + digit_total + puncuation_total
    random_password_array = []
    random_password_count = len(random_password)
    for i in random_password:
        #temp = [i]
        random_password_array.append(i)

    random_password = (secretRandom.sample(random_password_array, len(random_password_array)))
    print(str("".join(map(str, random_password))))
    #random_password = secretRandom.shuffle(random_password_array)
    #print(random_password)
    #while x < y:
    #    print(secrets.choice(ascii_lowercase))
    #    x += 1

#userInput()
#genRandWords()

if __name__ == "__main__":
    main()
    genRandWords()
    genRandLetters()
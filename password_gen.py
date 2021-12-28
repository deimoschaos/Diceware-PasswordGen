import pandas as pd
import secrets
import argparse
import string
import random

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('-r', '--random', action="store_true", help="This sets the password generator to generate random letters, digits, and characters.")
    parser.add_argument('-w', '--wordlist', action="store_true", help="This sets the password generator to generate random words from a word list.")
    parser.add_argument('-n', '--number', type=int, default=4, help="This sets the number of words. If not used default number is 4.")
    parser.add_argument('-s', '--source', type=str, default="eff_large_wordlist.txt", choices=["eff", "heartsucker"], help="This sets which word list is used. Use 'eff' or 'heartsucker'. EFF is the default used.")
    parser.add_argument('-u', '--uppercase', type=int, default=2, help="This sets the uppercase count of the random letter password. Default is 2")
    parser.add_argument('-d', '--digits', type=int, default=2, help="This sets the digit count of the random letter password. Defualt is 2.")
    parser.add_argument('-p', '--special', type=int, default=2, help="This sets the special count of the random letter password. Default is 2.")
    parser.add_argument('-t', '--total', type=int, default=16, help="This sets the total count of the random letter password. Defualt is 16")
    
    args = parser.parse_args()

    main.setrandom = args.random
    main.setwordlist = args.wordlist

    main.numberOfRolls = args.number
    main.sourceList = args.source
    if args.source == 'eff':
        main.sourceList = 'eff_large_wordlist.txt'
    elif args.source == 'heartsucker':
        main.sourceList = 'heartsucker-wordlist.txt'

    main.uppercase = args.uppercase
    main.digits = args.digits
    main.special = args.special
    main.total = args.total

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
    ascii_special = string.punctuation
    uppercase_count = main.uppercase
    digits_count = main.digits
    special_count = main.special
    special_count = uppercase_count + digits_count + special_count
    lowercase_count = main.total - special_count
    x = 0
    lowercase_total = (''.join(secrets.choice(ascii_lowercase) for i in range(lowercase_count)))
    uppercase_total = (''.join(secrets.choice(ascii_uppercase) for i in range(digits_count)))
    digit_total = (''.join(secrets.choice(ascii_digits) for i in range(digits_count)))
    special_total = (''.join(secrets.choice(ascii_special) for i in range(special_count)))

    random_password = lowercase_total + uppercase_total + digit_total + special_total
    random_password_array = []
    random_password_count = len(random_password)
    for i in random_password:
        #temp = [i]
        random_password_array.append(i)

    random_password = (secretRandom.sample(random_password_array, len(random_password_array)))
    print(str("".join(map(str, random_password))))

if __name__ == "__main__":
    main()
    if main.setwordlist:
        genRandWords()
    if main.setrandom:
        genRandLetters()
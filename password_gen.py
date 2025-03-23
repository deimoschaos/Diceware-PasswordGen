import pandas as pd
import secrets
import argparse
import string
import random
import tkinter as tk
from tkinter import ttk, messagebox

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
    password = str("".join(map(str, wordArray)))
    return password

def genRandLetters():
    secretRandom = secrets.SystemRandom()

    ascii_lowercase = string.ascii_lowercase
    ascii_uppercase = string.ascii_uppercase
    ascii_digits = string.digits
    ascii_special = string.punctuation
    uppercase_count = main.uppercase
    digits_count = main.digits
    special_count = main.special
    lowercase_count = main.total - (uppercase_count + digits_count + special_count)

    lowercase_total = ''.join(secrets.choice(ascii_lowercase) for _ in range(lowercase_count))
    uppercase_total = ''.join(secrets.choice(ascii_uppercase) for _ in range(uppercase_count))
    digit_total = ''.join(secrets.choice(ascii_digits) for _ in range(digits_count))
    special_total = ''.join(secrets.choice(ascii_special) for _ in range(special_count))

    random_password = lowercase_total + uppercase_total + digit_total + special_total
    random_password_array = list(random_password)
    random_password = ''.join(secretRandom.sample(random_password_array, len(random_password_array)))
    return random_password

def generate_password():
    if main.setwordlist:
        return genRandWords()
    if main.setrandom:
        return genRandLetters()

def genUsername():
    secretRandom = secrets.SystemRandom()
    wordlist = pd.read_csv(main.sourceList, sep="\t")
    adjective = wordlist["Word"][secretRandom.randint(0, len(wordlist) - 1)].capitalize()
    noun = wordlist["Word"][secretRandom.randint(0, len(wordlist) - 1)].capitalize()
    number = secretRandom.randint(1, 9999)
    username = f"{adjective}{noun}{number}"
    return username

def create_gui():
    root = tk.Tk()
    root.title("Password and Username Generator")

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    option_var = tk.StringVar(value="random")
    number_var = tk.IntVar(value=4)
    source_var = tk.StringVar(value="eff")
    uppercase_var = tk.IntVar(value=2)
    digits_var = tk.IntVar(value=2)
    special_var = tk.IntVar(value=2)
    total_var = tk.IntVar(value=16)
    password_var = tk.StringVar()
    username_var = tk.StringVar()

    def copy_password_to_clipboard():
        root.clipboard_clear()
        root.clipboard_append(password_var.get())
        messagebox.showinfo("Copied", "Password copied to clipboard")

    def copy_username_to_clipboard():
        root.clipboard_clear()
        root.clipboard_append(username_var.get())
        messagebox.showinfo("Copied", "Username copied to clipboard")

    def update_options(*args):
        if option_var.get() == "random":
            number_entry.grid_remove()
            source_combobox.grid_remove()
            uppercase_entry.grid()
            digits_entry.grid()
            special_entry.grid()
            total_entry.grid()
        elif option_var.get() == "wordlist":
            number_entry.grid()
            source_combobox.grid()
            uppercase_entry.grid_remove()
            digits_entry.grid_remove()
            special_entry.grid_remove()
            total_entry.grid_remove()
        else:
            number_entry.grid_remove()
            source_combobox.grid_remove()
            uppercase_entry.grid_remove()
            digits_entry.grid_remove()
            special_entry.grid_remove()
            total_entry.grid_remove()

    ttk.Radiobutton(frame, text="Random", variable=option_var, value="random").grid(row=0, column=0, sticky=tk.W)
    ttk.Radiobutton(frame, text="Wordlist", variable=option_var, value="wordlist").grid(row=1, column=0, sticky=tk.W)
    ttk.Radiobutton(frame, text="Username Only", variable=option_var, value="username").grid(row=2, column=0, sticky=tk.W)
    ttk.Label(frame, text="Number of words:").grid(row=3, column=0, sticky=tk.W)
    number_entry = ttk.Entry(frame, textvariable=number_var)
    number_entry.grid(row=3, column=1, sticky=(tk.W, tk.E))
    ttk.Label(frame, text="Source:").grid(row=4, column=0, sticky=tk.W)
    source_combobox = ttk.Combobox(frame, textvariable=source_var, values=["eff", "heartsucker"])
    source_combobox.grid(row=4, column=1, sticky=(tk.W, tk.E))
    ttk.Label(frame, text="Uppercase count:").grid(row=5, column=0, sticky=tk.W)
    uppercase_entry = ttk.Entry(frame, textvariable=uppercase_var)
    uppercase_entry.grid(row=5, column=1, sticky=(tk.W, tk.E))
    ttk.Label(frame, text="Digits count:").grid(row=6, column=0, sticky=tk.W)
    digits_entry = ttk.Entry(frame, textvariable=digits_var)
    digits_entry.grid(row=6, column=1, sticky=(tk.W, tk.E))
    ttk.Label(frame, text="Special count:").grid(row=7, column=0, sticky=tk.W)
    special_entry = ttk.Entry(frame, textvariable=special_var)
    special_entry.grid(row=7, column=1, sticky=(tk.W, tk.E))
    ttk.Label(frame, text="Total count:").grid(row=8, column=0, sticky=tk.W)
    total_entry = ttk.Entry(frame, textvariable=total_var)
    total_entry.grid(row=8, column=1, sticky=(tk.W, tk.E))
    ttk.Label(frame, text="Generated Password:").grid(row=9, column=0, sticky=tk.W)
    password_entry = ttk.Entry(frame, textvariable=password_var, state='readonly', width=50)
    password_entry.grid(row=9, column=1, sticky=(tk.W, tk.E))
    ttk.Button(frame, text="Copy", command=copy_password_to_clipboard).grid(row=9, column=2, sticky=tk.W)
    ttk.Label(frame, text="Generated Username:").grid(row=10, column=0, sticky=tk.W)
    username_entry = ttk.Entry(frame, textvariable=username_var, state='readonly', width=50)
    username_entry.grid(row=10, column=1, sticky=(tk.W, tk.E))
    ttk.Button(frame, text="Copy", command=copy_username_to_clipboard).grid(row=10, column=2, sticky=tk.W)

    option_var.trace_add('write', update_options)
    update_options()

    def on_generate():
        main.sourceList = source_var.get()
        if main.sourceList == 'eff':
            main.sourceList = 'eff_large_wordlist.txt'
        elif main.sourceList == 'heartsucker':
            main.sourceList = 'heartsucker-wordlist.txt'
        
        if option_var.get() == "username":
            username = genUsername()
            username_var.set(username)
            password_var.set("")
        else:
            main.setrandom = option_var.get() == "random"
            main.setwordlist = option_var.get() == "wordlist"
            main.numberOfRolls = number_var.get()
            main.uppercase = uppercase_var.get()
            main.digits = digits_var.get()
            main.special = special_var.get()
            main.total = total_var.get()
            password = generate_password()
            password_var.set(password)
            username_var.set("")

    ttk.Button(frame, text="Generate", command=on_generate).grid(row=11, column=1, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        main()
    else:
        create_gui()
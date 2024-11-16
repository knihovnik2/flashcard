#!/usr/bin/env python3
import argparse
from colorama import Fore, Back, Style
import time
from random import randint as ri
import os

def practice(file_name):
    f = open(f"{os.path.dirname(os.path.abspath(__file__))}/files/{file_name}.txt")
    entry = ""
    for i in f:
        for j in i:
            if j != "\n":
                entry += j
    
    cards = []
    for i in entry.split(";"):
        cards.append(i.split(","))
    print(cards[0][0])
    cards.pop(0)
    cards.pop()
    
    stats = {"correct": 0, "total": 0}

    if config["limit"] == 0:
        config["limit"] = len(cards)

    start = time.time()
    for i in range(config["limit"]):
        current = cards.pop(ri(0,len(cards)-1))
        stats["total"] += 1

        if current[0][-1] == "?":
            answer = input(f"{current[0]} ")
        else:
            answer = input(f"{current[0]}: ")

        if answer[0] == ";":
            stats["correct"] += 1
            print(f"{Fore.YELLOW}*preklep corrected*{Style.RESET_ALL}")
            if answer.lower()[1:] == current[1].lower():
                print(f"{Fore.GREEN}correct!{Style.RESET_ALL}")
                stats["correct"] += 1
            else:
                print(f"{Fore.RED}wrong :({Style.RESET_ALL} the correct answer was {Fore.CYAN}{current[1]}{Style.RESET_ALL}")
        else:
            if answer.lower() == current[1].lower():
                print(f"{Fore.GREEN}correct!{Style.RESET_ALL}")
                stats["correct"] += 1
            else:
                print(f"{Fore.RED}wrong :({Style.RESET_ALL} the correct answer was {Fore.CYAN}{current[1]}{Style.RESET_ALL}")
    
    print(f"{Fore.MAGENTA}Score:{Style.RESET_ALL} {stats["correct"]}/{stats["total"]} {round(stats["correct"]/stats["total"]*100,2)}% {round(time.time()-start, 2)} s")

def choice(file_name):
    f = open(f"{os.path.dirname(os.path.abspath(__file__))}/files/{file_name}.txt")
    entry = ""
    for i in f:
        for j in i:
            if j != "\n":
                entry += j
    
    cards = []
    for i in entry.split(";"):
        cards.append(i.split(","))
    print(cards[0][0])
    cards.pop(0)
    cards.pop()
    
    stats = {"correct": 0, "total": 0}

    if config["limit"] == 0:
        config["limit"] = len(cards)

    start = time.time()
    for i in range(config["limit"]):
        current = cards.pop(ri(0,len(cards)-1))
        stats["total"] += 1
        
        letters = config["quiz_option_markers"]

        print(current[1])
        for i in range(int(current[0])):
            print(f"{letters[i]}) {current[i+2]}")
        
        answer = input("Answer: ")

        if answer.lower() == letters[int(current[-1])]:
            print(f"{Fore.GREEN}correct!{Style.RESET_ALL}")
            stats["correct"] += 1
        else:
            print(f"{Fore.RED}wrong :({Style.RESET_ALL} the correct answer was {Fore.CYAN}{letters[int(current[-1])]}){Style.RESET_ALL}")
    
    print(f"{Fore.MAGENTA}Score:{Style.RESET_ALL} {stats["correct"]}/{stats["total"]} {round(stats["correct"]/stats["total"]*100,2)}% {round(time.time()-start, 2)} s")



def main():
    parser = argparse.ArgumentParser(description="Command Line Flashcard Tool")
    
    # Adding a positional argument 'command'
    parser.add_argument("command", choices=["practice", "choice", "abcd"], help="The command to execute")
    
    # Adding a positional argument for the file name
    parser.add_argument("file", type=str, help="The name of the file")
    
    # Allows you to set a limit on how many you want to practice
    parser.add_argument("--limit", type=int, default=0, help="Limit of flashcards shown")

    # Parse the arguments
    args = parser.parse_args()

    # Load config
    config_file = open(f"{os.path.dirname(os.path.abspath(__file__))}/flashcard.config")
    config_read = [i for i in config_file]
    global config
    config = {}
    for i in config_read:
        config[i.split("=")[0]] = i.split("=")[1]
    config["limit"] = args.limit
    
    # Handle the command
    if args.command == "practice":
        input_file = ""

        for i in args.file.lower():
            if i == " ":
                input_file += "_"
            else:
                input_file += i

        practice(input_file)
    
    elif args.command == "choice" or args.command == "abcd":
        input_file = ""

        for i in args.file.lower():
            if i == " ":
                input_file += "_"
            else:
                input_file += i

        choice(input_file)
    

if __name__ == "__main__":
    main()
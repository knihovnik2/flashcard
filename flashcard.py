#!/usr/bin/env python3
import argparse
from colorama import Fore, Back, Style
import time
from random import randint as ri

def practice(file_name):
    f = open(f"/home/lukas/Apps/Flashcards/{file_name}.txt")
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
    
    stats = {"correct": 0, "total": len(cards)}

    start = time.time()
    for i in range(len(cards)):
        current = cards.pop(ri(0,len(cards)-1))

        if current[0][-1] == "?":
            answer = input(f"{current[0]} ")
        else:
            answer = input(f"{current[0]}: ")

        if answer.lower() == current[1].lower():
            print(f"{Fore.GREEN}correct!{Style.RESET_ALL}")
            stats["correct"] += 1
        else:
            print(f"{Fore.RED}wrong :({Style.RESET_ALL} the correct answer was {Fore.CYAN}{current[1]}{Style.RESET_ALL}")
    
    print(f"{Fore.MAGENTA}Score:{Style.RESET_ALL} {stats["correct"]}/{stats["total"]} {round(stats["correct"]/stats["total"]*100,2)}% {round(time.time()-start, 2)} s")

#def remove_package(package_name):
#    print(f"Removing {package_name}...")

def main():
    parser = argparse.ArgumentParser(description="Command Line Flashcard Tool")
    
    # Adding a positional argument 'command'
    parser.add_argument("command", choices=["practice"], help="The command to execute")
    
    # Adding a positional argument for the file name
    parser.add_argument("file", type=str, help="The name of the file")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Handle the command
    if args.command == "practice":

        input_file = ""
        for i in args.file.lower():
            if i == " ":
                input_file += "_"
            else:
                input_file += i

        practice(input_file)


    #elif args.command == 'remove':
    #    remove_package(args.file)

if __name__ == "__main__":
    main()
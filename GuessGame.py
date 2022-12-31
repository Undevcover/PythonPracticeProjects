#!/usr/bin/python3

import random

def guessGame(limit):
    count = 0
    compGuess = random.randint(1, limit)
    myGuess = 0;
    while(myGuess != compGuess):
        count = count + 1
        myGuess = eval(input(f"Guess a number between 1 and {limit}: "))
        if (compGuess > myGuess):
            print("Too Low, try again")
        elif (compGuess < myGuess):
            print("Too high, guess lower")

    print(f"Yaay! you guessed it right after {count} attempt(s)")


guessGame(10)

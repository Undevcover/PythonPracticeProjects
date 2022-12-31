import random
import time

def compGuess(limit):
    init = 1
    count = 0
    cycle = 1;
    while (cycle):
        count = count + 1
        guess = random.randint(init, limit)
        result = int(input(f"Is {guess} too high (enter 1), too low (enter 2) or just right? (enter 0) : "))
        if result == 1:
            limit = guess-1
        elif result == 2:
            init = guess+1
        else:
            cycle = 0
    print(f"Yaay!, I guessed {guess} right after just {count} attempts!")
print("Pick a number between 1 and 10, and I'll guess it 😊😊")
time.sleep(3)
compGuess(10)

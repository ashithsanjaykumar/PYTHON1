import random


def guess_num():
    number = random.randint(1, 100)
    attempts = 0
    while True:
        guess = int(input("Take a guess(1-100):"))
        attempts += 1
        if (guess < number):
            print("Too low")
        elif (guess > number):
            print("Too high")
        elif (guess == number):
            print("Correct! You have taken", attempts, "to guess it correctly")
            break


guess_num()

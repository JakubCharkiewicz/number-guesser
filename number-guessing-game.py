
from art import  logo, awesome_donut, an_actual_donut
import random
import  time

def menu():
    while True:
        print("1.Awesome donut(was not made by me)")
        print("2.An actual game")
        print("3.Exit")

        nd_choice = input("Choose an option, kind sir ")
        if nd_choice == "1":
            print(awesome_donut)
            print()
            print(an_actual_donut)
        elif nd_choice == "2":
            print(logo)
            print("Welcome to the Number Guesser game!")
            print("I'm thinking od a number between 1 and 100.")
            diff_chooser()

        elif nd_choice == "3":
            print("Bye!")
            break

random_number = random.randint(1, 100)

def diff_chooser():
    diff = input("Choose a difficulty. Type 'easy or 'hard': ")
    if diff == "easy":
        diff_easy()
    elif diff == "hard":
        diff_hard()

def diff_easy():
    attempts = 10
    while True:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess < random_number:
            attempts -= 1
            print("Too low!")
            if attempts > 0:
                print("Guess again!")
                time.sleep(3)
            if attempts == 0:
                print("You've run out of guesses, you lose!")
                print(f"I was thinking about {random_number}!")
                time.sleep(3)
                break
        elif guess > random_number:
            attempts -= 1
            print("Too high!")
            if attempts > 0:
                print("Guess again!")
            if attempts == 0:
                print("You've run out of guesses, you lose!")
                print(f"I was thinking about {random_number}!")
                time.sleep(3)
                break
        elif guess == random_number:
            print(f"Woah, you won! It was really : {random_number}! ")
            time.sleep(3)
            break


def diff_hard():
    attempts = 5
    while True:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess < random_number:
            attempts -= 1
            print("Too low!")
            if attempts > 0:
                print("Guess again!")
            if attempts == 0:
                print("You've run out of guesses, you lose!")
                print(f"I was thinking about {random_number}!")
                time.sleep(3)
                break
        elif guess > random_number:
            attempts -= 1
            print("Too high!")
            if attempts > 0:
                print("Guess again!")
            if attempts == 0:
                print("You've run out of guesses, you lose!")
                print(f"I was thinking about {random_number}!")
                time.sleep(3)
                break
        elif guess == random_number:
            print(f"Woah, you won! It was really: {random_number}!")
            time.sleep(3)
            break
menu()
#define function to generate sets of numbers
from random import randint
import os

os.system('cls')


def generate_numbers(lines, number, range, bonus = True, powerball = 0):
    ###   Check the inputs are valid and print out sets of random lottery numbers in the format requested  ###
    os.system('cls')
    all_sets = []
    if range < number and bonus == False or range < number + 1 and bonus == True:
        print("Error: I cannot return more numbers than the range of the lottery")
        return None
    if powerball == 0 and bonus == True:
        print (f"You asked for {lines} lines of {number} numbers from 1 to {range} with a bunus ball and no powerball")
    elif powerball != 0 and bonus == True:
        print (f"You asked for {lines} lines of {number} numbers from 1 to {range} with a bonus ball and powerball from 1 to {powerball}")
    else:
        print (f"You asked for {lines} lines of {number} numbers from 1 to {range} and powerball from 1 to {powerball}")

    while len(all_sets) < lines:
        numbers = set()
        while len(numbers) < number:
            num = randint(1, range)
            if num not in numbers:
                numbers.add(num)
        print(f"Your {number} lotto numbers are {numbers}", end=' ')
        if bonus == True:
            while len(numbers) < number + 1:
                bon = randint(1, range)
                if bon not in numbers:
                    numbers.add(bon)
            print("""Bonus number = (""", bon, """)""", end = ' ')
        if powerball != 0:
            pow = randint(1, powerball)
            numbers.add(pow)
            print("powerball =", pow, end = ' ')
        all_sets.append(numbers)
        print("")
    return all_sets
# test the function

while True:
    os.system('cls')
    print("Welcome to the lotto number generator.\nPlease follow the instructions to generate the numbers that match your country's lottery.\nPress ctrl-c to exit at any time.")

    try:
        lines = 0
        while lines == 0:
            try:
                lines = int(input("How many lines of numbers do you want to generate?"))
            except ValueError:
                print("Please enter a number")
        bonus = -1
        while bonus < 0:
            try:
                bonus = str(input("Do you want a bonus ball?"))
                if bonus.capitalize() == "Y" or bonus.capitalize() == "YES":
                    bonus = bool(True)
                else:
                    bonus = bool(False) 
            except ValueError:
                print("Please enter (y)es or (n)o")
                bonus = -1
        number = 0
        while number == 0:
            try:
                number = int(input("How many numbers per line are there in the draw?"))
            except ValueError:
                print("Please enter a number")
        rang = 0
        while rang == 0:
            try:
                rang = int(input("What is the maximum number for the lottery? (usually 40)"))
            except rang < number:
                print("There can't be more numbers than the range of the lottery")
            except ValueError:
                print("Please enter a number")
        powerball = -1
        while powerball < 0:
            try:
                powerball = int(input("If you want a powerball, enter the max number, otherwise press ENTER: ") or 0)
                if powerball > -1:
                    break
            except ValueError:
                print("Please enter a number")
    finally:
        x = generate_numbers(lines, number, rang, bonus, powerball)
    input("Press enter to continue or ctrl-c to exit")

    
# lines = int(input("How many lines of numbers do you want to generate?"))
# number = int(input("How many numbers per line are ther in the draw?"))
# rang = int(input("What is the total number of balls in the draw?"))
# bonus = bool(input("Do you want a bonus ball? (True or False)"))
# powerball = int(input("What is the maximum number for the powerball?"))

# generate_numbers(how many lines to generate, number of balls, range of lottery numbers, bonus ball(True or False), powerball max number)


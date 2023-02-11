#define function to generate sets of numbers
from random import randint
import os

os.system('cls')


def generate_numbers(lines, number_of_balls_drawn, max_ball_value, powerball = 0):
    ###   Check the inputs are valid and print out sets of random lottery numbers in the format requested  ###
    os.system('cls')
    all_sets = []
    if max_ball_value < number_of_balls_drawn:
        print("Error: I cannot return more numbers than the number off balls in the lottery")
        return None
    if powerball == 0:
        print (f"You asked for {lines} lines of {number_of_balls_drawn} numbers from 1 to {max_ball_value} and no powerball")
    elif powerball != 0:
        print (f"You asked for {lines} lines of {number_of_balls_drawn} numbers from 1 to {max_ball_value} with powerball from 1 to {powerball}")

    while len(all_sets) < lines:
        numbers = set()
        while len(numbers) < number_of_balls_drawn:
            num = randint(1, max_ball_value)
            if num not in numbers:
                numbers.add(num)
        print(f"Your {number_of_balls_drawn} lotto numbers are {sorted(list(numbers))}", end=' ')
        if powerball != 0:
            power_ball = randint(1, powerball)
            numbers.add(power_ball)
            print("powerball =", power_ball, end = ' ')
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
                print("There can't be more numbers than the max_ball_value of the lottery")
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
        user_input = ""
        while user_input.capitalize() != "N": 
            x = generate_numbers(lines, number, rang, powerball)
            user_input = input("- ENTER for a new set of numbers\n- N to change the settings\n- Q to quit")
            if user_input.capitalize() == "Q":
                quit()
            
    


    


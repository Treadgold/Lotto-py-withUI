import numpy as np
import os


def clear_console():
    # clear the console
    
    #check if the os is windows
    if os.name == 'nt':
        os.system('cls')
    #otherwise assume it is linux
    else:
        os.system('clear')
    

def get_numbers(max_value, powerball, number_of_balls_drawn):
    # Given the max value, powerball and number of balls drawn, return a set of numbers as an array
    
    balls = np.array(range(1, max_value + 1))
    if powerball != 0:
        powerball = list(range(1, powerball + 1))
    draw = np.random.choice(balls, number_of_balls_drawn, replace=False)
    if powerball != 0:
        powerball = np.random.choice(powerball, 1, replace=False)
        return draw, powerball
    return draw


def get_lines(lines, max_value, number_of_balls_drawn, powerball=0):
    # Generate a set of numbers for the number of lines requested
    # does this by calling get_numbers() and appending the result to a list
    
    all_sets = []
    while len(all_sets) < lines:
        all_sets.append(get_numbers(max_value, powerball, number_of_balls_drawn))
    return all_sets


def print_set(set):
    # takes input as list of arrays and prints them out in a nice format
    for line in set:
        for number in line:
            print(number, end=' ')
        print("")

while True:
    # main loop, gets user input and calls the functions to generate the numbers
    clear_console()

    print("Welcome to the lotto number generator.\nPlease follow the instructions to generate the numbers that match your country's lottery.\nPress ctrl-c to exit at any time.\n")

    try:
        lines = 0
        while lines == 0:
            try:
                lines = int(input("How many lines of numbers do you want to generate? : "))
            except ValueError:
                print("Please enter a number : ")
        number_of_balls = 0
        while number_of_balls == 0:
            try:
                number_of_balls = int(input("How many numbers per line are there in the draw? : "))
            except ValueError:
                print("Please enter a number : ")
        max_ball_value = 0
        while max_ball_value == 0:
            try:
                max_ball_value = int(input("What is the maximum number for the lottery? (usually 40) : "))
            except ValueError:
                print("Please enter a number : ")
            if max_ball_value < number_of_balls:
                print("There can't be more numbers than the max_ball_value of the lottery")
                max_ball_value = 0
            
        powerball = -1
        while powerball < 0:
            try:
                powerball = int(input("If you want me to add a powerball, enter the max number, otherwise press ENTER: ") or 0)
                if powerball > -1:
                    break
            except ValueError:
                print("Please enter a number")
    finally:
        user_input = ""
        while user_input.capitalize() != "N": 
            set = get_lines(lines, max_ball_value, number_of_balls, powerball)
            print("")
            print_set(set)
            print("")
            user_input = input("- ENTER for a new set of numbers\n- N to change the settings\n- Q to quit\n: ")
            clear_console()
            if user_input.capitalize() == "Q":
                quit()
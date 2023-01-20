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


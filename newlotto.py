import random
import os


def clear_console():
    # clear the console

    # check if the os is windows
    if os.name == 'nt':
        os.system('cls')
    # otherwise assume it is linux
    else:
        os.system('clear')


def get_numbers(max_value=40, powerball=10, number_of_balls_drawn=6):

    # make list of numbers for main draw
    balls = [str(i).zfill(2) for i in range(1, max_value + 1)]

    # make list of numbers for powerball
    if powerball != 0:
        powerball = [str(i).zfill(2) for i in range(1, powerball + 1)]

    # shuffle the balls
    random.shuffle(balls)

    # take a sample of the balls
    # Sort them so they are in order
    drawn_balls = sorted((balls[:number_of_balls_drawn]))

    # shuffle the powerball
    if powerball != 0:
        random.shuffle(powerball)
        drawn_powerball = powerball[0]
        # if powerball is not 0, return both the main draw and the powerball
        # as a tuple

        final = (drawn_balls, drawn_powerball)
        return final

    # otherwise return just the main draw
    return drawn_balls


def get_lines(lines=6, max_value=40, number_of_balls_drawn=6, powerball=10):
    # Generate a set of numbers for the number of lines requested
    # does this by calling get_numbers() and appending the result to a list

    all_sets = []
    while len(all_sets) < lines:
        all_sets.append(
            get_numbers(max_value, powerball, number_of_balls_drawn))
    return all_sets

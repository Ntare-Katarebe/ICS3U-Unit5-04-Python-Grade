#!/usr/bin/env python3

# Created by: Ntare Katarebe
# Created on: May 2021
# This program prints the volume of a cylinder
#   user inputs number

import math


def calculate_percentage(level):
    # This function prints the volume of a cylinder

    # process
    if(level == "4+"):
        result = (100 + 95) / 2
    elif(level == "4"):
        result = (94 + 87) / 2
    elif(level == "4-"):
        result = (86 + 80) / 2
    elif(level == "3+"):
        result = (79 + 77) / 2
    elif(level == "3"):
        result = (76 + 73) / 2
    elif(level == "3-"):
        result = (72 + 70) / 2
    elif(level == "2+"):
        result = (69 + 67) / 2
    elif(level == "2"):
        result = (66 + 63) / 2
    elif(level == "2-"):
        result = (62 + 60) / 2
    elif(level == "1+"):
        result = (59 + 57) / 2
    elif(level == "1"):
        result = (56 + 53) / 2
    elif(level == "1-"):
        result = (52 + 50) / 2
    elif(level == "R"):
        result = 49 / 2
    else:
        result = -1

    return result


def main():
    # this function just calls other functions

    level_from_user = input("Enter the level: ")
    # level_integer = int(level_from_user)
    level_percentage = calculate_percentage(level_from_user)
    print("Level {0} has a middle percentage of {1:,.0f}%."
          .format(level_from_user, level_percentage))


if __name__ == "__main__":
    main()

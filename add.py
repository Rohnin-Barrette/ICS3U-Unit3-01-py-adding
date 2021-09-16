#!/usr/bin/env python3

# Created by: Rohnin Barrette
# Created on: Sept 2021

# this program calculates the sum of any two numbers


def main():
    # this program calculates the sum of any two numbers

    # input
    first_number = int(input("Please enter the first number (integer) here: "))
    second_number = int(
        input("Please enter the first number (integer) here: ")
    )

    # process
    sum = first_number + second_number

    # output
    print("")
    print("{0} + {1} = {2} ".format(first_number, second_number, sum))
    print("\nDone.")


if __name__ == "__main__":
    main()

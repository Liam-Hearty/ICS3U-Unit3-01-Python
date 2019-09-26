#!/usr/bin/env python3

# Created by: Liam Hearty
# Created on: September 2019
# This program adds two integers together.


def main():
    # This program adds two integers together.

    # input
    first_integer = int(input("Enter the first integer of the adding " +
                              "equation: "))
    second_integer = int(input("Enter the second integer of the adding " +
                               "equation: "))

    # process
    total = first_integer + second_integer

    # output
    print("")
    print("{0} + {1} = {2}".format(first_integer, second_integer, total))


if __name__ == "__main__":
    main()

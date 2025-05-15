#!/usr/bin/env python3
# Created by: Viviana Hurtado
# Date: may 5 2025
# This program has a function called fahrenheit().
# This function lets you enter a temperature in
# degrees Celsius (as a decimal), and converts
# and displays the temperature in Fahrenheit


def Fahrenheit():
    # convert celsius to fahrenheit

    # input
    celsius = float(input("Enter temperature in Celsius: "))

    # process
    fahrenheit = (9 / 5) * celsius + 32

    # output
    print("The temperature is {0}°F".format(fahrenheit))


def main():
    # this function just calls other functions

    # call function
    Fahrenheit()


if __name__ == "__main__":
    main()

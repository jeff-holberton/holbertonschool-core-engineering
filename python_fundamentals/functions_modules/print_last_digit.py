#!/usr/bin/env python3

def print_last_digit(number):
    print(number % 10 if number >= 0 else (number % 10 - 10) * -1, end="")

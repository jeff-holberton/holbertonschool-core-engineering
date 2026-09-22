#!/usr/bin/env python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print(" ")
    for list in matrix:
        for index, element in enumerate(list):
            if index != len(list) - 1:
                print("{:d} ".format(element), end="")
            else:
                print("{:d}".format(element))

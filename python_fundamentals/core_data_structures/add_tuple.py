#!/usr/bin/env python3

def add_tuple(tuple_a=(), tuple_b=()):
    list_a = [0, 0]
    list_b = [0, 0]
    for index, element in enumerate(tuple_a):
        list_a[index] = element
    for index, element in enumerate(tuple_b):
        list_b[index] = element
    return (list_a[0] + list_b[0], list_a[1] + list_b[1])

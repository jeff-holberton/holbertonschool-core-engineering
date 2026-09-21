#!/usr/bin/env python3

def pow(a, b):
    if b == 0:
        return 1
    p = a
    if (b > 0):
        for i in range(1, b):
            p *= a
    if b < 0:
        for i in range(1, b * -1):
            p *= a
        return 1 / p
    return p

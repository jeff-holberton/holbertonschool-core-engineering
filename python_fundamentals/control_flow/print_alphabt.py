#!/usr/bin/env python3

alphabet = "abcdefghijklmnopqrstuvwxyz"
result = ""

for i in alphabet:
    if i != 'e' and i != 'q':
        result = "{}{}".format(result, i)
print(result)

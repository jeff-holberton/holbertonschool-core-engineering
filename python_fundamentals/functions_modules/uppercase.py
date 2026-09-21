#!/usr/bin/env python3

def uppercase(str):
    result = ""
    for c in str:
        ascii_char = ord(c)
        if ord('a') <= ascii_char <= ord('z'):
            result += chr(ascii_char - 32)
        else:
            result += chr(ascii_char)
    print("{}".format(result))

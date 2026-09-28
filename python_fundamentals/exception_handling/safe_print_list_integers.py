#!/usr/bin/env python3

def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    for index in range(0, x):
        try:
            print("{:d}".format(my_list[index]), end="")
            printed += 1
        except TypeError:
            pass
        except ValueError:
            pass
        except AttributeError:
            pass
        except IndexError:
            print()
            return printed
    print()
    return printed

#!/usr/bin/env python3
"""verboselist"""

from abc import ABC, abstractmethod


class VerboseList(list):
    """VerboseList Class"""

    def append(self, element):
        super().append(element)
        print(f"Added [{element}] to the list.")

    def extend(self, iterable):
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, element):
        super().remove(element)
        print(f"Removed [{element}] from the list.")

    def pop(self, index=None):
        if index is None:
            index = len(self) - 1
        print(f"Popped [{self[index]}] from the list.")
        return super().pop(index)


if __name__ == "__main__":
    vl = VerboseList([1, 2, 3])
    vl.append(4)
    vl.extend([5, 6])
    vl.remove(2)
    vl.pop()
    vl.pop(0)

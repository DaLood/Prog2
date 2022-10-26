"""
m1.py
"""

import random
import time
import math

def length_longest(lst):
    """Returns the length of the longest (sub-)list in lst"""
    pass


def bubbelsort(aList):
    for i in range(len(aList)-1):
        for j in range(len(aList)-1):
            if aList[j] > aList[j+1]:
                aList[j], aList[j+1] = aList[j+1], aList[j]
                

def foo(n):
    result = 1
    for k in range(3):
        for i in range(n*n):
            result += k*n
    return result
    

def main():
    print(length_longest(1))                   # Should be 0
    print(length_longest([]))                  # Should be 0
    print(length_longest([1,2,3]))             # Should be 3
    print(length_longest([1,[2,3]]))           # Should be 2
    print(length_longest([1,[1,2,3,4],3]))     # Should be 4 

    aList=[3,2,5,1,7]
    bubbelsort(aList)
    print(aList)

if __name__ == "__main__":
    main()
    
"""
Solution to A2 (Time complexity for bubbelsort):








Solution to B1 (Time complexity for function foo):







"""
    
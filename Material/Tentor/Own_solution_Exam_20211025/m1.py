"""
m1.py
"""

import random
import time
import math

def length_longest(lst):
    """Returns the length of the longest (sub-)list in lst"""
    if lst == [] or isinstance(lst, list) == False:
        return 0
    else:
        return max(len(lst),length_longest(lst[0]),length_longest(lst[1:]))

#
# def length_longest(lst):
#     # Variant 1: Iteratively in the 'width' direction
#     if type(lst) != list:
#         return 0
#     result = len(lst)
#     for x in lst:
#         result = max(result, length_longest(x))
#     return result






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

    times = []
    for i in range(700,900):
        start = time.perf_counter()

        foo(i)

        stop = time.perf_counter()

        c = (stop-start)/(i^2)

        t = c * 1000000**(2)
        times.append(t)

    t_avg = sum(times)/len(times)
    print(t_avg)

    # 146504597.50891393

if __name__ == "__main__":
    main()


    
"""
Solution to A2 (Time complexity for bubbelsort):

Tidsuppskattning från antalet iterationer som görs är:

t(n) = c * n^2

Då första for-loopen itererar n gånger och för varje itereration kommer andra for-loopen itererare 
n gånger, alltså n^2 gånger.









Solution to B1 (Time complexity for function foo):

342442993.1671672 sek







"""
    
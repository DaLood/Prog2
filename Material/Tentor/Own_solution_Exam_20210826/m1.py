"""
Solutions to exam tasks for modul 1
Name:
Code:
"""

import random
import time
import math


def count_all(lst, d):
    """ A1: Count_all all occurencies of d recursively """
    if len(lst) == 0:  # Basfall listan är tom returnera 0
        return 0
    elif lst[0] == d:
        return 1 + count_all(lst[1:], d)  # Om lst[0] är det sökta elementet addera en 1 och kör resterande elementen i count_all.
    elif type(lst[0]) == list:  # Om lst[0] elementet är en lista, kör den listan i count_all och kör resterande elementen i count_all.
        return count_all(lst[0], d) + count_all(lst[1:], d)
    else:
        return count_all(lst[1:], d)  # Om lst[0] inte är en lista och inte är sökta elementet kör resterande elementen i count_all.


def c(n):
    k = 0
    if n <= 2:
        return 1
    else:
        k =  k + 1
        return c(n-1) - c(n-3)

def c_mem(n):
    """ A2:
        Compute c(n) recursively as above but use
        memorization to keep the runtime down.
    """
    memory = {0:0,1:1}

    def c_mem_1(n):
        if n <= 2:
            return 1
        elif n not in memory:
            memory[n] = c_mem_1(n-1) - c_mem_1(n-3)
        return memory[n]

    return c_mem_1(n)




def main():


    # # print('Test count_all_all')
    #
    # print(count_all([], 1))
    # print(count_all([1], 1))
    # print(count_all([1, 2, 1, 3, [[1], [1, 2, 3]]], 1))
    # print(count_all([1], 0))
    #
    # print('\nTest of c')
    # print('c(3):', c(3))
    # print('c(4):', c(4))
    # print('c(5):', c(5))
    # print('c(9):', c(9))
    #
    # print('\nTest of c_mem')
    # print('c_mem(3):', c_mem(3))
    # print('c_mem(4):', c_mem(4))
    # print('c_mem(5):', c_mem(5))
    # print('c_mem(9):', c_mem(9))
    #
    # print('c_mem(100):', c_mem(100))

    print('\nCode for task B1')

    n = 10

    tstart = time.perf_counter()
    c(n)
    tstop = time . perf_counter()

    k = (tstop-tstart) / (2**n)

    T_100 = k*2**100

    print(f'{T_100/(60*60*24*365)} years')





if __name__ == "__main__":
    main()
    print('Over and out')


"""
Answer to task B1:
Vi låter t(n) beteckna antalet additioner som utförs för c(n) och får då:
f(n) = 0 om n=<2
f(n) = 1 + f(n-1) + f(n-3) om n>2
 
Uppskattning:
f(n) = 1 + 2*f(n-1) = 2**n-1 = 2**n

Vet därför att den växer som f(n) men för att ta fram tiden behöver vi hitta konstanten C som beror på datorn:
t(n) = c*f(n)

Testar därför för t(10) och får då en tid och akn bryta ut c.
Härifrån beräknas t(100) med den funna konstanten  


"""

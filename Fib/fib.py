from numba import njit
from time import perf_counter as pc
import matplotlib.pyplot as plt



def fib_py(n):

    if n <= 1:
        return n

    else:
        return(fib_py(n-1) + fib_py(n-2))


@njit
def fib_numba(n):

    if n <= 1:
        return n

    else:
        return(fib_numba(n-1) + fib_numba(n-2))


if __name__ == '__main__':
    sek_py = []
    sek_nb = []
    sek_c =[]

    n = 1

    print(f'\n for n = {n}')
    start = pc()
    print(fib_py(n))
    end = pc()
    print(f"Py process took {round(end - start, 2)} seconds \n")



    start = pc()
    print(fib_numba(n))
    end = pc()
    print(f"Numba process took {round(end - start, 2)} seconds \n")



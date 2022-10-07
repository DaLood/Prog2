#!/usr/bin/env python3.9
from time import perf_counter as pc
from fib import fib_py, fib_numba
from person import Person



        
if __name__ == '__main__':
    for n in range(30,46):


        print(f'\n for n = {n}')
        start = pc()
        print(fib_py(n))
        end = pc()
        print(f"Py process took {round(end - start, 2)} seconds \n")


        start = pc()
        print(fib_numba(n))
        end = pc()
        print(f"Numba process took {round(end - start, 2)} seconds \n")
           
        start = pc()
        f = Person(n)
        print(f.fib())
        end = pc()
        print(f"C++ process took {round(end - start, 2)} seconds")

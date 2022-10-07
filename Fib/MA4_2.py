#!/usr/bin/env python3.9
from time import perf_counter as pc
from fib import fib_py, fib_numba
from person import Person
import matplotlib as plt

def sek_p(n):
    start = pc()
    res = fib_py(n)
    end = pc()
    sek = round(end - start, 2)
    return sek, res


def sek_n(n):
    start = pc()
    res = fib_numba(n)
    end = pc()
    sek = round(end - start, 2)
    return sek, res

def sek_c(n):
    start = pc()
    f = Person(n)
    res = f.fib()
    end = pc()
    sek = round(end - start, 2)
    return sek, res

        
if __name__ == '__main__':
    n1 = range(30,46)
    n2 = range(20,31)
    n3 = 3
    
    sek_n(0)

    plt.figure(1)

    plt.plot(n1,[sek_p(i)[0] for i in n1], "b", label = 'For python')
    plt.plot(n1,[sek_n(i)[0] for i in n1], "r", label = 'For numba')
    plt.plot(n1,[sek_c(i)[0] for i in n1], "g", label = 'For c++')
 


    plt.title('Timing for all three function')
    plt.xlabel('n')
    plt.ylabel('Sekunder')
    plt.legend(loc="upper right")
    
    plt.savefig('All_three')
    

    plt.figure(2)

    plt.plot(n2, [sek_p(i)[0] for i in n2], "b", label='For python')
    plt.plot(n2, [sek_n(i)[0] for i in n2], "r", label='For numba')
    
    plt.title('Timing for python and numba')
    plt.xlabel('n')
    plt.ylabel('Sekunder')
    plt.legend(loc="upper right")

    plt.savefig('python_numba')


    sek_n ,res_n = sek_n(n3)
    sek_c ,res_c = sek_c(n3)
    print(f'For n = {n3} is: \n fib = {res_n} for numba \n fib = {res_c} for c++')
    #For c++ the numbers got out of int range

        
        

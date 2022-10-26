from time import perf_counter as pc
from fib import fib_py, fib_numba
import matplotlib.pyplot as plt


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




if __name__ == '__main__':
    n1 = range(20,25)
    n2 = range(20,25)
    n3 = 3
    sek_n(1)

    plt.figure(1)
    plt.plot(n1,[sek_p(i)[0] for i in n1],"b", label = 'For python')
    plt.plot(n1,[sek_n(i)[0] for i in n1],"r", label = 'For numba')

    plt.title('Timing for all three function')
    plt.xlabel('n')
    plt.ylabel('Sekunder')
    plt.legend(loc="upper right")
    plt.show()


    plt.figure(2)
    plt.plot(n2, [sek_p(i)[0] for i in n2], "b", label='For python')
    plt.plot(n2, [sek_n(i)[0] for i in n2], "r", label='For numba')

    plt.title('Timing for numba and c++')
    plt.xlabel('n')
    plt.ylabel('Sekunder')
    plt.legend(loc="upper right")
    plt.show()




import math, matplotlib.pyplot as plt, random

def pi(n):
    x = []
    y = []
    nc = []
    nk = []

    for i in range(n):
         x.append(random.uniform(-1,1))
         y.append(random.uniform(-1,1))
         if x[i]**2 + y[i]**2 <= 1:
            nc.append(i)
         elif x[i]**2 + y[i]**2 > 1:
            nk.append(i)
    pi = 4 * len(nc)/n


    plt.plot([x[i] for i in nc],[y[i] for i in nc],'.',color='red')
    plt.plot([x[i] for i in nk],[y[i] for i in nk],'.',color='blue')
    plt.show()

    return n, nc, pi





if __name__ == "__main__":

    n, nc, pi = pi(1000)


    print(f'Antalet punkter som hamnat i cirkeln är: {len(nc)} av {n}')
    print(f'Approximationen av pi är: {pi}')
    print(f'Inbyggda konstanten pi i python är: {math.pi}')


"""
Approximation PI när n = {1000, 10000, 100000}

n = 1000:
pi = 3.172


n = 10000:
pi = 3.138


n = 100000:
pi = 3.1412

"""














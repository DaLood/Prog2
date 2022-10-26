from time import perf_counter as pc
from Upg1.Higher_order import higher_order
import concurrent.futures as future
import random, math


def higher_order_2(n,d):
    nc = []
    x = [[list(map(lambda x : x**2,[random.uniform(-1,1) for i in range(d)]))] for jj in range(n)]
    for i in zip(range(n),x):
        if sum(i[1][0]) <= 1:
            nc.append(i[0])

    return len(nc)



if __name__ == "__main__":
    start = pc()

    V_MC, V_teo = higher_order(1000000,2)
    print(f'Approx: {V_MC} \n'
          f'Teo: {V_teo}:')

    end = pc()
    print(f"Process took {round(end-start, 4)} seconds \n")



if __name__ == "__main__":
    start = pc()
    r = 1
    d = 2

    times = 10
    n_per = 100000
    n_tot = n_per*times

    with future.ProcessPoolExecutor() as ex:
        results = ex.map(higher_order_2, [n_per for i in range(times)],[d for i in range(times)])

    V_MC = sum(results) * ((2 * r) ** d) / n_tot
    print(f'Parallelprogrammering: {V_MC}')

    end = pc()
    print(f"Process took {round(end - start, 2)} seconds")







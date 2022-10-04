import random, math
def higher_order(n,d):
    r = 1


    nc = []

    x = [[list(map(lambda x : x**2,[random.uniform(-1,1) for i in range(d)]))] for jj in range(n)]

    for i in zip(range(n),x):
        if sum(i[1][0]) <= 1:
            nc.append(i[0])

    V_MC = len(nc) * ((2*r)**d) / n
    V_teo = (math.pi**(d/2)*r**d)/(math.gamma(d/2+1))

    return V_MC, V_teo






if __name__ == "__main__":

    V_MC, V_teo = higher_order(100000,3)
    print(f'Approx: {V_MC} \n'
          f'Teo: {V_teo}:')



"""

(n, d) = (100000, 2)
Approx: 3.13752 
Teo: 3.141592653589793:

(n, d) = (100000, 11)
Approx: 1.8432 
Teo: 1.8841038793898994:

"""






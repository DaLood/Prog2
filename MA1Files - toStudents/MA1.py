"""
Solutions to module 1
Student: David Lood
Mail: david.lood.3070@student.uu.se
Reviewed by: Adam Pehrson
Reviewed date: 7/9
"""

import random
import time
import time
import numpy
import statistics
import math




def power(x, n):         # Optional
    if n < 0:
        return 1/power(x,-n)
    elif n==0:
        return 0
    else:
        return x*power(x,n-1)

def divide(t, n):        # Optional
    if t < n:
        return 0
    return 1 + divide(t-n,n)

def digit_sum(x):        # Optional
    x = str(x)
    if len(x) - 1 == 0:
        return int(x)
    return int(x[0]) + digit_sum(int(x[1:]))

def get_binary(x):       # Optional
    if x == 0:
        return ""
    else:
        return get_binary(x // 2) + str(x % 2)

def reverse(s):          # Optional
    if len(s)<=1:
        return s
    else:
        return s[-1] + reverse(s[:-1])


def reverse1(s):          # Optional
    if len(s) <= 1:
        return s
    else:
        mid = len(s) // 2
        return reverse1(s[mid:]) + reverse1(s[:mid])

#Tid för fibonacci
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)













def multiply(m, n):      # Compulsory
    if n == 0:  #Basfall
        return 0
    else:
        return m + multiply(m, n-1) #Adderar m och körs n gånger


# Använda basfallet 1 istället och return m
# N är alltid den minsta av n och m
# Dividera ner n och multplicera upp m

def multiply1(m, n):      # Compulsory
    if n >= m:
        n, m =m, n

    if n >= 1000 and n%2 == 0:
        n = divide(n, 2)
        m = multiply(m, 2)

    if n == 1:
        return m
    else:
        return m + multiply(m, n-1)





def harmonic(n):         # Compulsory
    if n == 1: #Basfall
        return 1
    return 1/n + harmonic(n-1)





def largest(a):     # Compulsory
    if len(a) == 1: # Basfall om listan a har 1 eller mindre element returneras första elementet
        return a[0]
    elif a[0] < a[1]:   # Om a:s första element är mindre än andra kör listan igen utan första elementet
        return largest(a[1:])
    else:             # Om a:s första element istället är större än andra kör listan igen utan det andra elementet
        return largest(a[:1] + a[2:])





def count(x, s):    # Compulsory
    if len(s) == 0:    # Basfall listan är tom returnera 0
        return 0
    elif s[0] == x:
        return 1 + count(x, s[1:])  # Om s[0] är det sökta elementet addera en 1 och kör resterande elementen i count.
    elif type(s[0]) == list:  # Om s[0] elementet är en lista, kör den listan i count och kör resterande elementen i count.
        return count(x, s[0]) + count(x,s[1:])
    else:
        return count(x, s[1:])   # Om s[0] inte är en lista och inte är sökta elementet kör resterande elementen i count.


def count1(x, s):    # Compulsory
    if len(s) == 0:
        return 0
    elif s[0] == x:
        return 1 + count1(x, s[1:])
    elif type(s[0]) == list:
        return count1(x,s[1:])  # Körs som count1 förrutom att den tittar bara på första lagret och om det då är en lista förbises den.
    else:
        return count1(x, s[1:])





def zippa(l1, l2):       # Compulsory
    if len(l1) == 0 or len(l2) == 0: # Basfall när l1 eller l2 är tomma returnera resten av den ena eller andra listan
        return l1 + l2
    else:
        return [l1[0]] + [l2[0]] + zippa(l1[1:],l2[1:])




def bricklek(f, t, h, n): # Compulsory
    if n == 0:    # Basfall inga brickor att flytta
        return []
    else:
        return  bricklek(f, h, t, n-1) + [str(f) + '->' + str(t)] + bricklek(h,t,f,n-1)



# bricklek(f,t,h,2)     från f -> t med h emellan
# ['f->h', 'f->t', 'h->t']
# Första termen kommer ifrån bricklek(f,h,t,1)    från f -> h med t emellan
# Andra termen kommer ifrån bricklek(f,t,h,2)     från f -> t med h emellan
# Tredje termen kommer ifrån bricklek(h,t,f,1)    från h -> t med f emellan
# Leder till bricklek(f, h, t, n-1) + [str(f) + '->' + str(t)] + bricklek(h,t,f,n-1)





def main():
    """ Demonstates my implementations """
    # Write your demonstration code here
    # print(multiply(300, 5))
    # print(multiply1(1000, 1000))
    # print(harmonic(3))
    # print(largest(['15', '3', '6', '19']))
    # print(count(4, [1, 4, 2, ['a', [[ 4 ], 3, 4]]]))
    # print(zippa([1, 3, 5], [ 2, 4, 6, 8, 10])
    # print(bricklek('f', 't', 'h', 2))





#Exc 17

#x = range(20,40)
#l3 = []
#for i in x:
#    tstart = time . perf_counter ()
#    fib(i)
#    tstop = time . perf_counter ()
#    l3.append((tstop - tstart)/1.618**i)
#
#c = statistics.mean(l3)
#print(c)
#
#n = 50
#t = c * 1.618**n



if __name__ == "__main__":
    main()
    
####################################################    



"""
  Answers to the none-coding tasks
  ================================
  
  Exercise 16: Time for bricklek with 50 bricks:
  Theta(2^n-1)
  
  t(1) = 1 = (2^1-1)   =>   c=1
  
  t(50) = 2^50-1 = 10^15 s = (10^15)/(60*60*24*365) ~= 36 million years
  
  
 
  
  
  Exercise 17: Time for Fibonacci:
  a)
  After multiple runs I get t(n) ~= 1.48e-07 * 1.618^n
  b)
  t(50) = 1.15 h
  t(100) = 3.7e6 years
  

  
  
  Exercise 20: Comparison sorting methods:
  
  t_i(n) = c * n^2       =>     t_i(1000) = 1 = c * 1000^2     =>     c = 1e-6 
             
  t_m(n) = c * n*log10(n)     =>     t_i(1000) = 1 = c * 1000*log10(1000)     =>    c = 3e-3
  
  
  t_i(1e6) = 11.6 days
  t_i(1e9) = 31710 years
  
  t_m(1e6) = 33 min
  t_m(1e9) = 34.7 days
  
  
    
    
  Exercise 21: Comparison Theta(n) and Theta(n log n)
  
  Algoritm A:
  Theta(n)
  
  
  
  Algoritm B, Theta(n*log10(n):
  t(n) = c*n*log10(n)   =>   t(10) = 1 = c*10*log10(10)  =>   c = 1/10
  
  
  Algoritm A = Algoritm B:
  n = n * log10(n)/10     =>     n > 10^10 
  
  
  Answer: n Should be at least 10^10
  
  
  
  
  
  

"""
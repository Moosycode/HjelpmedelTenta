"""
Solutions to module 1
Student: 
Mail:
Reviewed by:
Reviewed date:
"""

import random
import time


def power(x, n):  # Optional
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)


def multiply(m, n):  # Compulsory
    if n == 0:
        return 0
    else:
        return m + multiply(m, n - 1)


def divide(t, n):  # Optional
    if n > t:
        return 0
    else:
        return 1 + divide(t - n, n)


def harmonic(n):  # Compulsory
    if n == 0:
        return 0
    else:
        return 1 / n + harmonic(n - 1)


def digit_sum(x):  # Optional
    if x == 0:
        return 0
    else:
        return x % 10 + digit_sum(int(x / 10))


def get_binary(x):  # Optional

    pass


def reverse(s):  # Optional
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverse(s[:-1])


def largest(a):  # Compulsory
    n = len(a)
    if len(a) == 1:
        return a[0]
    else:
        foreg = largest(a[:-1])
        nu = a[-1]
        if foreg > nu:
            return foreg
        else:
            return nu


def count(x, s):  # Compulsory
    if len(s) == 0:
        return 0
    if type(s) != list:
        if s == x:
            return 1
        else:
            return 0
    if type(s[-1]) == list:
        return count(x, s[-1]) + count(x, s[:-1])
    else:
        if x == s[-1]:
            return 1 + count(x, s[:-1])
        else:
            return count(x, s[:-1])


def zippa(l1, l2):
    if len(l1) == 0:
        return l2
    elif len(l2) == 0:
        return l1
    else:
        return [l1[0], l2[0]] + zippa(l1[1:], l2[1:])


def bricklek(f, t, h, n):  # Compulsory
    if n == 0:
        return []
    else:
        return bricklek(f, h, t, n-1) + [f'{f}->{h} '] + bricklek(t, f, h, n-1)


def exchange(a, coins):
    """ Count possible way to exchange a with the coins in coins"""
    if a == 0:
        return 1
    elif (a < 0) or (len(coins) == 0):
        return 0
    else:
        return exchange(a, coins[1:]) + exchange(a - coins[0], coins)

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)



n = 5
tstart = time.perf_counter()
fib(n)
tstop = time.perf_counter()
t1 = tstop-tstart
print (f" Measured time : {tstop - tstart } seconds for n = {n}")
tstart = time.perf_counter()
fib(n-4)
tstop = time.perf_counter()
t2 = tstop-tstart
print (f" Measured time : {tstop - tstart } seconds for n = {n-4}")
print(f'Qoutient betwwen t1 and t2: {t1/t2}')
print(f'Analytical ratio: {power(1.618,n-1)}')

"""
  Answers to the none-coding tasks
  ================================


  Exercise 16: Time for bricklek with 50 bricks:
    Ran code for 1 hr and gave up :(

  Exercise 17: Time for Fibonacci:
  Time for n = 1: 1e-6
  Time for n = 50: 1e-6 *1.618^49 sek (about 5 hrs)
  Time for n = 100: 1e-6 * 1.618^99 (about 15 million years)

  Exercise 20: Comparison sorting methods:
    10^3 --> 10^6
    1 --> 1000^3 sek för O(n^2)
    1 --> 3000 sek för o(n log(n))
    
    10^3 --> 10^6
    1 --> 1000^6 sek för O(n^2)
    1--> 6000 sek för O(n log(n))

  Exercise 21: Comparison Theta(n) and Theta(n log n)
  
  c = 1/(10log10) = 0.1
  => 0.1 n log n > n
  <=>
  log n > 10
  <=> 
  n > 10^10
  ans n > 10^10
  











"""
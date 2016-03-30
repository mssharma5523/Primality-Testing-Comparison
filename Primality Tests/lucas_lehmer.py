'''
This pseudocode can be taken from the Lucas lehmer primality test.
'''

import time
import random
import pickle
PRIME_MAX = 15485863
#PRIME_MAX = 100
def isqrt(n):
    if n < 0:
        raise ValueError
    elif n < 2:
        return n
    else:
        a = 1 << ((1 + n.bit_length()) >> 1)
        while True:
            b = (a + n // a) >> 1
            if b >= a:
                return a
            a = b
 
def isprime(n):
    if n < 5:
        return n == 2 or n == 3
    elif n%2 == 0:
        return False
    else:
        r = isqrt(n)
        k = 3
        while k <= r:
            if n%k == 0:
                return False
            k += 2
        return True
 
def lucas_lehmer_fast(n):
    if n == 2:
        return True
    elif not isprime(n):
        return False
    else:
        m = 2**n - 1
        s = 4
        for i in range(2, n):
            sqr = s*s
            s = (sqr & m) + (sqr >> n)
            if s >= m:
                s -= m
            s -= 2
        return s == 0

if __name__ == '__main__':
    primes_list = []
    start_time = time.time()
    for p in range(2,PRIME_MAX):
        print(str(p))
        result = lucas_lehmer_fast(p)
        if result == True:
            primes_list.append(p)
    print("Time taken to run is %s seconds" % (time.time()-start_time))
    with open('output_lucas.pickle', 'w') as handle:
        pickle.dump(primes_list, handle)
 
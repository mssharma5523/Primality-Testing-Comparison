import pickle
import time
#PRIME_MAX = 373587883
PRIME_MAX = 35485863
def primes(limit):
        limitn = limit+1
        not_prime = set()
        primes = []
        for i in range(2, limitn):
            if i in not_prime:
                continue
            for f in range(i*2, limitn, i):
                not_prime.add(f)
            primes.append(i)
        return primes

if __name__ == '__main__':
    start_time = time.time()
    primes_list = primes(PRIME_MAX)
    print("Time taken to run is %s seconds" % (time.time()-start_time))
    with open('output_sieve_eratos_test.pickle', 'w') as handle:
        pickle.dump(primes_list, handle)
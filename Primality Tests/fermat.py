import time
import random
import pickle
PRIME_MAX = 35485863
#PRIME_MAX = 100
def fermat(n,k=100):
	if n == 2:
		return True
	if not n & 1:
		return False
	for i in xrange(k):
		a = random.randrange(2,n-1)
		if pow(a,n-1,n) != 1:
			return False
	return True

if __name__ == '__main__':
	primes_list = []
	start_time = time.time()
	for p in range(4,PRIME_MAX):
		result = fermat(p)
		if result == True:
			primes_list.append(p)
	print("Time taken to run is %s seconds" % (time.time()-start_time))
	with open('output_fermat_100.pickle', 'w') as handle:
		pickle.dump(primes_list, handle)

	
# benchmark of 10000 iterations of fermat(100**10-1); Which is not prime.

# 10000 calls, 21141 per second.
# 20006 function calls in 0.481 seconds
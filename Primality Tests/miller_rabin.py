import time
import random
import pickle
PRIME_MAX = 35485863
#PRIME_MAX = 100
def miller_rabin(n, k=100):
	if n == 2:
		return True
	if n == 3:
		return True
	if not n & 1:
		return False

	def check(a, s, d, n):
		x = pow(a, d, n)
		if x == 1:
			return True
		for i in xrange(s - 1):
			if x == n - 1:
				return True
			x = pow(x, 2, n)
		return x == n - 1

	s = 0
	d = n - 1

	while d % 2 == 0:
		d >>= 1
		s += 1

	for i in xrange(k):
		a = random.randrange(2, n - 1)
		if not check(a, s, d, n):
			return False
	return True

if __name__ == '__main__':
	primes_list = []
	start_time = time.time()
	for p in range(2,PRIME_MAX):
		result = miller_rabin(p)
		if result == True:
			primes_list.append(p)
	print("Time taken to run is %s seconds" % (time.time()-start_time))
	with open('output_miller_rabin_100.pickle', 'w') as handle:
		pickle.dump(primes_list, handle)

# benchmark of 10000 iterations of miller_rabin(100**10-1); Which is not prime.

# 10000 calls, 11111 per second.
# 74800 function calls in 0.902 seconds
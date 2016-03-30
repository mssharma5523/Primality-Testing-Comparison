import time
import random
import pickle
PRIME_MAX = 35485863
#PRIME_MAX = 100
def solovay_strassen(n, k=100):
	if n == 2:
		return True
	if n == 3:
		return True
	if not n & 1:
		return False

	def legendre(a, p):
		if p < 2:
			raise ValueError('p must not be < 2')
		if (a == 0) or (a == 1):
			return a
		if a % 2 == 0:
			r = legendre(a / 2, p)
			if p * p - 1 & 8 != 0:
				r *= -1
		else:
			r = legendre(p % a, a)
			if (a - 1) * (p - 1) & 4 != 0:
				r *= -1
		return r

	for i in xrange(k):
		a = random.randrange(2, n - 1)
		x = legendre(a, n)
		y = pow(a, (n - 1) / 2, n)
		if (x == 0) or (y != x % n):
			return False

	return True

if __name__ == '__main__':
	primes_list = []
	start_time = time.time()
	for p in range(2,PRIME_MAX):
		result = solovay_strassen(p)
		if result == True:
			primes_list.append(p)
	print("Time taken to run is %s seconds" % (time.time()-start_time))
	with open('output_solovay_100.pickle', 'w') as handle:
		pickle.dump(primes_list, handle)

# benchmark of 10000 iterations of solovay_strassen(100**10-1); Which is not prime.

#10000 calls, 2440 per second.
#571496 function calls (74873 primitive calls) in 4.100 seconds
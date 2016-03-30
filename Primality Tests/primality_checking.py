import math
import pickle

if __name__ == '__main__':
	with open('output_sieve_eratos.pickle', 'rb') as handle:
		primes_data = pickle.load(handle)
	#print primes_data

	with open('output_fermat_100.pickle', 'rb') as handle:
		expected_primes = pickle.load(handle)
	#print expected_primes
	print "Total Number of primes are" + str(len(primes_data))
	intersection = set(expected_primes).intersection(primes_data)
	print len(list(set(expected_primes) - set(primes_data)))
	#print set(expected_primes).intersection(primes_data)
	#print list(set(expected_primes) - set(primes_data))
import time
PRIME_MAX = 35485863
#PRIME_MAX = 100
def prime3(a):
    if a < 2: return False
    if a == 2 or a == 3: return True # manually test 2 and 3   
    if a % 2 == 0 or a % 3 == 0: return False # exclude multiples of 2 and 3
 
    maxDivisor = a**0.5
    d, i = 5, 2
    while d <= maxDivisor:
        if a % d == 0: return False
        d += i 
        i = 6 - i # this modifies 2 into 4 and viceversa
 
    return True

if __name__ == '__main__':
    start_time = time.time()
    for p in range(0,PRIME_MAX):
        t = prime3(p)
    print("Time taken to run is %s seconds" % (time.time()-start_time))
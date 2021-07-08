
primes = [2,3]

def isPrime(n):
	for i in primes:
		if (i > n//2+1):
			break
		if(n%i==0):
			return False
	return True

# fill up the primes
for i in range(1,1000//6 + 2):
	if (isPrime(6*i-1)):
		primes.append(6*i-1)
	if (isPrime(6*i+1)):
		primes.append(6*i+1)

print(primes)

	
def countPrime(a, b):
	prime = True
	n = 0
	while(prime):
		if (n*n + a*n + b < 0):
			return 0
		#print(n*n + a*n + b, " : ", isPrime(n*n + a*n + b))
		if (not isPrime(n*n + a*n + b)):
			prime = False
		n = n + 1
		if (n > 50):
			break
	return n

a_ = 0
b_ = 0
max = -1

for a in range(-999,999):
	for b in range(-1000,1000):
		foo = countPrime(a, b)
		if(foo>max):
			a_ = a
			b_ = b
			max = foo

print("a_ : ",a_," | b_ : ",b_," | max : ",max)
print(countPrime(1, 41))
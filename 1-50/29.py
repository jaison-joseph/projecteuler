
primes = [2,3]

nos = []
nos2 = []

def isPrime(n):
	for i in primes:
		if (i > n//2+1):
			break
		if(n%i==0):
			return False
	return True

def isPrime2(n):
	if n in primes:
		return True
	else:
		return False

# fill up the primes
for i in range(1,100//6+1):
	if (isPrime(6*i-1)):
		primes.append(6*i-1)
	if (isPrime(6*i+1)):
		primes.append(6*i+1)

print(primes)

for a in range(2,101):
	for b in range(2,101):
		if (isPrime2(a) and isPrime2(b)):
			nos.append(a**b)
		else:
			nos2.append(a**b)

print(len(nos) + len(list(set(nos2))))
print(len(nos))				
print(len(primes))				

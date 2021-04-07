#include <stdio.h>
#include <math.h>
#include <stdbool.h>

int main() {
	long a[80000], i, j, k, longest, len = 2, latest;
	a[0] = 2;
	a[1] = 3;

	//get all primes
	for (i=5;i<1000;i+=2) {
		j=3;
		bool prime = true;
		while (j<=sqrt(i) && prime) {
			if (i%j == 0){prime = false;}
			else {j+=2;}
		}
		if (prime) {a[len] = i; len++; latest = i;}
	}

	
	long long sum;
	long length = 1, alsoLongest = 0;
	longest = 0;
	//get the desired num
	
	for (i=0;i<len-1;i++) {
		sum = a[i];
		j=i;
		bool prime = true;
		while ((++j)<=len && prime && ((sum += a[j])<1000)) {
			sum += a[j];
			//
			//chk for prime
			length ++;
			k=-1;
			while (prime && a[++k]<=sqrt(sum)) {
				if (sum%a[k] == 0) {prime = false;}
				/*
				if (!prime) {
					prime = true;
					k=-1;
					sum -=a[i];
				}
				*/
			}
			if (prime && sum>longest && length>alsoLongest && sum < 1000) {longest = sum; alsoLongest = length;}
			/*
			for (k=j+1;k<len;k++) {
				if (sum == a[k]) {longest = sum;}
			}
			*/
		}

	}
	printf ("%ld, %d", latest, len);
	printf ("\n %ld %lld",alsoLongest, longest);
	return 0;
}

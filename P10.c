#include <stdio.h>
#include <math.h>
#include <stdbool.h>

int main() {
	long int b[10000], i=2, counter;
	b[0] = 2;
	b[1] = 3;
	long long int sum = 5;
	for (counter=5; counter<200000; counter+=2) {
		bool prime = true;
		int j = 0;
		int lastPrime = sqrt(counter);
		//printf("%ld  ", counter);
		while (prime && b[j] <= lastPrime && j<i) {
			if (counter % b[j] == 0) {prime = false;}
			else {j++;}
		}
		if (prime) {b[i]=counter; sum += b[i]; i++;/* printf("%ld ",b[i-1]);*/ }
	}
	printf("%lld", sum);
	return 0;
}

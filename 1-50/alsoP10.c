#include <stdio.h>
#include <math.h>
#include <stdbool.h>

int main() {
	long i, j;
	unsigned long long sum = 2;
	for (i=3;i<2000000; i+=2) {
		bool prime = true;
		j = 3;
		while (prime && j <= sqrt(i)) {
			if (i%j == 0) {prime = false;}
			else {j+=2;}
		}

		if (prime) {sum += i; printf("%ld \n",i);}
	}
	printf("%llu",sum);
return 0;}

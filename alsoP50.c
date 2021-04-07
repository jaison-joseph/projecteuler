
#include <stdio.h>
#include <math.h>
#include <stdbool.h>

int main() {
	long a[80000], i, j, k, longest, len = 2, latest;
	a[0] = 2;
	a[1] = 3;
	for (i=5;i<1000;i+=2) {
		j=3;
		bool prime = true;
		while (j<=sqrt(i) && prime) {
			if (i%j == 0){prime = false;}
			else {j+=2;}
		}
		if (prime) {a[len] = i; len++; latest = i;/* printf("\n %ld", a[len-1]);*/ }
	}
	//printf("%ld", a[len-1]);

	long sum, con_len, num;
	longest=0;
	//start indice loop
	for (i=0;i<len-1;i++) {
		sum = a[i];
		con_len = 1;
		for (j=i+1; j<len ;j++) {
			sum += a[j];
			//printf("%ld \n", sum);
			con_len ++;
			bool prime = true;
			long k=0;
			while (a[k]<=sqrt(sum) && prime) {
				if (sum%a[k] == 0) {prime = false;}
				k++;
			}
			if (prime && con_len>longest)  {longest = con_len; num=longest; printf("%ld:%ld :: %ld:%ld :: %ld \n",i,a[i],j,a[j],num);}
		}
	}
	//printf("%ld, %ld",num, con_len);
}

#include <stdio.h>

int main() {
	float a, b, c;
	for (a=1;a<1000;a++) {
		for (b=1;b+a<1000;b++) {
			c = 1000 - b - a;
			//if (((a*a) + (b*b)) == c*c) {printf("%d : %d : %d",a,b,c);}
			if (a*a + b*b == c*c) {printf("%f",a*b*c);} 
		}
	}
	return 0;
}

#include <iostream>
#include <math.h>

using namespace std;

int main() {
    long ct = 2;
    unsigned long long int a = 1, b = 1, t;
    while (ct < 101000000) {
        t = b;
        b += a;
        a = t;
        ct ++;
    }

    cout << ++ct << ": " << b << endl;
}

//b<10*pow(10,13
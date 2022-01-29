#include <iostream>
#include <vector>

using namespace std;

bool isPrime(int no) {
    int i=3;
    while (i*i<=no) {
        if (no%i==0)
        return false;
        i+=2;
    }
    return true;
}

int main() {
    int count=1, current=3, i=1, n1, n2;
    while (count < 10001) {
        n1=6*i-1;
        n2=6*i+1;
        if (isPrime(n1)) {
            cout << endl << n1;
            count++;
        }
        if (isPrime(n2)){
            cout << endl << n2;
            count++;
        }
        i++;
    }
    return 0;
}
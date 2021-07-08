#include <iostream>

using namespace std;

enum boolean {NO='3', YES}; //it plays along, storing YES as a 4
// if NO was not given a vaue, it would be 0 and YES 1

int prim(int x) {
    int i = 3, isp = 1;
    while (i*i<=x) {
        if (x%i == 0) {
            return 0;
        }
        i += 2;
    }
    return isp;
}

void explorefn(int a, int b) {
    int temp;
    for (int i=0;i<10;i++) {
        cout << i << ": " << i*i + a*i + b << endl;
    }
}

int main() {
    cout << NO << ", " << YES << endl; // 3, 4 is the output
    explorefn(1,1);
}
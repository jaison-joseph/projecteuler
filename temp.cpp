#include <iostream>

using namespace std;

int main() {
    int i=63,j=62,b,c=1;
    b = i&j;
    cout << b;
    b=c<<1;
    cout << int(c<<1) << endl << b;
    for (b=0;b<4;b++) {
        for (c=0;c<4;c++) {
            int x = b&c;
            cout << endl << b << ", " << c << ", " <<x;
            if (b & c) { cout << ": true";}
        }
    }
}
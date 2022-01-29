#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;

int main() {
    int s = 4;
    int x[s][s];
    x[0][0] = 0;
    int i, j;
    for (i=1;i<s;i++) {
        x[i][0] = 1;
        x[0][i] = 1;
    }
    for (i=1;i<s;i++) {
        for (j=1;j<s;j++) {
            x[i][j] = ( x[i-1][j] + x[i][j-1] );
        }
    }

    /*
    for (i=0;i<20;i++) {
        for (j=0;j<20;j++) {
            cout << x[i][j] << ' ';
        }
        cout << endl;
    }
    */

   cout << x[s-1][s-1];
    return 0;
}
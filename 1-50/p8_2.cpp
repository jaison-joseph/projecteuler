#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;

int main() {
    char c;
    int i=0,len=0, selected[13], nos[1000];
    long product=1, longest = 1;
    fstream f("p8nums.txt");
    while (f >> c) {
        nos[i] = c - 48;
        len ++;
        //cout << nos[i] << ", ";
        //if (i%10 == 0) { cout << endl; }
        if (len>12) {
            len--;
            product = 1;
            for (int j=0;j<13;j++) {product*=nos[i-j];}
            if (product > longest) {longest = product;}
        }
        //if (nos[i] == 0) { len = 0; }
        //else { len ++; }
        
        i++;
    }
    //cout << endl;
    //for (i=0;i<10;i++) {cout << selected[i] << ", ";}
    //cout << endl << nos << endl << nos.length();
    cout << endl << "Longest: " << longest;
    return 0;
}
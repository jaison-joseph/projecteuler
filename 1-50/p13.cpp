#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;

int main() {
    string c;
    char ch;
    vector <string> nos;
    int i, count[10] = {0,0,0,0,0,0,0,0,0,0}, sum, carry_over = 0, digs[10];
    long product=1, longest = 1;
    fstream f("13nos.txt");
    while (getline(f,c)) {
        nos.push_back(c);
    }
    /*
    for (i=0;i<10;i++) {
        cout <<i<<", " << count[i] << endl;
    }
    */
    for (i=0;i<10;i++) {
        sum = 0;
        for (int j=0;j<49;j++) {
            ch = nos[j][49-i];
            //cout << ch;
            //if (j%10==0) { cout << endl; }
            sum += (ch-48);
        }
        sum += carry_over;
        digs[9-i] = sum%10;
        carry_over = (sum-digs[9-i])/10;
        cout <<i<<", " << "sum" << sum << ", carry_ver: "<< carry_over << endl;
    }
    for (i=0;i<10;i++) {cout << digs[i];}
    //cout << endl << "sum: " << sum;
    return 0;
}
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;

int main() {
    string c;
    char ch;
    vector <string> nos;
    int i, a[14][14], sum, carry_over = 0, digs[10];
    fstream f("p18.txt");
    while (getline(f,c)) {
        nos.push_back(c);
    }

    for (i=0; i<nos.size(); i++) {
        string s = nos[i];
        int num =0,start = 0, j=0;

        for (int j=0;j<s.size();j++) {
            if (s[j] == ' ') {
                string temp = "";
                temp += s[j-2];
                temp += s[j-1];
                cout << endl << "Ahaa";
                a[i][j] = stoi(temp);
                j++;
            }
        }
    }

    for (i=0;i<14;i++) {
        for (int j=0;j<14;j++) {
            cout << a[i][j] << ' ';
        }
        cout << endl;
    }

    return 0;
}
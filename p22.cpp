#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

int main() {
    vector<string> names;
    string temp;
    int a[20][20],no,count=0, delim, greatest=0;
    int max=0;
    ifstream f("p22_names.txt");
    while (getline(f,temp)) { count += 1; }
    cout << count << endl;
    cout << temp;
    return 0;
}
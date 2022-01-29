#include <iostream>
#include <vector>
using namespace std;

int main() {
    long long i, len=0, num, longest=0;
    vector <int> num_len;
    num_len.reserve(1000000);
    for (i=1;i<1000000;i++) {
        //if (i> 100000)cout << i <<endl;
        //cout << endl << i;
        len=0;
        int j=i;
        while (j!=1) {
            if (i==113383) { cout << j << ", "; }
            len++;
            if (j%2==0) { 
                j=j/2; 
                if (j<i) {
                    len += num_len[j-1];
                    j=1;
                }
            }
            else { j = 3*j+1; }
        }
        num_len.push_back(len);
        if (len>longest) {num=i; longest = len;}
    }
    cout << "longest: " << num << ", length: " << num_len[num-1];
    return 0;
}
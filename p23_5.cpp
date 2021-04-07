#include <iostream>
#include <vector>
using namespace std;

int p(int n) { //gives sum of divisors
    int sum = 0;
    for (int i=1;i<=n/2;i++) {
        if (n%i==0) sum += i;
    }    
    return sum;
}

int main() {
    vector <int> nos;
    long int sum = 0;
    bool isab[28124] = {false};

    for (int i=12;i<=28122;i++) {
        if (p(i)>i) nos.push_back(i);
        //if (i%2==1) count +=1;
    }
    for (int i=0;i<nos.size();i++) {
        for (int j=i;j<nos.size()&&nos[i]+nos[j]<28124;j++) {
            isab[nos[i]+nos[j]] = true;
        }
    }

    for (int i=0;i<=28123;i++) {
        if (!isab[i]) sum += i;
    }
    cout << sum;
    return 0;
}
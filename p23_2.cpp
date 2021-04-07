#include <iostream>
#include <vector>

using namespace std;

bool isab(int x) {
    bool ret = false;
    int sum = 0;
    int i=1;
    while(i<=x/2 && sum<=x) {
        if (x%i==0) { sum += i; }
        i++;
    }
    if (sum>x) {ret = true;}

    return ret;
}

vector <int> nos;
vector <int> sums;
int temp;


long long sum = 0;

void fillUp() {
    int i;
    for (i=1;i<=2812;i++) {
        if (isab(i)) {
            nos.push_back(i);
        }
    }

    cout << endl << "Done: "<< nos.size();
}

void fillSums_v2() {
    int temp,i,j,k;
    sums.push_back(0);
    for (i=0;i<nos.size();i++) {
        for (j=i;j<nos.size();j++) {
            temp = nos[i] + nos[j];
            if (temp < 28123) {
                int canWrite = 1;
                for (k=0;k<sums.size();k++) {
                    if (sums[k]>temp) break;
                    if (sums[k] == temp) {
                        canWrite = 0;
                        break;
                    }
                }
                if (canWrite==1) sums.insert(sums.begin()+k,temp);
            }
            else {break;}
        }
    }
    cout << endl << "Sums length: " << sums.size();
}
/*
void fillSums() {
    for (int i=0;i<nos.size();i++) {
        //cout << i;
        
        for (int j=i;j<nos.size();j++) {
            if (j == i) { cout << i; }
            temp = nos[i] + nos[j];
            if (temp<28123) { 
                k=0;
                while (k<sums.size() && temp < sums[k]) { k++; }
                if (temp == sums[k]) { temp = 30000; j = nos.size(); }
                else { sums.insert(k,temp); }
            }
            else { j = nos.size(); }
        }   
        //cout << '!'; 
        
    }
}
*/

void getSum() {
    for (int i=1;i<=28124;i++) {
        temp = 0;
        for (int j=0;j<sums.size();j++) {
            if (sums[j] == i) {
                sums.erase( sums.begin()+j );
                temp = 1;
                break;
            }
        }
        if (temp == 0) { sum += i; }
    }
}

int main() {
    cout << isab(28122) << endl << nos.size();
    fillUp();
    fillSums_v2();
    //getSum();
    return 0;
}
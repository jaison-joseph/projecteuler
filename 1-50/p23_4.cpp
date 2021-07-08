#include <iostream>
#include <vector>

using namespace std;

vector <int> nos;
vector <int> nonos;

int count = 0, odd1, temp, k, c2 = 0;
bool f;
long int sum = 0;
long long int fatty = 0;

int p(int n) {
    int sum = 0;
    for (int i=1;i<=n/2;i++) {
        if (n%i==0) sum += i;
    }    
    return sum;
}

void calc() {
    //nonos.push_back(0);
    for (int i=0; i<nos.size(); i++) {
        for (int j=i; j<nos.size(); j++) {
            temp = nos[i]+nos[j];
            if (temp<=28123) {             
                k=0;
                f = true; // 
                while (k<nonos.size() && f) {
                    if (temp==nonos[k]) { f = false; }
                    k += 1;
                }
                if (f) {nonos.push_back(temp);}
            }
            else {
                break;
            }
        }
    }
    sum = 0;
    for (int i=0;i<nonos.size();i++) {
        sum += nonos[i];
    }   
}


int main() {
    for (int i=12;i<=14063;i++) {
        if (p(i)>i) nos.push_back(i);
        //if (i%2==1) count +=1;
    }
    calc();
    for (int i=1;i<28123;i++) {
        fatty += i;
    }
    cout << nos[nos.size()-1] << endl << c2<<endl << nonos.size() << endl << sum <<endl << fatty-sum;
    return 0;
}

/* 
for ( k=0; k<nonos.size() && nonos[k]<temp; k++) { }
            if (k==nonos.size() && temp>nonos[k-1]) 
                nonos.push_back(temp);
            if (k<nonos.size() && nonos[k]>temp) 
                nonos.push_back(temp);
*/

/*
k=0;
foundasmall = false;
while (k<nonos.size()) {
    if (nonos[k]>temp) {
        foundasmall=true;
        break;
    }
    k+=1;
}
if (!foundasmall) {
    nonos.insert(nonos.begin()+k,temp);
}
if (foundasmall) {
    if (nonos[k-1]!=temp)
    nonos.insert(nonos.begin()+k-1,temp);
}
*/

/*
int j=0;
f = false; //if it can be expresses, tru
while (j<nonos.size() && !f) {
    if (nonos[j]==i) { f = true; }
    j+=1;
}
if (!f) {sum += i;}
else { nonos.erase(nonos.begin()+j-1); }
*/
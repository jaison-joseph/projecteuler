#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;
int no=0, num=14 ,i;

int count(int n) {
    int result = 0;
    for (int i = 1; i*i <= n; i++){
        if (n % i == 0) {
            cout << endl << i << " is a factor";
            result+=2;
            if (n / i == i)
                result--;
        }
    }
    cout << endl << result;
    return result;

}

int main() {
    count (num);
    /*
    while (no<=500) {
        no=0;
        count++;
        num += count;

        i=0;
        while (++i<=num/2) {
            if (num%i==0) { no++; }
        }
        if (no>100) {cout << endl << num << ", " << no;}
    }
    */
    //cout << endl << "The final number is: " << count(num);
}

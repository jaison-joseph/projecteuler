#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

int main() {
    int a[20][20],no,count=0, delim, greatest=0;
    int max=0;
    ifstream f("p11_nums.txt");
    while (f >> no ) {
        a[count/20][count%20] = no;
        count++;
    }

    cout << "Ocunt: " << count;
    
    for (int i=0;i<20;i++) {
        for (int j=0;j<20;j++) {
            int products[6] = {a[i][j],a[i][j],a[i][j], a[i][j], a[i][j], a[i][j]};
            for (int delta=1;delta<4;delta++) {
                //down
                if (i<17) { 
                    products[0] *= a[i+delta][j]; 
                    //l_to_r_diagonal
                    if (j<17) { 
                        products[1] *= a[i+delta][j+delta]; 
                    }
                }
                //right
                if (j<17) { 
                    products[2] *= a[i][j+delta]; 
                }
                //left
                if (j>=3) {
                    products[3] *= a[i][j-delta];
                }
                //top
                if (i>=3) {
                    products[4] *= a[i-delta][j];
                    //r-to-l diagonal
                    if (j<=17) {
                        products[5] *= a[i-delta][j+delta];
                    }
                }
            }
            for (int delta=0;delta<6;delta++) {
                if (products[delta]>greatest) {
                    greatest = products[delta];
                }
            }
        }
    }
    cout << endl << "Greatest product: " << greatest;

    return 0;
}

/*
    
    for (int i=0;i<20;i++){
        for (int j=0;j<20;j++) {
            //int t[5] = {a[i][j],a[i][j],a[i][j],a[i][j],a[i][j]};
            int t[3] = { a[i][j],a[i][j],a[i][j] };
            for (delim=1;delim<4;delim++) {
                //up
                if (j-delim>=0) t[0]*=a[i][j-delim];
                //if (i-delim>=0) {t[0]+=a[i][j-delim];}

                //dowm
                //if (i+delim<=19) {t[1]+=a[i][j+delim];}
                //if (j+delim<=19) {t[1]*=a[i][j+delim];}

                //left
                //if (i-delim>=0) { t[2] *= a[i-delim][j]; }

                //RIGHt
                if (i+delim<=19) {
                    t[1] *= a[i+delim][j];
                    if (j+delim<=19) {
                        //diagonal
                        t[2] *= a[i+delim][j+delim];
                    }
                }
            }
            for (delim=0;delim<3;delim++) {
                if (t[delim]>max) { max=t[delim]; cout << endl <<i << ", " <<j << ", " << delim;}
            }
        }
    }
    

    for (int i=0;i<20;i++){
        for (int j=0;j<20;j++) {
            //int t[5] = {a[i][j],a[i][j],a[i][j],a[i][j],a[i][j]};
            int t[3] = { a[i][j],a[i][j],a[i][j] };
            for (delim=1;delim<4;delim++) {
                //up
                if (j-delim>=0) {t[0]*=a[i][j-delim];}

                //RIGHt
                if (i+delim<=19) { 
                    t[1] *= a[i+delim][j];
                    //diagonal
                    if (j+delim<=19){ t[2] *= a[i+delim][j+delim]; }
                }
            }
            for (delim=0;delim<3;delim++) {
                if (t[delim]>max) { max=t[delim]; cout << endl <<i << ", " <<j << ", " << delim;}
            }
        }
    }

    */
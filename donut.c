#include <stdio.h>
#include <time.h>
#include <string.h>

int main() {

    struct timespec req;
    req.tv_sec = 0;
    req.tv_nsec = 90000000;
    char p[199];

    clock_t t = clock();
    for (int i=0; i<25; i++) {
        /*
        if (i<25) {
            for (int j=i;j<25;j++) {
                
            }
        }
        */
        /*
        if (i>25 && i<50) {
            for (int j=i;j<25;j++) {
                printf(" ");
            }
        } 
        */

        //printf("\n Tralalalalala");
        p[i] = 'a';
        printf(p);
        nanosleep(&req, NULL);
        printf("\e[1;1H\e[2J");
    }
    t = clock() - t;
    printf("\n ztime taken: %f", (double)t);
}
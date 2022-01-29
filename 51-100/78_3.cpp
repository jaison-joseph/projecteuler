#include <iostream>

using namespace std;

// this method was designed with the assumption that
// the input > 4

/*
prevCombo is set for 3: [[1,1,1], [1,2], [3]]
*/

int main() {
  long long unsigned int prevCombo = 3;
  int sed = 4;
  int hi = 0;
  int lo = 0;
  if (false) {
    while (sed <= 7) {
      hi = sed-2;
      lo = 2;
      prevCombo += 1;
      while (hi >= lo) {
        prevCombo += 1;
        hi -= 1;
        lo += 1;
      }
      cout << "\n "<< sed << " : " << prevCombo;
      sed += 1;
    }
  }
  if (true) {
    while(prevCombo % 1000000 != 0) {
      hi = sed-2;
      lo = 2;
      prevCombo += 1;
      while (hi >= lo) {
        prevCombo += 1;
        hi -= 1;
        lo += 1;
      }
      sed += 1;
    }
  }
  cout << "\n the solution is:" << sed;
  cout << "\n the length of the previous combo is" << prevCombo;
}

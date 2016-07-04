#include <iostream>

void increment(int i) {                 // variant 1
  i = i+1;
}

void increment_ref(int& i) {            // variant 2
  i = i+1;
}

void increment_ptr(int* i) {            // variant 3
  *i += 1;
}

/*
int& increment_alt(int i) {             // variant 4	--- seriously wrong !!!
  int j = i+1;
  return j;
}
*/

int main() {
  int j = 4;
  increment(j);      std::cout << j << "\n";
  increment_ref(j);  std::cout << j << "\n";
  increment_ptr(&j); std::cout << j << "\n";
  //std::cout << increment_alt(j) << "\n";
  return 0;
}


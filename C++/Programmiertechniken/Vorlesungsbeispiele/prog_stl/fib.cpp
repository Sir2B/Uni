#include <iostream>
using namespace std;


double fib(unsigned int n) {
  if (n == 1) return 1;
  if (n == 0) return 0;
  return (fib(n-1) + fib(n-2));
}

int main() {
  for (unsigned int i=0; i < 10; i++) {
    cout<< i << " : " << fib(i) << "\n";
  }
  //cout<< 100 << " : " << fib(100) << "\n";
  //cout<< 1000 << " : " << fib(1000) << "\n";
  return 0;
}

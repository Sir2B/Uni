


#include <iostream>

using namespace std;

void swap1 (int a, int b) { int t=a; a=b; b=t; }                          // compiles but does nor swap the values
void swap2 (int& a, int& b) { int t=a; a=b; b=t;}                         // correct
//void swap3 (int const & a, int const & b) { int t=a; a=b; b=t;}           // does not compile
void swap4 (int *a, int *b) { int *t=a; a=b; b=t;}                        // swaps the values of the copies of the pointers inside swap4 only
void swap5 (int* a, int* b) {int t=*a; *a=*b; *b=t;}                      // correct


int main() {
  int a=1; int b=2;
  swap1(a,b); cout << a << " " << b << "\n";
  a=1; b=2;
  swap2(a,b); cout << a << " " << b << "\n";
  a=1; b=2;
  //swap3(a,b); cout << a << " " << b << "\n";
  //a=1; b=2;
  swap4(&a,&b); cout << a << " " << b << "\n";
  a=1; b=2;
  swap5(&a,&b); cout << a << " " << b << "\n";
  return 0;
}



#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std; // declare namespace
int main()
{
  union { long l; double x; } u;  // ugly hack
  for ( int i=-4;i<=4;i++) {
    u.x = pow(2., i);
    printf("%f %lX \n", u.x, u.l );
    cout << u.x << endl << u.l << endl;
  }
}   // end-main

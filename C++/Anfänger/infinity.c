#include <iostream>
#include <cmath>
using namespace std;	

int main() 
{
double a = 0, b=1;
double c = b/a;
double d = sqrt(-1);

cout << " a = " << a    // ok
<< ", b = " << b        // ok
<< ", c = " << c        // inf
<< ", d = " << d        // nan 
<< endl;
}


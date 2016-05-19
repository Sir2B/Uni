#include <iostream>
#include "My3Vector.h"
using namespace std;

int main()
{
    My3Vector a, b(1.,1.,-1.), c(0.,2.,1.); // create 3 ThreeVec objects
    a = b.Add(c); // add ThreeVec b and c, result is stored in a
    cout << a.Length() << endl;

    cout << b+c << endl;
    cout << 3*c << " = ";
    cout << c*3 << endl;

    return 0;
}

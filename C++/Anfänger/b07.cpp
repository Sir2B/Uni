#include "BigInt.h"
#include <iostream>
using namespace std;

int main()
{
   BigInt a = "234578997624315";
   BigInt b = "23987489367823";
   BigInt c = a + b;
   cout << c << endl;
   return 0;

}

// exceptions



#include <iostream>
using namespace std;

int main () {
  try
  {
    throw 20;           // error nr 20
  }
  catch (int e)
  {
    cout << "An exception occurred. Exception Nr. " << e << '\n';
  }
  return 0;
}

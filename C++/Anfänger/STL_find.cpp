#include <iostream>
#include <cstring>      // C std string ops
#include <algorithm>   // STL algorithms, find ...

using namespace std;
int main()
{
  char* s = "C++ is the better C";
  int len = strlen(s);
  char * where = find(&s[0],&s[len],'e');
  cout << *(where) << *(where+1) << endl;
};

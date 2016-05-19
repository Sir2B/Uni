#include <iostream>
#include <string>
using namespace std;
template < class T>        // declare template function
T Max(const T &x,const T &y)
{
  return (x < y ? y:x);
}
void templ()
{
  double a=3.2,b=4.2;
  int c=4,d=7;
  string s="Hallo",t="Hello";
  cout << "Max(a,b) :" << Max(a,b) <<  endl;
  cout << "Max(c,d) :" << Max(c,d) <<  endl;
  cout << "Max(s,t) :" << Max(s,t) <<  endl;
};

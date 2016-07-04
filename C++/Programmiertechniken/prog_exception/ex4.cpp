

// using standard exceptions		-- C++11
#include <iostream>
#include <exception>
using namespace std;

class myexception: public exception
{
  virtual const char* what() const noexcept
  {
    return "My exception happened";
  }
} myex;

int main () {
  try
  {
    throw myex;
  }
  catch (exception& e)
  {
    cout << e.what() << '\n';
  }
  return 0;
}

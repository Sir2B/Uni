#include <iostream>
#include <typeinfo>			// for typeid
#include <string>

int zero = 0;

int fun() { return zero; }

int& fun2() {return zero;}

int* fun3() { return &zero;}

int main() {
  
  
  
  auto x = 0;               // OK, x is of type int
  const auto y = 0.;        // OK, y is of type const double -- note however the conversion due to cout below
  //y = 5.;                 // Error
  //auto z;                 // Error!
  auto s = std::string("Hello, world!");      //OK
  auto p = &y;              // OK -- pointer to constant double

  auto iarr = {1,2,3,4};	// OK -- int[4]

  auto f = fun();           // OK -- f is of type int
  auto f2 = fun2();         // p2 is of type int, not int& -- use auto& f2bis = fun2() instead
  auto pf = fun3();         // pf is of type int*

  // the result is compiler-dependent.
  // if you exectute .a.out | c++filt you will get readable answers
  std::cout << typeid(x).name() << " " << typeid(y).name() << " " << typeid(s).name() << " " << typeid(p).name() << " " << typeid(iarr).name() << " " << typeid(f).name() << " " << typeid(f2).name() << " " << typeid(pf).name()  << "\n";

  return 0;
}


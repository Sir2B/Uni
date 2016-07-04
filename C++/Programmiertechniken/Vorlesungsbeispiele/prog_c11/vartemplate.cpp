#include <iostream>
#include <string>

using namespace std;

// for a class or struct
template<class ... Types> struct Tuple {};      // the std::tuple is defined with variadic templates

// for a function
template<class ... Types> void f(Types ... args) {};    // uses ... to unpack

// example 1
template<typename T>                            // variadic templates are very often used recursively
T adder(T v) {
  return v;
}

template<typename T, typename... Args>
T adder(T first, Args... args) {
  return first + adder(args...);
}

// example 2

template<typename T>
bool pair_comparer(T a, T b) {
  // In real-world code, we wouldn't compare floating point values like
  // this. It would make sense to specialize this function for floating
  // point types to use approximate comparison.
  return a == b;
}

template<typename T, typename... Args>              // variadic templates are very often used recursively
bool pair_comparer(T a, T b, Args... args) {
  return a == b && pair_comparer(args...);
}


int main() {
  Tuple<> t0;           // Types contains no arguments
  Tuple<int> t1;        // Types contains one argument: int
  Tuple<int, float> t2; // Types contains two arguments: int and float
  //Tuple<0> error;       // error: 0 is not a type

  f();       // OK: args contains no arguments
  f(1);      // OK: args contains one argument: int
  f(2, 1.0); // OK: args contains two arguments: int and double

  long sum = adder(1, 2, 3, 8, 7);

  std::string s1 = "x", s2 = "aa", s3 = "bb", s4 = "yy";
  std::string ssum = adder(s1, s2, s3, s4);


  std::cout << ssum << "\n";
 
  std::cout << pair_comparer(1.5, 1.5, 2, 2, 6, 6) << "\n";

  return 0;
}

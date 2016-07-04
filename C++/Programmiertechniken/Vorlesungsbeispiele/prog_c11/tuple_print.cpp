// a way to iterate over all elements of a tuple and print them to the screen
#include <iostream>
#include <tuple>

using namespace std;

// Define a type which holds an unsigned integer value 
template<size_t> struct int_{};

// templated function for printing an element of a tuple + recursion via template arguments
// note the use of tupe_size<Tuple>::value
template <class Tuple, size_t Pos>
ostream& print_tuple(ostream& out, const Tuple& t, int_<Pos> ) {
  out << get< tuple_size<Tuple>::value-Pos >(t) << ',';
  return print_tuple(out, t, int_<Pos-1>() );
}

// template specialziation when there is only one element
template <class Tuple>
ostream& print_tuple(ostream& out, const Tuple& t, int_<1> ) {
  return out << get<tuple_size<Tuple>::value-1>(t);
}

template <class... Args>
ostream& operator<<(ostream& out, const tuple<Args...>& t) {
  out << '('; 
  print_tuple(out, t, int_<sizeof...(Args)>()); 
  return out << ')';
}

int main() {
  auto t1 = make_tuple( 10, 3.4f, "awesomeness" );
  cout  << t1 << "\n";
  return 0;
}

#include <iostream>



// example of template metaprogramming
// the factorial is computed at compile time!

template <unsigned int n>
struct factorial {
	enum { value = n * factorial<n - 1>::value };
};

template <>
struct factorial<0> {
	enum { value = 1 };
};


int main() {
  std::cout << factorial<0>::value << "\n";
  std::cout << factorial<4>::value << "\n";
}

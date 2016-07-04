#include <iostream>
#include <array>


constexpr
int fac(const int n) noexcept {
  return n==1? 1 : n *fac(n-1);
}

int main() {
    
  int i;                                // non-const
  //constexpr auto ArraySize1 = i;		// error, i not known at compile time
  //std::array<int, ArraySize1> m1;		// error, same problem
  constexpr auto ArraySize2 = 10;		// OK
  std::array<int, ArraySize2> m2;		// OK

  std::array<int, fac(4)> m3;			// OK
  
}

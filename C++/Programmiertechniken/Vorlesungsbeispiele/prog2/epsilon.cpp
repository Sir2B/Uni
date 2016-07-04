#include<iostream>
#include<limits>

int main() {
  std::cout << "machine precision of float       : " << std::numeric_limits<float>::epsilon() << "\n"; 
  std::cout << "machine precision of double      : " << std::numeric_limits<double>::epsilon() << "\n"; 
  std::cout << "machine precision of long double : " << std::numeric_limits<long double>::epsilon() << "\n"; 
  return 0;
}

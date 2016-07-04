// exception constructor. from cplusplus.com -- C++11
#include <iostream>       // std::cout
#include <exception>      // std::exception

struct ooops : std::exception {
  const char* what() const noexcept {return "Ooops!";}
};

int main () {
  ooops e;
  std::exception* p = &e;
  try {
    throw e;       // throwing copy-constructs: ooops(e)
  } catch (std::exception& ex) {
    std::cout << ex.what() << "\n";
  }
  try {
    std::cerr << p->what() << "\n";
    throw *p;      // throwing copy-constructs: std::exception(*p)
  } catch (std::exception& ex) {
    std::cout << ex.what() << "\n";
  }
  return 0;
}



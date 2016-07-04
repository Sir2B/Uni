#include <iostream>
#include <exception>

class Object_t : public std::exception {
public:
  Object_t () {std::cout << "Ctor of Object_t called\n";}
  Object_t (const Object_t& rhs) {std::cout << "Copy-ctor of Object_t called\n";}
  const char* what() const noexcept { return "absolutely crazy error";}

};

int main() {
  Object_t obj;
  try {
    throw obj;
  }
  catch (std::exception& exc) {
    std::cerr << "# an error occurred of type " << exc.what() << "\n";
  }
  return 0;

}

// make_pair example
#include <utility>      // std::pair
#include <iostream>     // std::cout

int main () {
  std::pair <int,int> foo;
  std::pair <int,int> bar;
  std::pair <int, char> baz;

  foo = std::make_pair (10,20);
  bar = std::make_pair (10,'A'); // ok: implicit conversion from pair<int,char>
  baz = std::make_pair (10,'A');
  

  std::cout << "foo: " << foo.first << ", " << foo.second << '\n';
  std::cout << "bar: " << bar.first << ", " << bar.second << '\n';
  std::cout << "baz: " << baz.first << ", " << baz.second << '\n';

  return 0;
}

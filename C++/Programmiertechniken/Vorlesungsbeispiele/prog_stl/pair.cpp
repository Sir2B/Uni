#include <iostream>
#include <utility>

int main() {
  std::pair <int,int> foo;
  std::pair <int,int> bar;
  std::pair <int,char> baz;
  std::pair<double, double> oof(15.0, 3.5);

  foo = std::make_pair (10,20);
  bar = std::make_pair (10.5,'A'); // ok: implicit conversion from pair<double,char>
  baz = std::make_pair (10.5,'A');

  std::cout << "foo: " << foo.first << ", " << foo.second << '\n';
  std::cout << "bar: " << bar.first << ", " << bar.second << '\n';
  std::cout << "baz: " << baz.first << ", " << baz.second << '\n';
  std::cout << "oof: " << oof.first << ", " << oof.second << '\n';
  return(0);
}

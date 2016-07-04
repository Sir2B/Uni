// virtual vs non-virtual
#include <iostream>
#include <string>
using namespace std;

class Polygon {
protected:
  int width, height;
public:
  void set_values (const int a, const int b) { width=a; height=b; }
  int area() const {return width*height;}
  void print() { std::cout << " I am polygon\n";}
  void print(const int color) { std::cout << " I am " << color << " polygon\n";}
};


class Rectangle: public Polygon {
public:
  int area () const { return (width * height); }
  void print(std::string& s) { std::cout << " I am " << s << " Rectangle\n";}
};

int main () {
  Polygon poly;
  Rectangle rect;
  poly.set_values(4,5);
  rect.set_values(5,6);
  std::string s = "beautiful";
  rect.print(s);
  // rect.print();          // error
  // rect.print(1);         // error
  poly.print(5);
  poly.print();
  return 0;
}





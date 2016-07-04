// virtual vs non-virtual
#include <iostream>
using namespace std;

class Polygon {
protected:
  int width, height;
public:
  void set_values (const int a, const int b) { width=a; height=b; }
  int area() const {return width*height;}
  void print() { std::cout << " I am polygon\n";}
};

class Polygon_abstract {
protected:
  int width, height;
public:
  void set_values (const int a, const int b) { width=a; height=b; }
  int area() const {return width*height;}
  virtual void print() = 0;
};


class Rectangle: public Polygon {
public:
  int area () const { return (width * height); }
  void print() { std::cout << " I am Rectangle\n";}
};

class Triangle: public Polygon {
public:
  int area () const { return (width * height / 2); }
  void print() { std::cout << " I am Triangle\n";}
};

class Rectangle_bis: public Polygon_abstract {
public:
  int area () const { return (width * height); }
  void print() { std::cout << " I am Rectangle\n";}
};

class Triangle_bis: public Polygon_abstract {
public:
  int area () const { return (width * height / 2); }
  void print() { std::cout << " I am Triangle\n";}
};


void static_print(Polygon p) {
  p.print();      // always invokes print of Polygon, never of a derived class (compile time binding)
}


void dynamic_print(Polygon* p) {
  p->print();     // always invokes print of Polygon, never of a derived class (compile time binding)
}

void dynamic_print(Polygon_abstract* p) {
  p->print();     // run-time binding
}

int main () {
  Polygon poly;
  Rectangle rect;
  Triangle trgl;
  poly.set_values(4,5);
  rect.set_values(5,6);
  trgl.set_values(6,7);
  static_print(poly);
  static_print(rect);
  static_print(trgl);
  dynamic_print(&poly);
  dynamic_print(&rect);
  dynamic_print(&trgl);
  
  cout << "\n\n"; 
  
  Rectangle_bis rect2;
  Triangle_bis trgl2;
  rect2.set_values(5,6);
  trgl2.set_values(6,7);
  dynamic_print(&rect2);
  dynamic_print(&trgl2);
  return 0;
}

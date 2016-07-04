// example on copying/assigning with "slicing"
#include <iostream>
using namespace std;

class Polygon {
protected:
  int width, height;
public:
  void set_values (const int a, const int b) { width=a; height=b; }
  int area() const {return width*height;}
};

class Rectangle: public Polygon {
public:
  int area () const { return (width * height); }
  void set_color(const int cl) { color = cl;}
  int get_color() const {return color;}
private:
  int color;
};

class Triangle: public Polygon {
public:
  int area () const { return (width * height / 2); }
  void set_color(const int cl) { color = cl;}
  int get_color() const {return color;}
private:
  int color;
};

int main () {
  enum colors {blue, green};
  Polygon poly;
  Rectangle rect;
  Triangle trgl;
  poly.set_values(4,5);
  rect.set_values(5,6);
  trgl.set_values(6,7);
  rect.set_color(blue);
  trgl.set_color(green);
  poly = rect;
  cout << poly.area() << "\n";
  //cout << poly.get_color() << '\n';       // Error!
  Polygon * poly2 = &rect;
  cout << poly2->area() << "\n";

  return 0;
}

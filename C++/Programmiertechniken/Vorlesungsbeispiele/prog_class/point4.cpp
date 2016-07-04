


#include <iostream>
#include <cmath>

using namespace std;

class Point {
public:
  Point(double x=0, double y=0) { x_ = x; y_ = y; Npoints++;}
  ~Point() {Npoints--;}
  double dist() const { return sqrt(x_*x_ + y_ * y_);}
  static int Npoints;
private:
  double x_;
  double y_;
};

int Point::Npoints = 0;			// must be outside the class body and any function

int main() {
  Point p1(1.,1.);		// functional form
  cout << "There are " << Point::Npoints << " points in the plane\n";
  Point *p2 = new Point(2., 2.);
  cout << "There are " << p1.Npoints << " points in the plane\n";
  cout << "There are " << p2->Npoints << " points in the plane\n";
  delete p2;
  cout << "There are " << Point::Npoints << " points in the plane\n";
  return 0;
}


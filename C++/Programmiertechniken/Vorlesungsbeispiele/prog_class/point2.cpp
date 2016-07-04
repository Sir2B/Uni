


#include <iostream>
#include <cmath>

using namespace std;

class Point {
public:
  //Point(double x, double y) : x_(x) { y_ = y;}
  //Point(double x, double y) { x_ = x; y_ = y;}
  Point(double x, double y) : x_(x), y_(y) {};
  double dist() const { return sqrt(x_*x_ + y_ * y_);}
private:
  double x_;
  double y_;
};


int main() {
  Point p1(1.,1.);		
  cout << "Distance :  " << p1.dist() << "\n";
  return 0;
}


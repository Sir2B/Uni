


#include <iostream>
#include <cmath>

using namespace std;

class Point {
public:
  Point(double x, double y) : x_(x) { y_ = y;}
  double dist() const { return sqrt(x_*x_ + y_ * y_);}
private:
  double x_;
  double y_;
};

class StraightLine {
public:
  StraightLine(double x1, double y1, double x2, double y2) : p1(x1,y1), p2(x2,y2) { slope = (x2 == x1 ? 1e9 : (y2-y1)/(x2-x1));}
  double get_slope() const { return slope;}
private:
  Point p1;
  Point p2;
  double slope;
};



int main() {
  StraightLine X(1.0, 0.0, 0.0, 1.0);
  cout << "slope : " << X.get_slope() << "\n";
  return 0;
}


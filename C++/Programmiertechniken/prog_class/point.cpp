


#include <iostream>
#include <cmath>

using namespace std;

class Point {
public:
  Point(double x=0, double y=0) { x_ = x; y_ = y;}
  double dist() const { return sqrt(x_*x_ + y_ * y_);}
private:
  double x_;
  double y_;
};


int main() {
  Point p1(1.,1.);		// functional form
  Point p2 = p1;	
  Point p3 {2.0, 3.0};		// uniform intializaiton  
  Point p4 = {2.5, 3.5};	// equivalent
  Point p5;
  Point p6{};
  cout << "Distance :  " << p1.dist() << " " << p2.dist() << " " << p3.dist()
       << " " << p4.dist() << " " << p5.dist() << " " << p6.dist() << "\n";
  return 0;
}


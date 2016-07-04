


#include <iostream>
#include <cmath>

using namespace std;

class Point {
public:
  Point(double x, double y) { x_ = x; y_ = y;}
  double dist() const { return sqrt(x_*x_ + y_ * y_);}          // example of a const member function
  double get_x() const { return x_;}
    
  const double& get_x() { return x_;}                           // example of a return type const&
  
    
  double get_y() { return y_;}
  const double& get_y() const { return x_;}                     // example of a const member function
                                                                // and a return type const&
  double x_;
  double y_;
};


void print (const Point& p) {
  cout << p.get_x() << " " << p.get_y() << "\n";
}

int main() {
  const Point p(5., 4.);		// example of const object of class Point
  //p.x_ = 4.;				// error!
  cout << "Distance :  " << p.dist() << "\n";
  print(p);
  return 0;
}



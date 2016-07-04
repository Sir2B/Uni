


#include <iostream>
#include <cmath>

using namespace std;

template<class T>
class Point {
public:
  Point(double x=0, double y=0) { x_ = x; y_ = y;}
  double dist() const { return sqrt(x_*x_ + y_ * y_);}
private:
  double x_;
  double y_;
};

template<>
class Point<unsigned int> {
public:
  Point(unsigned int x=0, unsigned y=0) { x_ = x; y_ = y;}
  unsigned int dist() const { return x_ + y_;} // Manhattan distance
private:
  unsigned x_;
  unsigned y_;
};


int main() {
  Point<unsigned int> p(1,1);		
  cout << "Distance " << p.dist() << "\n";
  return 0;
}


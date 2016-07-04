


#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#if __cplusplus > 199711L
#include <tuple>
#endif

using namespace std;

template<class T>
class Point {
public:
  Point(double x=0, double y=0) { x_ = x; y_ = y;}
  Point (const Point& p) { x_ = p.x_; y_ = p.y_;}
  Point& operator=(const Point& p) {x_ = p.x_; y_ = p.y_; return *this;}
  double dist() const { return sqrt(x_*x_ + y_ * y_);}
  
  bool operator==(const Point& p) {
    return ((x_ == p.x_) && (y_ == p.y_));
  }

  template<class U>
  friend bool operator<(const Point<U>&, const Point<U>&);
  
  template<class U>
  friend std::ostream& operator<<(std::ostream& os, const Point<U>& p) {os << "(" << p.x_ << "," << p.y_ << ")"; return os;}
  
private:
  double x_;
  double y_;

};



#if __cplusplus > 199711L

template <class T>
bool operator<(const Point<T>& p1, const Point<T>& p2) {
  return (tie(p1.x_, p2.x_) < tie(p2.x_, p2.y_)); 
}

#else

template <class T>
bool operator<(const Point<T>& p1, const Point<T>& p2) {
  if (p1.x_ < p2.x_) return true;
  if ((p1.x_ == p2.x_) && (p1.y_ < p2.y_)) return true;
  return false;
}

#endif


int main() {
  Point<unsigned int> p1(1,1);		
  Point<unsigned int> p2(2,1);		
  Point<unsigned int> p3(1,3);		
  cout << (p1 < p1) << " " << (p1 < p2) << " " << (p1 < p3)  << "\n";
  
  cout << (p1 == p2) << "\n";

  vector<Point<unsigned int> > v;
  v.resize(3); 
  v[0] = p1; v[1] = p2; v[2] = p3;
  sort(v.begin(), v.end());
  for (vector<Point<unsigned int> >::iterator it = v.begin(); it != v.end(); ++it) cout << it->dist() << " "; cout << "\n"; 
  
  cout << "p1 = " << p1 << "\n";
  return 0;
}


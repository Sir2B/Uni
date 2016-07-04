


#include <iostream>
#include <cmath>

using namespace std;

class fun {
public:
  double operator() (double x) { return x*exp(-x);}
};

template <class T, class F>
T integrate(F f, T a, T b, unsigned int N) {
    T res=T(0);
    T x=a;
    T dx=(b-a)/N;
    for (unsigned int i=0; i<N; ++i) {
      res +=f(x);
      x += dx;
    }
    return (res*dx);
}


int main() {
  cout << integrate(fun(), 0. ,1., 1000) << "\n";
  return 0;
}

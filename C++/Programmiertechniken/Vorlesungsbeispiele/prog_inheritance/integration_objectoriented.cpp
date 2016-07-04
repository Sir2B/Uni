


#include <iostream>
#include <cmath>

using namespace std;

class Integrator {
public:
  Integrator() {}
  double integrate(double a, double b, unsigned int n);
  virtual double f(double) = 0;
};

double Integrator::integrate(double a, double b, unsigned int N) {
  double res=0;
  double x = a;
  double dx = (b-a)/N;
  for (unsigned int i=0; i<N; ++i) {
    res += f(x);
    x += dx;
  }
  return (res*dx);
}

class Func : public Integrator {
public:
  Func() {}
  double f(double x) { return x*exp(-x);} 
};


int main() {
  Func fun;
  cout << fun.integrate(0., 1., 1000) << "\n";
  return 0;
}




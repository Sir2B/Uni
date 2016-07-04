#include <iostream>
#include <cmath>

using namespace std;

double fun(const double x) {
  return exp(-x);
}

int foo(const double x) {
  return static_cast<int>(x*2);
}


// the integration routine
template<typename F, typename Prec>
double integrate(F& f, Prec a, Prec b, size_t steps)
{
  double s = 0;
  double h = (b-a)/steps;
  for (size_t i = 0; i < steps; ++i)
    s += f(a + i*h);			// this implies that () must be defined on f with arguments of type double
  return h*s;
}


int main() {
  cout << integrate(fun, 0., 1., 1000) << "\t" << 1-exp(-1.) << "\n";
  cout << integrate(foo, 0., 2., 20) << "\t" << 3 << "\n";
}

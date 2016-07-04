


#include <iostream>
#include <cmath>

using namespace std;

double fun(double x) {
  return x*exp(-x);
}

double integrate( double (*f) (double), double a, double b, unsigned int N)
  {
    double res = 0;
    double x = a;
    double dx = (b-a)/N;
    for (unsigned int i=0; i<N; ++i) {
      res += f(x);
      x += dx;
    }
    return (res*dx);
}

int main() {
  cout << integrate(fun, 0.,1., 1000) << "\n";
  return 0;
}




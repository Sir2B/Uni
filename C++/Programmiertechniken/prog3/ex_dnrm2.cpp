// g++ dnrm2.cpp -lblas
#include <iostream>

extern "C" double dnrm2_(int* n, double* x, int* incx);

int main() {
  const int N = 10;
  double vec[N];
  for (unsigned int n=0; n < N;n++) vec[n] = 1.0;
  int vecsize = N;
  int incx = 1;
  std::cout << "norm of vector : " << dnrm2_(&vecsize, vec, &incx) << "\n";
  return 0;
}

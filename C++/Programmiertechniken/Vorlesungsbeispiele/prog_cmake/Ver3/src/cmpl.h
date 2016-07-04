


#ifndef GUARD_CMPL_
#define GUARD_CMPL_
#ifndef pi
#define pi 3.14159265359
#endif


// cmpl.h
struct cmpl {
  double real_;
  double imag_;
};

double get_modulus_squared(const cmpl&);
double get_arg(const cmpl&);
cmpl addition(const cmpl&, const cmpl&);

#endif




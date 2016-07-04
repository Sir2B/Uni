

#include <assert.h>
#include <cmath>
#include <iostream>
#include "cmpl.h"

double get_modulus_squared(const cmpl& c) {
  return c.real_ * c.real_ + c.imag_ * c.imag_;
}

double get_arg(const cmpl& c) {
  // we want a value between [0, 2pi[, there is a branch cut on the positive x-axis which should be excluded
  assert (!(c.real_ == 0 && c.imag_ == 0)); 
  assert (!(c.imag_ == 0 && c.real_ > 0));
  double phase = (c.imag_ < 0 ? 2*pi : 0);
  return std::atan2(c.imag_ , c.real_) + phase;	// atan2 returns a value between [-pi, pi[
}


// for proper use of templates, classes and constness : see later in the course 

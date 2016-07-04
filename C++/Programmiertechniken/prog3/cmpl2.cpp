
// cmpl2.cpp
#include "cmpl.h"

cmpl addition(const cmpl& c1, const cmpl& c2) {
  cmpl c;
  c.real_ = c1.real_ + c2.real_;
  c.imag_ = c1.imag_ + c2.imag_;
  return c;
}





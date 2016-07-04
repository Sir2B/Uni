#include <iostream>
#include <cmath>
#include "cmpl.h"

using namespace std;


int main() {
  cmpl MyComplexNumber;
  double argm;
  MyComplexNumber.real_ = 1.;
  MyComplexNumber.imag_ = 1.;
  cout << "A complex number " << MyComplexNumber.real_ << " + i " << MyComplexNumber.imag_ << "\n";
  cout << "modulus squared : " << get_modulus_squared(MyComplexNumber) << "\n";
  argm = get_arg(MyComplexNumber);
  cout << "argument : " << argm << " in degrees : "  << argm / (2 * pi) * 360 << "\n";
  //MyComplexNumber.imag_ = 0;
  //argm = get_arg(MyComplexNumber);
  
  return 0; 

}


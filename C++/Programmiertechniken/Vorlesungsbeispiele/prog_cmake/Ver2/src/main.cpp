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
  
  MyComplexNumber.real_ = -1.;
  MyComplexNumber.imag_ = 1.;
  cout << "A complex number " << MyComplexNumber.real_ << " + i " << MyComplexNumber.imag_ << "\n";
  cout << "modulus squared : " << get_modulus_squared(MyComplexNumber) << "\n";
  argm = get_arg(MyComplexNumber);
  cout << "argument : " << argm << " in degrees : "  << argm / (2 * pi) * 360 << "\n";
  
  MyComplexNumber.real_ = -1.;
  MyComplexNumber.imag_ = -1.;
  cout << "A complex number " << MyComplexNumber.real_ << " + i " << MyComplexNumber.imag_ << "\n";
  cout << "modulus squared : " << get_modulus_squared(MyComplexNumber) << "\n";
  argm = get_arg(MyComplexNumber);
  cout << "argument : " << argm << " in degrees : "  << argm / (2 * pi) * 360 << "\n";
  

  MyComplexNumber.real_ = 1.;
  MyComplexNumber.imag_ = -1.;
  cout << "A complex number " << MyComplexNumber.real_ << " + i " << MyComplexNumber.imag_ << "\n";
  cout << "modulus squared : " << get_modulus_squared(MyComplexNumber) << "\n";
  argm = get_arg(MyComplexNumber);
  cout << "argument : " << argm << " in degrees : " << argm / (2 * pi) * 360 << "\n";
  

  MyComplexNumber.real_ = -1.;
  MyComplexNumber.imag_ = 0.;
  cout << "A complex number " << MyComplexNumber.real_ << " + i " << MyComplexNumber.imag_ << "\n";
  cout << "modulus squared : " << get_modulus_squared(MyComplexNumber) << "\n";
  argm = get_arg(MyComplexNumber);
  cout << "argument : " << argm << " in degrees : " << argm / (2 * pi) * 360 << "\n";


  cmpl MyComplexNumber_bis;
  MyComplexNumber_bis.real_ = 0.5;
  MyComplexNumber_bis.imag_ = -0.5;
  cout << "A complex number " << MyComplexNumber.real_ << " + i " << MyComplexNumber.imag_ << "\n";
  cout << "A complex number " << MyComplexNumber_bis.real_ << " + i " << MyComplexNumber_bis.imag_ << "\n";
  cmpl MyComplexNumber_sum = addition(MyComplexNumber, MyComplexNumber_bis);
  cout << "Adding two complex numbers : ";
  cout << MyComplexNumber_sum.real_ << " + i " << MyComplexNumber_sum.imag_ << "\n";
  cout << "modulus squared : " << get_modulus_squared(MyComplexNumber_sum) << "\n";
  argm = get_arg(MyComplexNumber_sum);
  cout << "argument : " << argm << " in degrees : " << argm / (2 * pi) * 360 << "\n";
  
  /*
  MyComplexNumber.real_ = 1.;
  MyComplexNumber.imag_ = 0.;
  cout << "A complex number " << MyComplexNumber.real_ << " + i " << MyComplexNumber.imag_ << "\n";
  cout << "modulus squared : " << get_modulus_squared(MyComplexNumber) << "\n";
  argm = get_arg(MyComplexNumber);
  cout << "argument : " << argm << " in degrees : " << argm / (2 * pi) * 360 << "\n";
  */

}


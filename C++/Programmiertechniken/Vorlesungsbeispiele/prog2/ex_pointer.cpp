

#include <iostream>
using namespace std;
int main() {
    
  int x1 = 3;
  int y1 = 5;
       
  /* pointer notation */
  int *p;  // also correct is int* p. p is now a pointer to int, but still uninitialized
  p = &x1;  // & takes the address of a variable

  *p = 1;  // * dereferences a pointer. Note that x1 is now set to 1
  std::cout << "x1 = " << x1 << std::endl;

  // Pointers can be dangerous to use:
  // p = 1; *p = 258; // this compiles but will most likely crash
  // style note: raw pointers should be avoided when possible ( and this almost always )
  // the risk of catastrophic errors otherwise is too great


  /* array */
  double v[10];  // allocates memory for 10 numbers;
  for (int i=0; i < 10; ++i) v[i] = i*2. - 5;
  for (int i=0; i < 10; ++i) std::cout << "i = " << i << " v[i] = " << v[i] << std::endl;

  unsigned int n; std::cout << "Type a positive integer number :\n"; std::cin >> n;
  // float x[n];  // will not compile because n is not known at compile time

  // solution : dynamic allocation
  double *x;
  x = new double[n]; // allocate memory
  x[0] = 5.;
  delete [] x; // deleting the memory for the array; x[i] is now undefined
  // note that 'delete' is for variables, 'delete []' for arrays

  /* pointer artihmetic */
  std::cout << "Element 1 of v : " << v[1] << " " << *(v + 1) << std::endl; // v[n] is the same as *(p+n)
  std::cout << "Element 0 of v : " << *v << " " << *(&v[0]) << std::endl;   // v is in effect the address as its first element
  double* pv = v;
  for (int i=0; i < 10; i++) 
    std::cout << "Element " << i << " of v : " << *pv++ << std::endl;                  // increment and decrement also work

  // references
  double var1 = 5.;
  double &var2 = var1;        // var2 refers to the same memory allocation
  var2 = 4.;
  std::cout << "var 1 : " << var1 << "\tvar2 : " << var2 << std::endl;    // output is 4 4
  double var3 = 2;
  var2 = var3;
  std::cout << "var 1 : " << var1 << "\tvar2 : " << var2 << "\tvar3 : " << var3 << std::endl;    // output is 2 2 2
  var2 = 3.;
  std::cout << "var 1 : " << var1 << "\tvar2 : " << var2 << "\tvar3 : " << var3 << std::endl;    // output is 3 3 2
    
  return 0; 
}





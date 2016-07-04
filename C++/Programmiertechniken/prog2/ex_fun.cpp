


#include <iostream>
#include <vector>


void print_message() {
  std::cout << "Welcome to the program!\n";
  // no return value when the function is void
}

double square(double x) { // computes the square
  return x*x;
}

void increment(int i) { // pass by value : a copy of the parameter i is made (the same name i is irrelevant)
  i = i+1;	
  std::cout << "inside function increment i = " << i << std::endl; 	// the local copy is 5
} // now the local variable goes out of scope

void increment_bis(int& i) { // pass by reference : no local copy is made
  i = i+1; 
}


void increment_vector(std::vector<double>& v) {
  // pass by reference, this avoids copying large sets of data, but data may be modified
  // etc
}

void increment_vector(std::vector<double> const &v) {
  // this avoids copying large sets of data and v may not be modified
  // etc
}

void increment_tres(int* i) {
    // pass by pointer, rarely needed in C++. Also avoids copying the data but has the risk of raw pointers
    (*i) += 1;
}

int main() {
  print_message();  // note that the function must have been declared before
  double x = 2.;
  std::cout << "x = " << x << " square : " << square(x) << std::endl;
  int i = 4;
  std::cout << "in main before increment: i = " << i << std::endl;
  increment(i);
  std::cout << "in main after increment: i = " << i << std::endl; 	// still 4
  increment_bis(i);
  std::cout << "in main after increment_bis: i = " << i << std::endl; 	// now it is 5
  increment_tres(&i); // we have to provide the address of the variable
  std::cout << "in main after increment_bis: i = " << i << std::endl; 	// now it is 6
  // increment_bis(5); // will not compile because 5 is a literal constant
  return(0);
    
    
  int k;                        // declares variable to be of type int
  double foo(const int );       // declares function fun to return a double and take a const int as argument
  
  int y=4;
  //3 = x;                         // error! a constant literal cannot be considered an lvalue


}

double foo(const int i) { return i+1;}      // no function definitions inside another function




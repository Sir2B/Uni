#include <iostream>

using namespace std;

class MyClass_t {
public:
  // default constructor
  MyClass_t() { cout << "Default constructor called\n"; x_ = 0; y_ = 0;}
  // specific constructor
  MyClass_t(const double x, const double y) { cout << "Specific constructor called\n"; x_ = x; y_ = y;}
  // copy constructor
  MyClass_t(const MyClass_t& c) { cout << "Copy constructor called\n"; x_ = c.x_; y_ = c.y_;}
  // assignment operator
  MyClass_t& operator=(const MyClass_t& c) { cout << "Assignment operator called\n"; x_ = c.x_; y_ = c.y_;}
  // destructor
  ~MyClass_t() { cout << "Destructor called\n";}
 
  // operator +
  friend MyClass_t operator+(const MyClass_t&, const MyClass_t&);
  
  //operator +=
  MyClass_t& operator+=(const MyClass_t& c2) {
    x_ += c2.x_;
    y_ += c2.y_;
    return *this;
  }
  
  friend double norm_sq(const MyClass_t c) { return (c.x_ * c.x_ + c.y_ * c.y_); }

private:
  double x_;
  double y_;
};

// operator +
MyClass_t operator+(const MyClass_t& c1, const MyClass_t& c2) {
  MyClass_t c_new;
  c_new.x_ = c1.x_ + c2.x_;
  c_new.y_ = c1.y_ + c2.y_;
  return c_new;
}


int main() {
  std::cout << "\n# Variable 1 : ";
  MyClass_t var1;


  std::cout << "\n# Variable 2 : ";
  MyClass_t var2(4.0, 4.0);
  
  
  std::cout << "\n# Variable 3 : ";
  MyClass_t var3 = var1;
  //MyClass_t var3b(var1);
  //MyClass_t& var3 = var1; 			// and now?
  
  
  std::cout << "\n# Variable 4 : ";
  MyClass_t var4;
  var4 = var2;
  
  
  std::cout << "\n# sum : ";
  var3 = var1 + var2;
  
  
  
  std::cout << "\n# operator += : ";
  var4 += var1;
  

  std::cout << "\n# Finishing...";

}


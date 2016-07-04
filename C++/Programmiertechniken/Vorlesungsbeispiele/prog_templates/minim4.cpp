
//#include <iostream>




template <typename R, typename U, typename T>
R const min(U const& x, T const& y) {
  return (x < y ? static_cast<R>(x) : static_cast<R>(y));
}

int main() {
  int a = 5;
  double b = 3.4;
  
  min<int>(a,b);      // OK   -- yields 3
  min<double>(a,b);   // OK   -- yields 3.4
  
  
  //std::cout << min<int>(a,b) << "\n";      // OK
  //std::cout << min<double>(a,b) << "\n";   // OK

    
    
}




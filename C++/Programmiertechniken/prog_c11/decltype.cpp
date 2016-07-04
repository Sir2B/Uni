#include <iostream>
#include <utility>          // for std::declval

template <typename T>
struct Cmpl {
  T x;
  T y;
};



// std::declval : Converts any type T to a reference type, making it possible to use member functions in decltype expressions without the need to go through constructors. declval is commonly used in templates where acceptable template parameters may have no constructor in common, but have the same member function whose return type is needed. Note that because no definition exists for declval, it can only be used in unevaluated contexts; it is an error to evaluate an expression that contains this function.

template<typename U, typename V>
auto operator+(const Cmpl<U> c1, const Cmpl<V> c2) -> Cmpl<decltype(std::declval<U>() + std::declval<V>() ) >    {
    Cmpl<decltype(std::declval<U>() + std::declval<V>() ) > result;
    result.x = c1.x + c2.x;
    result.y = c1.y + c2.y;
    return result;
}


/*
// this would also work but is ovbiously less elegant
template<typename U, typename V>
auto operator+(const Cmpl<U> c1, const Cmpl<V> c2) -> Cmpl<decltype(c1.x + c2.x)> {
  Cmpl<decltype(c1.x + c2.x) > result;
  result.x = c1.x + c2.x;
  result.y = c1.y + c2.y;
  return result;
}
*/

/*
// this does not work if c1 and c2 are Cmpl<type> of different type
template<typename U>
Cmpl<U> operator+(const Cmpl<U> c1, const Cmpl<U> c2)   {
  Cmpl<U> result;
  result.x = c1.x + c2.x;
  result.y = c1.y + c2.y;
  return result;
}
*/


template<typename T, typename U>
auto add(T t, U u) -> decltype(t + u) { // return type depends on template parameters
  return t+u; 
}

int main() 
{
    
  int i = 10;
  decltype(i) j = i * 5;		// j is an int

   
  Cmpl<double> c = {1.0, 0.5};
  decltype (c.x) z;			// z is a double

  Cmpl<int> c2 = {2, 0};

  int s1 = add(i,j);

  auto s2 = add(c,c2);
    
  auto s3 = add(1, 4.5);

  std::cout << " i = " << i << " j= " << j << " i+j = " << s1 << "\n";
  std::cout << "( " << s2.x << " ,  " << s2.y << " )" << "\n";
  std::cout << s3 << "\n";

  return 0;
} 

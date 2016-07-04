#include <iostream>


template <class T>
inline T Mymin(T x, T y) {
  return (x < y ? x : y);
}

template <>
char Mymin(char x, char y) {
  char x1= ((x>='a')&&(x<='z')) ? x + 'A'-'a' : x;
  char y1= ((y>='a')&&(y<='z')) ? y + 'A'-'a' : y;
  return x1 < y1 ? x : y;
}

int main() {
  char a = 'a';
  char b = 'b';
  std::cout << Mymin(a,b) << "\n";

  char c = 'A';
  std::cout << Mymin(c,b) << "\n";  
  return 0;
}




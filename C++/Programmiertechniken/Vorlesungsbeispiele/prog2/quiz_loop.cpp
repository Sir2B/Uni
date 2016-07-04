#include <iostream>

using namespace std;

int main() {
  std::cout << "Enter a number: "; unsigned int n;
  std::cin >> n;
    
  // loop nr 1
  for (int i=1;i<=n;++i)
    cout << i << "\n";
  
  // loop nr 2
  int i=0;
  while (i<n)
    std::cout << ++i << "\n";
  
  // loop nr 3
  i=1; 
  do
    std::cout << i++ << "\n";
  while (i<=n);
  
  // loop nr 4
  i=1;
  while (true) {
   if(i>n) break;
    std::cout << i++ << "\n";
  }
}

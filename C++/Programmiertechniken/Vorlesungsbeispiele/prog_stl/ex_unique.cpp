#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    
    
  int myints[] = {0,7,5,6,1,2,2,3,4,7,4,3,3,3};
  std::vector<int> v (myints, myints + sizeof(myints) / sizeof(int) );
  std::sort(v.begin(), v.end()); // 0	1	2	2	3	3	3	3	4	4	5	6	7	7
  std::vector<int>::iterator last = std::unique(v.begin(), v.end()); // 0 1 2 3 4 5 6 7 x x x x x x
  v.erase(last, v.end());  // remove indeterminate elements
    
    
    
  for (std::vector<int>::iterator it = v.begin(); it != v.end(); ++it) std::cout << *it << "\t";
  std::cout << std::endl;
  return 0;
}



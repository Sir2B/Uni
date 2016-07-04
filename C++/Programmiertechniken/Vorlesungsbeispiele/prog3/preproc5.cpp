


#include <iostream>
#define MAX(a, b) ((a) < (b) ? (b) : (a))

using std::cout;

int main() {
  int i = 5;
  int j = 6;
  cout << "Max : " << MAX(i,j) << "\n";			// example of a macro
  // this is however dangerous because macros do not evaluate their arguments 
  int z = MAX(i++,j++);
  cout << i << " " << j << " " << z << "\n";		// what is the output? Is this what was intended?
  return 0;
}


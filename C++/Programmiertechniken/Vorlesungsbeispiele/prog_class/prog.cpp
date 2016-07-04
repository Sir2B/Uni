#include <iostream>
//#include "vec.hpp"
#include "live.hpp"

using namespace std;

int main() {
  Vec<int> v1(100, 1);		// specific constructor

  Vec<int> v2 = v1;		// copy constructor
  Vec<int> v3(v1);		// copy constructor
  
  Vec<int> v4;			// default constructor
  v4 = v1;			// assignment
  v4.operator=(v1);		// identical to previous line
  for (Vec<int>::const_iterator it = v1.begin(); it != v1.end(); ++it) cout << *it << " "; cout << "\n"; 
  for (Vec<int>::const_iterator it = v2.begin(); it != v2.end(); ++it) cout << *it << " "; cout << "\n"; 
  for (Vec<int>::const_iterator it = v3.begin(); it != v3.end(); ++it) cout << *it << " "; cout << "\n"; 
  for (Vec<int>::const_iterator it = v4.begin(); it != v4.end(); ++it) cout << *it << " "; cout << "\n"; 

  //operator+= and operator+
  Vec<int> v5(50, 2);
  v1 += v5;
  cout << "# v1 : ";
  for (Vec<int>::const_iterator it = v1.begin(); it != v1.end(); ++it) cout << *it << " "; cout << "\n"; 
  
  cout << "# v5 : ";
  for (Vec<int>::const_iterator it5 = v5.begin(); it5 != v5.end(); ++it5) cout << *it5 << " "; cout << "\n";
    
  Vec<int> v6 = v1 + v5;
  cout << "# v6 = v1 + v5 : ";
  for (Vec<int>::const_iterator it = v6.begin(); it != v6.end(); ++it) cout << *it << " "; cout << "\n";

  //operator *=
  v6 *= 4;
  cout << "# v6 = v6 * 4 : ";
  //for (Vec<int>::const_iterator it = v6.begin(); it != v6.end(); ++it) cout << *it << " "; cout << "\n";
  // ostream
  cout << v6 << "\n";
}

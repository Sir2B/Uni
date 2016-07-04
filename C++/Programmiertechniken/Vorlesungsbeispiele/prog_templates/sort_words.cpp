#include <iostream>  
#include <algorithm>  
#include <vector>  
#include <string>  
#include <iterator> 
 
using namespace std;   
int main() 
{ 
  vector<string> data; 
  copy(istream_iterator<string>(cin), istream_iterator<string>(), back_inserter(data));  
  sort(data.begin(), data.end()); 
  copy(data.begin(), data.end(), ostream_iterator<string>(cout," ")); cout << "\n";
  // unique_copy(data.begin(), data.end(), ostream_iterator<string>(cout," "));
}



#include <iostream>
#include <vector>
#include <memory>
using namespace std;

int main() {
    
    
  unique_ptr<vector<int> > pVector(new vector<int>); 
  pVector->push_back(100); // Add 100  
  (*pVector)[0] = 200; // Dereferencing works as usual
    
  cout << (*pVector)[0] << "\n";


  unique_ptr<int> one(new int);
  *one = 1;
  unique_ptr<int> two;
  two = std::move(one);
  cout << "one : " << (one == nullptr ? "nullptr" : "1") << " two : " << *two << "\n"; 
   
  return 0; 
    
}

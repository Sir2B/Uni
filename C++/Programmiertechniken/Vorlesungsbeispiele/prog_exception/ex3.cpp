#include <iostream>
using namespace std;

int main() {
    
    
  try {
    try {
      throw 20;
    }
    catch (int n) {
      std::cout << "Error nr " << n << "\n";
      throw;
    }
  }
  catch (...) {
    cout << "Exception occurred\n";
  }
    
    
    
}

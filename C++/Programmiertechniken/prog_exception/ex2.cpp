#include <iostream>
using namespace std;

int main() {
    
    
  try {
    // comment any of the lines below and compare the output
    throw 'a';
    throw 5;
    throw 5.0; 
    cout << "This line will not be executed\n";
  }
  catch (int param) { cout << "int exception"; }
  catch (char param) { cout << "char exception"; }
  catch (...) { cout << "default exception"; }
    
    
}

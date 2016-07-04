// loop example; break and continue
#include <iostream>
using namespace std;

int main () {
  cout << "The for loop:\n";
  for (int n=10; n>0; n--) cout << n << " ";
  cout << "\n";
  
  cout << "The while loop:\n";
  int n = 10;
  while (n > 0) {
    cout << n << " ";
    n--;
  }
  cout << endl;
  
  cout << "The do loop:\n";
  n = 10;
  do {
    cout << n << " ";
    n--;
  } while (n > 0);
  cout << "\n";
  
  cout << "break:";
  for (int n=10; n>0; n--) {
    cout << n << " ";
    if (n==3) {
      cout << "countdown aborted!";
      break;
    }
  }
  
  cout << "\n";
  
  cout << "continue:";
  for (int n=10; n>0; n--) {
    if (n==3) {
      continue;
    }
    cout << n << " ";
  }
  cout << endl;
  
  
  return 0;
  
}

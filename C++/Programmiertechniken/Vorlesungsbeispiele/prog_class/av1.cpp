#include <iostream>
#include <vector>

using namespace std;

template <class T>
T average(const vector<T>& v) {
  T sum = 0;
  for (unsigned int n=0; n < v.size(); n++) sum += v[n];
  return sum/v.size();
}

int main() {
  vector<int> v(3);
  v[0] = 1; v[1] = 3; v[2] = 3;
  cout << average(v) << "\n";
  return 0; 
}

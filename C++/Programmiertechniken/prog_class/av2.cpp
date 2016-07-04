#include <iostream>
#include <vector>

using namespace std;

// general traits type
template <class T>
struct average_type {
  typedef T type;
};

// special cases
template<>
struct average_type<int> {
  typedef double type;
};

// repeat for all integer types : int32_t, int64_t, ...

template <class T>
typename average_type<T>::type average(const vector<T>& v) {
  typename average_type<T>::type sum = 0;
  for (unsigned int n=0; n < v.size(); n++) sum += v[n];
  return sum/v.size();
};

int main() {
  vector<int> v(3);
  v[0] = 1; v[1] = 3; v[2] = 3;
  cout << average(v) << "\n";
  return 0; 
}

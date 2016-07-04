#include <iostream>
#include <vector>
#include <limits>

using namespace std;


// first helper
template<class T, bool B>
struct helper {
  typedef T type;
};

// specialization in case type is integer
template<class T>
struct helper<T, true> {
  typedef double type;
};


// general traits type
template <class T>
struct average_type {
  typedef typename helper<T, numeric_limits<T>::is_integer>::type type;
};

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
  vector<double> v2(3);
  v2[0] = 1.; v2[1] = 3.; v2[2] = 3.;
  cout << average(v2) << "\n";
  return 0; 
}

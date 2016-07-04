#include <iostream>
#include <string>
#include <assert.h>

using namespace std;


template<typename T>
class Vec_t {
public:
  // construtor
  Vec_t() { cout << "Default Constructor of Vec_t called.\n"; data_ = nullptr; }
  Vec_t(const size_t n) : size_(n) { cout << "Constructor of Vec_t called.\n"; data_ = new T[size_];  }
  // copy constructor
  Vec_t(const Vec_t& rhs) : size_(rhs.size_) {
    cout << "Copy constructor of Vec_t called.\n";
    data_ = new T[size_];
    for (size_t j=0; j < size_; j++) data_[j] = rhs.data_[j];
  } 
  // copy-assignment operator
  Vec_t& operator=(const Vec_t& rhs) {
     if (&rhs != this) {
       cout << "Copy-operator= of Vec_t called\n";
       delete [] data_;
       size_ = rhs.size_;
       data_ = new T[size_];
       for (size_t j=0; j < size_; j++) data_[j] = rhs.data_[j];
     }
     return *this;
  }
  // destructor
  ~Vec_t() { cout << "Destructor of Vec_t called.\n"; delete [] data_;} 
  // operator[]
  T& operator[](size_t n) {return data_[n];}
  const T& operator[](size_t n) const { return data_[n];}
  // get functions
  size_t get_size() const { return size_;}
  // operator+
  template <typename U>
  friend Vec_t<U> operator+(const Vec_t<U>& v1, const Vec_t<U>& v2);
private:
  T* data_;
  size_t size_;
};

template <typename T>
Vec_t<T> operator+(const Vec_t<T>& v1, const Vec_t<T>& v2) {
  cout << "Operator+ on two Vec_t called.\n";
  Vec_t<T> newvec(v1.get_size());
  for (size_t j =0; j < newvec.get_size(); j++) newvec[j] = v1[j] + v2[j];
  cout << "There is no call to the copy constructor when \"return newvec\" is called thanks to (named) Return Value Optimization\n";
  return newvec;
}

template <typename T>
Vec_t<T> half(const Vec_t<T>& v1, const int b) {
  assert(v1.get_size() % 2 == 0);
  if (b) {
   Vec_t<T> newvec(v1.get_size()/2);
   for (size_t j =0; j < newvec.get_size(); j++) newvec[j] = v1[j];
   return newvec;
  }
  else {
   Vec_t<T> newvec(v1.get_size()/2);
   for (size_t j =0; j < newvec.get_size(); j++) newvec[j] = v1[j + newvec.get_size()];
   return newvec;
  }
  
}

int main() {
  const size_t N = 10;
  Vec_t<int> MyVec(N);  
  for (size_t j =0; j < N; j++) MyVec[j] = 1;
  for (size_t j=0; j < N; j++) cout << MyVec[j] << " "; cout << "\n";
  cout << "Taking half :\n";
  Vec_t<int> MyHalf(N/2);
  MyHalf = half(MyVec, 0);
  for (size_t j=0; j < N/2; j++) cout << MyHalf[j] << " "; cout << "\n";
}

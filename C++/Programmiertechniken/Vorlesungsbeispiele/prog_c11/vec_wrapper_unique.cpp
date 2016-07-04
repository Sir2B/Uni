#include <iostream>
#include <string>
#include <assert.h>
#include <memory>

using namespace std;


template<typename T>
class Vec_t {
public:
  // construtor
  Vec_t() { cout << "Default Constructor of Vec_t called.\n"; data_ = nullptr; }
  Vec_t(const size_t n) : size_(n), data_(new T [size_]) { cout << "Constructor of Vec_t called.\n"; }
  // move constructor
  Vec_t(Vec_t&& rhs) : size_(rhs.size_) {
    cout << "Move constructor of Vec_t called.\n";
    data_ = std::move(rhs.data_);
  }
  // move-assignment operator
  Vec_t& operator=(Vec_t&& rhs) {
    if (&rhs != this) {
       cout << "Move-operator= of Vec_t called\n";
       size_ = rhs.size_;
       data_ = std::move(rhs.data_);
    }
  }
  // destructor
  ~Vec_t() { cout << "Destructor of Vec_t called.\n";} 
  // operator[]
  T& operator[](size_t n) {return data_[n];}
  const T& operator[](size_t n) const { return data_[n];}
  // get functions
  size_t get_size() const { return size_;}
private:
  size_t size_;
  unique_ptr<T[]> data_;
};

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

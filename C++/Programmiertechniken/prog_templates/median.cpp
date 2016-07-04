// based on "Accelerated C++, Chapter 8"

#include <iostream>
#include <vector>
#include <algorithm>
#include <stdexcept>

template <class T>
T median(std::vector<T>& v) {
  
  typedef typename std::vector<T>::size_type vec_sz;       // NOVELTY
  
  vec_sz size = v.size();
  
  if (size == 0)
    throw std::domain_error("median of an empty vector");
  
  std::sort(v.begin(), v.end());                          // note the use of iterators
  
  vec_sz mid = size/2;
  
  return size%2 ? v[mid] : (v[mid] + v[mid+1])/2;
  
}

int main() {
  std::vector<int> premier_league;
  premier_league.push_back(10);
  premier_league.push_back(37);
  premier_league.push_back(12);
  premier_league.push_back(35);
  premier_league.push_back(25);
  std::cout << "median : " << median(premier_league) << "\n";
  
}
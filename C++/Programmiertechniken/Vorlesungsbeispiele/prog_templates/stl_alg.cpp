#include <iostream>
#include <vector>


template <class InputIterator, class X>
InputIterator myFind(InputIterator begin, InputIterator end, const X& x) {
  while (begin != end) {
    if (*begin == x) return begin;        // the input iterator should hence support == (and !=), and the unary *  (and ->)
    ++begin;                              // as well as pre- and post-increment (++)
  }
  return end;
}


template <class InputIterator, class OutputIterator>
OutputIterator myCopy(InputIterator first, InputIterator last, OutputIterator dest) {
  while (first != last) *dest++ = *first++;  // the output operator supports pre and post-increment (++), the unary * (and ->), followed by *dest=value
  return dest;                               // pay attention to the "write-once" rule for programs using OutputIterators
}

template <class ForwardIterator, class X>
void myReplace(ForwardIterator first, ForwardIterator last, const X& x, const X& y) {     // replaces every element that is equal to x by y
  while (first != last) {
    if (*first == x) *first = y;            // the ForwardIterator needs to support hence all the properties of an input and an output iterator
    ++first;                                // but there is no "write-once" rule
  }
}

template <class T>
inline void mySwap ( T& a, T& b )	    // since C++11 move semantics will be used, not copy semantics
{
  T c(a); a=b; b=c;
}

template <class ForwardIterator1, class ForwardIterator2>
inline void myIter_swap (ForwardIterator1 a, ForwardIterator2 b)
{
  mySwap (*a, *b);
}

template <class BiDirectionalIterator>
void myReverse( BiDirectionalIterator first, BiDirectionalIterator last) {
  while ((first != last) && (first != --last)) {  // the bidirectional iterator has all the functionality of the forward iterator but must also support --
    myIter_swap(first, last);
    ++first;
  }
}

template <class RandomIterator, class X>
bool myBinary_Search(RandomIterator first, RandomIterator last, const X& x) {
  while (first < last) {
    RandomIterator mid = first + (last - first)/2; // commpared to the bidirectional iterator, we additionally need arithmetic on the iterators  (eg present for std::vector but not  for the std::list )
    if (x < *mid)
      last = mid;
    else if (*mid < x)
      first = mid+1;
    else return true;
  }
  return false;
}

int main() {
  
  // I use the name myFind because the clang compiler tries to look for algorithm even though I don't specify the header file
  std::vector<int> v(10);
  int i = 0;
  for (std::vector<int>::iterator it = v.begin(); it != v.end(); ++it, ++i) *it = i*10;
  std::vector<int>::iterator it1 = v.begin();
  std::vector<int>::iterator it2 = v.end();
  std::vector<int>::iterator it = myFind(it1, it2, 0);
  if (it != it2)
    std::cout << "Element found in myvector: " << *it << '\n';
  else
    std::cout << "Element not found in myvector\n";
  it = myFind(it1, it2, 40);
  if (it != it2)
    std::cout << "Element found in myvector: " << *it << '\n';
  else
    std::cout << "Element not found in myvector\n";
  it = myFind(it1, it2, 91);
  if (it != it2)
    std::cout << "Element found in myvector: " << *it << '\n';
  else
    std::cout << "Element not found in myvector\n";
  
  std::vector<int> v2(10,0);
  --it2; --it2; --it2; ++ it1; // let us not copy all the values
  it = myCopy(it1, it2, v2.begin());
  for (std::vector<int>::iterator it = v2.begin(); it != v2.end(); ++it) std::cout << *it << " "; std::cout << "\n";
  myReplace(it1, it2, 20, 100);
  for (std::vector<int>::iterator it = v.begin(); it != v.end(); ++it) std::cout << *it << " "; std::cout << "\n";
  myReverse(v.begin(), v.end());
  for (std::vector<int>::iterator it = v.begin(); it != v.end(); ++it) std::cout << *it << " "; std::cout << "\n";
  i=0;
  for (std::vector<int>::iterator it = v.begin(); it != v.end(); ++it, ++i) *it = i*10;     // need a sorted list in increasing order
  if (myBinary_Search(v.begin(), v.end(), 0))
    std::cout << "Element found by binary search\n";
  else
    std::cout << "Element not found in binary search\n";
  
  return 0;
}

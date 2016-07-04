#include<iostream>
#include<vector>

using namespace std;

int main() {
  // declaration
  vector<int> v(10);			// vector of size 10
  vector<int> w(5, 100);		// vector of size 5 with value 100 each

  // initialization
  for (vector<int>::size_type i=0; i < 10; ++i) v[i] = i;

  // size and capacity
  cout << "size : " << v.size() << " capacity : " << v.capacity() << endl; 	// capacity can be larger; output: 10 10
  // resize
  v.resize(12);
  cout << "size : " << v.size() << " capacity : " << v.capacity() << endl; 	// capacity can be larger; output: 12 20 (could be another value than 20)
  v[10] = 10;
  v[11] = 11;
  cout << "Our vector is " << ( v.empty() ? "" : "not ") << "empty" << endl; // output: not empty

  // fast O(1) lookup and random access with the [] operator
  cout << v[4] << endl;			// also valid is v.at(4) which is equivalent to v[4]
  // output : 4
  // to access first and last element use (fast O(1) operation)
  cout << v.front() << " " << v.back() << endl;     // output : 0 11

  // since the data is stored contiguously in memory usual pointer arithmetic can be used
  cout << "# pointer traversal : ";
  for (int* ptr = &v[0]; ptr != &v[0] + 12; ++ptr) cout << *ptr << " "; cout << endl; // output: 0 1 2 ... 11
  // this is unwanted because we need a different pointer for every type and container
  // much better is to use iterators and const_iterators:
  // v.begin() points to the first element
  // v.end() is points to one past the last element
  // iterators are intended for sequential operations, and do not support random access
  // dereferencing through *
  cout << "# iterator traversal : ";
  for (vector<int>::iterator it = v.begin(); it != v.end(); ++it) cout << *it << " " ; cout << endl; // output: 0 1 2 ... 11
  // better is the following since the data do not change
  cout << "# const_iterator traversal : ";
  for (vector<int>::const_iterator it = v.begin(); it != v.end(); ++it) cout << *it << " "; cout << endl; // output: 0 1 2 ... 11
  // there is also a reverse iterator
  cout << "# const_reverse_iterator traversal : ";
  for (vector<int>::const_reverse_iterator it = v.rbegin(); it != v.rend(); ++it) cout << *it << " "; cout << endl; // output: 11 10 9 ... 0

  // modifiers: push_back, pop_back, insert, erase, assign
  v.assign(5, 1);	// 5 ints with a value of 1;
  for (vector<int>::const_iterator it = v.begin(); it != v.end(); ++it) cout << *it << " "; cout << endl; // output : 1 1 1 1 1
  vector<int> v2;
  v2.assign(v.begin()+1, v.begin()+3);	//indicate start and end positions of the range; 
  for (vector<int>::const_iterator it = v2.begin(); it != v2.end(); ++it) cout << *it << " "; cout << endl; // output : 1 1
  v.pop_back();       // remove the last element -- O(1) operation
  v.push_back(100);		// add 100 as last element -- amortized constant operation; cf the resize operation above
  vector<int>::iterator it = v.begin();
  v.insert(it, 2, 50);	// add 2 elements with value 50 before the iterator it
  // note that the iterator it is no longer valid because of the reallocation!!!
  it = v.begin();
  v.insert(it, w.begin(), w.begin() + 3);  // add 3 elements from another vector w specified by its positions
  v.erase(v.begin(), v.begin()+2); 
  for (vector<int>::const_iterator it = v.begin(); it != v.end(); ++it) cout << *it << " "; cout << endl; // output : 100 50 50 1 1 1 1 100
  return 0;
}

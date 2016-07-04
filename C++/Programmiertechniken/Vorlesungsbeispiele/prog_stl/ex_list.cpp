// example of a std::list
#include <iostream>
#include <list>
#include <vector>

int main ()
{
  std::list<int> mylist;
  std::list<int>::iterator it, it1, it2;

  // set some initial values:
  for (int i=3; i<=5; ++i) mylist.push_back(i);     // 3 4 5
  for (int i=2; i > 0; i--) mylist.push_front(i);   // 1 2 3 4 5

  it = mylist.begin();
  ++it;                                             // it points now to number 2
  it1 = it;
  
  mylist.insert (it,10);                            // 1 10 2 3 4 5

  // "it" still points to number 2                      
  // now we insert 2 copies of 20 just before it
  mylist.insert (it,2,20);                          // 1 10 20 20 2 3 4 5

  --it;                                             // it points now to the second 20

  // inserting from another sequence
  std::vector<int> myvector (2,30);                 // a vector of int with 2 elements of value 30
  it2 = mylist.insert (it,myvector.begin(),myvector.end());
                                                    // 1 10 20 30 30 20 2 3 4 5
  
  
  
  std::cout << "mylist contains:";
  for (it=mylist.begin(); it!=mylist.end(); ++it)
    std::cout << ' ' << *it;
  std::cout << '\n';

  std::cout << "mylist contains " << mylist.size() << " elements. Is the list empty? " << mylist.empty() << "\n";

  std::cout << "erasing from " << *it2 << " to " << *it1 << "\n";
  mylist.erase(it2, it1);
  std::cout << "mylist contains:";
  for (it=mylist.begin(); it!=mylist.end(); ++it)
    std::cout << ' ' << *it;
  std::cout << '\n';
  
  std::cout << "Illustration of remove :\n";
  mylist.push_front(40); mylist.push_front(40);
  for (it=mylist.begin(); it!=mylist.end(); ++it)
    std::cout << ' ' << *it;
  std::cout << '\n';
  // remove removes elements based on the value (unlike erase!)
  mylist.remove(40);
  for (it=mylist.begin(); it!=mylist.end(); ++it)
    std::cout << ' ' << *it;
  std::cout << '\n';
  
  
  return 0;
}

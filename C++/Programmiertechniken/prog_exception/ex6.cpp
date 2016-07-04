// unique_ptr::get example      -- c++11
#include <iostream>
#include <memory>

int main () {
  std::unique_ptr<int> p (new int); // rvalue
  *(p.get()) = 100;                 // get() returns the pointer
  std::cout << "p points to " << *p.get() << '\n';
  std::unique_ptr<int> p2 (new int(4)); // rvalue
  std::cout << "p2 points to " << *p2 << '\n';
  p.swap(p2);                       // we can swap the contents of unique_ptr
  std::cout << "p points to " << *p.get() << '\n';
  std::cout << "p2 points to " << *p2.get() << '\n';
  
  // we cannot copy unique_ptr, only transfer the ownership via move
  std::unique_ptr<int> p3 = std::move(p);
 
  std::cout << "p3 points to " << *p2 << '\n';
  // (p is now null-pointer unique_ptr)
  

  int* ip = nullptr;
  ip = p2.get();
  
  std::cout << "ip points to " << *ip <<  "\t p2 points to " << *p2 << '\n';
  
  ip = p3.release();          // we can also release the pointer:
  
  delete ip;    // we are now responsbile for deleting this memory, p2 is managed automatically
  

  return 0;
}

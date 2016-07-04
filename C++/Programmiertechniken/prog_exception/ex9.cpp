// unique_ptr in the context of exception handling
#include <memory>
#include <iostream>
#include <assert.h>
using namespace std;

class mylist {
public:
  int element;
  mylist *next;
};

int SomeCalculation() { return 0;} // dummy so the program compiles

// implementation using bare pointers. This is not exception safe if an error occurs in SomeCalculation
mylist* GetNewList() {
  mylist* newlist = new mylist;
  newlist->next = nullptr;
  newlist->element = SomeCalculation();
  return newlist;
}

// This version is exception safe when an exception ocurs in SomeCalculation
mylist* GetNewList_better() {
  unique_ptr<mylist> newlist(new mylist);
  newlist->next = nullptr;
  newlist->element = SomeCalculation();
  return newlist.release();               // because the return type is mylist*, not unique_ptr<mylist> we need release
}

// This version is exception safe even when the function is pathologically (but legally) called without left-hand-side
unique_ptr<mylist> GetNewList_evenbetter() {
  unique_ptr<mylist> newlist(new mylist);
  newlist->next = nullptr;
  newlist->element = SomeCalculation();
  return newlist;                             // because the return type is again unique_ptr<mylist>
}


int operation_on_even_int(const int n) {
  assert(!(n%2));
  return n/2;
}


int main() {
  mylist m;
  mylist* m2 = GetNewList();
  cout << m2->element << "\n";
  delete m2;                        // we need to clean up this memory because of new in GetNewList()
  GetNewList_better();              // memory leak because of missing left hand side
  GetNewList_evenbetter();          // OK
  cout << operation_on_even_int(4) << "\n";
  //cout << operation_on_even_int(5) << "\n";
  return 0;
}





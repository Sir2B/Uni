/* assert example */
#include <stdio.h>      /* printf */
#include <cassert>     /* assert */


void print_number(int* myInt) {
#if __cplusplus >= 201103L
  assert (myInt != nullptr);
#else
  assert (myInt!=NULL);
#endif
  printf ("%d\n",*myInt);
}

int main ()
{
  int a=10;
#if __cplusplus >= 201103L
  int *b = nullptr;
  int *c = nullptr;
#else
  int * b = NULL;
  int * c = NULL;
#endif

  b=&a;

  print_number (b);
  print_number (c);

  return 0;
}

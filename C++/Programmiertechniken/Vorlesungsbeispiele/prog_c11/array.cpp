


#include <iostream>
#include <array>

int main ()
{
  std::array<int,10> myarray;

  myarray.fill(10);

  // print content
  std::cout << "myarray contains:";
  for (unsigned int i=0; i<10; i++)
    std::cout << ' ' << myarray[i];
  std::cout << '\n';

  std::tuple_element<0,decltype(myarray)>::type myelement;  // int myelement
  myelement = std::get<2>(myarray);
  std::get<2>(myarray) = std::get<0>(myarray) + 5;
  std::get<0>(myarray) = myelement;

   for ( auto it = myarray.cbegin(); it != myarray.cend(); ++it )
    std::cout << ' ' << *it;   // cannot modify *it
  std::cout << "\n";

  //static_assert(2+2==5, "wrong sum");

  return 0;
}

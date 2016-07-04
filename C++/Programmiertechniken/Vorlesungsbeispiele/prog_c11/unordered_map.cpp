
// unordered_map::insert -- from cplusplus.com
#include <iostream>
#include <string>
#include <unordered_map>

int main ()
{
  std::unordered_map<std::string,double>
              myrecipe,
              mypantry = {{"milk",2.0},{"flour",1.5}};

  std::pair<std::string,double> myshopping ("baking powder",0.3);

  myrecipe.insert (myshopping);                        // copy insertion
  myrecipe.insert (std::make_pair<std::string,double>("eggs",6.0)); // move insertion
  myrecipe.insert (mypantry.begin(), mypantry.end());  // range insertion
  myrecipe.insert ( {{"sugar",0.8},{"salt",0.1}} );    // initializer list insertion

  std::cout << "myrecipe contains:" << std::endl;
  for (auto& x: myrecipe)
    std::cout << x.first << ": " << x.second << std::endl;

  std::cout << std::endl;

  std::unordered_map<std::string,double>::hasher hfun = myrecipe.hash_function();
  for (auto& x: myrecipe) std::cout << hfun(x.first) << std::endl;

  return 0;
}



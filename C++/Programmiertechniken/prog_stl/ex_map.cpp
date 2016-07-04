#include <iostream>
#include <map>
#include <utility>
#include <string>

int main ()
{
  // declaration of a map<key, map_value>
  std::map<char,std::string> mymap;

  // inserting values
  mymap['a']="LMU_Munich";
  mymap['b']="TU_Munich";
  // inserting values can also work (values do not need to be unique)
  mymap['c']=mymap['b'];
  
  // operator[] takes the key as argument and returns the map_value. Since C++11 also function at() exists:
  std::cout << "mymap['a'] is " << mymap['a'] << '\n';
  std::cout << "mymap['b'] is " << mymap['b'] << '\n';
  std::cout << "mymap['c'] is " << mymap['c'] << '\n';
  std::cout << "mymap['d'] is " << mymap['d'] << '\n';	// note that this inserts a new element with default string

  // size() is a function addressing the capacity
  std::cout << "mymap now contains " << mymap.size() << " elements.\n";

  // inserting elements can also be done in this way:
  mymap.insert(std::make_pair<char, std::string>('h', "Heidelberg"));
 

  // the single element version of insert returns in fact a pair where the first element
  // is the iterator to the newly inserted element and the second value is a bool which is true
  // in case of successful insertion.
  // in case the key already exists, the bool is false, and the iterator points to the existing element
  std::pair<std::map<char,std::string>::iterator,bool> ret;
  ret = mymap.insert(std::make_pair<char, std::string>('f', "FU_Berlin"));
  // show content:
  for (std::map<char,std::string>::iterator it=mymap.begin(); it!=mymap.end(); ++it)
    std::cout << it->first << " => " << it->second << '\n';
    
  ret = mymap.insert(std::make_pair<char, std::string>('f', "Stuttgart"));
  if (ret.second == false) {
    std::cout << "element " << ret.first->first << " already existed with a value of " << ret.first->second << "\n";
  }
  
  mymap['c'] = "Stuttgart"; // elements can be modified

  // we can also insert by providing a hint to the insertion position 
  // in case the optimal position is given, insertion can be done in amortized constant time
  // optimal means that the iterator is given to the element **preceding** the inserted element 

  // note: also a range insertion is possible (see the documentation)  
  mymap.insert(ret.first, std::make_pair<char, std::string>('g', "ETH Zurich"));

  // show content:
  for (std::map<char,std::string>::iterator it=mymap.begin(); it!=mymap.end(); ++it)
    std::cout << it->first << " => " << it->second << '\n';


  // empty() is a function addressing the capacity
  // erase takes an iterator as argument and erases this element
  std::cout << "starting to erase elements:\n";
  while (!mymap.empty())
  {
    std::cout << mymap.begin()->first << " => " << mymap.begin()->second << '\n';
    mymap.erase(mymap.begin());
  }


  return 0;
}

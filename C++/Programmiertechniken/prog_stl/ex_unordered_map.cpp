

// unordered_map --  requires C++11
#include <iostream>
#include <string>
#include <unordered_map>

int main ()
{
  std::unordered_map<std::string,int> bachelor_students, all_students;
  
  std::pair<std::string,int> exchange_student ("Fabricio", 2085);
  all_students.insert(exchange_student);
  bachelor_students.insert(std::make_pair<std::string,int>("Ann", 2183));
  bachelor_students.insert(std::make_pair<std::string,int>("Tom", 2184));
  all_students.insert(bachelor_students.begin(), bachelor_students.end());
  
  std::cout << "all_students contains " << std::endl;
  for (std::unordered_map<std::string,int>::iterator it = all_students.begin(); it != all_students.end(); ++it) {
    std::cout << it->first << " : " << it->second << std::endl;
  }
  
  std::cout << std::endl;
  
  std::unordered_map<std::string,int>::hasher hfun = all_students.hash_function();
  for (std::unordered_map<std::string,int>::iterator it = all_students.begin(); it != all_students.end(); ++it) {
    std::cout << hfun(it->first) << std::endl;
  }
  
  return 0;
}



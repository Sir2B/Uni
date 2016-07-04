

#include <iostream>
#include <string>
#include <regex>
 
int main()
{
  // Simple regular expression matching
  std::string fnames[] = {"foo.txt", "bar.txt", "baz.dat", "student"};
  std::regex txt_regex("[a-z]+\\.txt");
 
  for (const auto &fname : fnames) {
    std::cout << fname << ": " << std::regex_match(fname, txt_regex) << '\n';
  }   
}

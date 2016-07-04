

// The program of Chapter 1 in the book "Accelerated C++" by Andrew Koenig and Barbara E. Moo

#include <iostream>
#include <string>

using namespace std;

int main() {
  const std::string hello = "hello";					// valid string
  const std::string exclam = "!";					// valid string literal
  const std::string message = hello + " , world" + exclam;		// valid concatenation of strings and string literal
  const std::string s = "a string";
  std::cout << s << std::endl;
  { const string s = "another string";
    std::cout << s << std::endl;
  }
  std::cout << s << std::endl;						// the lines below are about the scope and curly braces
  { const std::string t = "a String";
    std::cout << t << std::endl;
    { const std::string t = "another String";
      std::cout << t << std::endl;}
    std::cout << t << std::endl;
  }
  { const std::string t = "a String";
    std::cout << t << std::endl;
    { const std::string t = "another String";
      std::cout << t << std::endl;};					// note the additional ';'
    std::cout << t << std::endl;
  }
  std::cout << "What is your name ?";
  std::string name; std::cin >> name;					// predict the output when answering Samuel Beckett
  std::cout << "Hello, " << name << std::endl << "And what is yours?";
  std::cin >> name;
  std::cout << "Hello, " << name << "; nice to meet you too!" << std::endl;
  return 0;
}

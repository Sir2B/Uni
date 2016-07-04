#include <iostream>

int main() {
  
  int speed = 57;
  
  
  // illustration of the if statement
  if (speed > 30) {
    std::cout << "You are driving too fast\n";
  }
  
  // second illustration: alternative when the condition is not met
  // for one line statements no braces are needed
  if (speed > 30)
    std::cout << "You are driving too fast\n";
  else
    std::cout << "OK\n";
  

  // third illustration: more options
  if (speed > 50) {
    std::cout << "You are driving much too fast\n";
  }
  else if (speed > 30) {
    std::cout << "You are driving a little bit too fast\n";
  }
  else {
      std::cout << "OK\n";
  }
  
  // illustration of the ternary operator
  int grade = 80;
  std::cout << (grade < 50 ? "You failed the course\n" : "You passed the course\n");
  
  
  // illustration of the switch statement -- C++11 syntax
  /*
  enum trafficlight_colors {red, yellow, green};	// scoped enum requires C++11
  trafficlight_colors light = green;
  switch (light) {
    case red:
      std::cout << "STOP!\n";
      break;          // DO NOT FORGET THE BREAK !!!! (what happens if you do?)
    case yellow:
      std::cout << "Watch out!\n";
      break;
    case green:
      std::cout << "Go!\n";
      break;
    default:
      std::cout << "New traffic rules?\n";
      abort();				// C++11 in <cstdlib>
  }
  */

  // illustration of the switch statement -- C++98 syntax
  enum {red, yellow, green};
  int light = green;
  switch (light) {
    case red:
      std::cout << "STOP!\n";
      break;          // DO NOT FORGET THE BREAK !!!! (what happens if you do?)
    case yellow:
      std::cout << "Watch out!\n";
      break;
    case green:
      std::cout << "Go!\n";
      break;
    default:
      std::cout << "New traffic rules?\n";
  }

  return 0;
}

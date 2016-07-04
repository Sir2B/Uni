#include <iostream>
#include <vector>
#include <algorithm> 		// for count_if

int main() {
  auto addition = [] (int i, int j) { return i+j;};
  std::cout << addition(2,4) << std::endl;

  std::vector<int> student_grades {20, 40, 67, 99, 13, 42, 65, 81, 82, 35, 79, 0, 4, 96, 54, 49, 35, 67, 1, 39 }; 

  auto nr_passed = std::count_if(student_grades.begin(), student_grades.end(), [] (int val) { return (val >= 50);});
  std::cout << "number of passed students is : " << nr_passed << " or " << static_cast<double>(nr_passed*100)/student_grades.size() << " percent. \n";

  auto nr_almost_passed = std::count_if(student_grades.begin(), student_grades.end(), [] (int val) { return (val >= 40 && val < 50);});
  std::cout << "number of almost-passed students is : " << nr_almost_passed << " or " << static_cast<double>(nr_almost_passed*100)/student_grades.size() << " percent. \n";

  int threshold = 45;
  auto nr_almost_passed2 = std::count_if(student_grades.begin(), student_grades.end(), [threshold] (int val) { return (val >= threshold && val < 50);});
  std::cout << "number of almost-passed students is : " << nr_almost_passed2 << " or " << static_cast<double>(nr_almost_passed*100)/student_grades.size() << " percent. \n";

  auto nr_almost_passed3 = std::count_if(student_grades.begin(), student_grades.end(), [=] (int val) { return (val >= threshold && val < 50);});
  std::cout << "number of almost-passed students is : " << nr_almost_passed3 << " or " << static_cast<double>(nr_almost_passed*100)/student_grades.size() << " percent. \n";

  int sum = 0;
  int count = 0;
  int ref_val = 0;
  // we want to know the average of all grades excluding all marks below 5 
 
  for_each(student_grades.begin(), student_grades.end(), [&, ref_val] (int val) { if (val >= ref_val) { sum += val; count++;}} ); 
  std::cout << "average grade : " << static_cast<double>(sum) / count << " for " << count << " students.\n";

}

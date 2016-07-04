


namespace Lecture {
  class Student {};
  void foo(Student& s, int i) {};
}

int main() {
  Lecture::Student s;
  foo(s, 100); // calls Lecture::foo 
}

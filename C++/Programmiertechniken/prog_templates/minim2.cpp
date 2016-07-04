
int min(int a, int b) {
  return (a < b ? a : b);
}

float min(float a, float b) {
  return (a<b ? a:b);
}

double min(double a, double b) {
  return (a<b ? a:b);
}

int main() {
  int a = 5;
  int b = 6;
  int c = min(a,b);

  float f1 = 3.1;
  float f2 = 9.5;
  float d = min(f1, f2);

  min(1,2); // OK
  min(4., 5.); // OK
  //min(5, 3.1); // does not compile, call to 'min' is ambiguous

    
    
}




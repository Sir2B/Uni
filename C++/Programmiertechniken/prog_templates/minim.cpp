

int min_int(int a, int b) {
  return (a<b ? a : b);
}

float min_float(float a, float b) {
  return (a<b ? a : b);
}


int main() {
  int a = 5;
  int b = 6;
  int c = min_int(a,b);

  float f1 = 3.1;
  float f2 = 9.5;
  float d = min_float(f1, f2);

}



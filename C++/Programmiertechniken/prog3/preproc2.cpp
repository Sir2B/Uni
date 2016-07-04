

#define DIM 2
#define pi 3.14

int main() {
  double R=1.;
  double Volume;
#if DIM == 2
  Volume = pi * R * R;
#elif DIM == 3
  Volume = 4 * pi * R* R* *R /3;
#else
#error Not a valid dimension!
#endif
  return 0;
}

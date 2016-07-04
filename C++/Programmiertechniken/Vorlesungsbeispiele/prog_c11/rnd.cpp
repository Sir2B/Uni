

// exponential_distribution -- based on the example from cplusplus.com
#include <iostream>
#include <random>

int main()
{
  const int nrolls=10000;  // number of experiments
  const int nstars=100;    // maximum number of stars to distribute
  const int nintervals=10; // number of intervals

  unsigned int seed = 10;
  std::cout << "Enter seed : ";
  std::cin >> seed;
  std::mt19937 generator(seed);		// Mersenne-Twister random number generator
  std::exponential_distribution<double> distribution(3.5);		// exponential distribution
  std::uniform_real_distribution<double> rnd(0.0, 1.0);			// uniform real distribution

  std::cout << "\na random number : " << rnd(generator) << "\n";

  int p[nintervals]={};

  for (int i=0; i<nrolls; ++i) {
    double number = distribution(generator);
    if (number < 1.0) ++p[int(nintervals*number)];
  }

  std::cout << "exponential_distribution (3.5):" << std::endl;
  std::cout << std::fixed; std::cout.precision(1);

  for (int i=0; i<nintervals; ++i) {
    std::cout << float(i)/nintervals << "-" << float(i+1)/nintervals << ": ";
    std::cout << std::string(p[i]*nstars/nrolls,'*') << std::endl;
  }

  return 0;
}

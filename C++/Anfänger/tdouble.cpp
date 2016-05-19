// 
#include <iostream>
using namespace std;

int main()
{
  double sum = 0., sum_tot = 1.0;

  for ( int i=0; i<10; i++ ) {
    sum += 0.1;
  }
  if ( sum != sum_tot ) {
    cout << " Rechner kann nicht rechnen: 1 - 1 = "
	 << sum - sum_tot << endl;
  }
}

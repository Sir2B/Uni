// print Fahrenheit->Celsius conversion table
#include <iostream>
using namespace std; // declare namespace
int main()
{
  int lower(0), upper(30000), step = 1;  // declaration and initialization
  double fahr, celsius;
  fahr = lower;

  while ( fahr <= upper ) {  // while loop
    celsius = (5.0/9.0) * (fahr-32.0);        // rechnen ...
    cout  << fahr << "  " << celsius << endl;  // ausgeben ...
    fahr += step;                             // rechnen ...
  } // end-while
}   // end-main

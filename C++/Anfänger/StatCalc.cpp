#include <iostream> // pre-prozessor command 
#include <cmath> // pre-prozessor command 
using namespace std; // declare namespace

class StatCalc {

private:
 int count;   // Number of numbers that have been entered.
 double sum;  // The sum of all the items that have been entered.
 double squareSum;  // The sum of the squares of all the items.
 double max, min; 

public:
  StatCalc() : count(0), sum(0.), squareSum(0.), max(0.), min(0.) {} // default constructor

  void enter(double num) {
    // Add the number to the dataset.
    if (count == 0)
	min=max=num;
    count++;
    sum += num;
    squareSum += num*num;
    if (num < min)   
	min = num;
    if (num > max)
	max = num;
  }

  int getCount() {   
    // Return number of items that have been entered.
    return count;
  }
  
  double getSum() {
    // Return the sum of all the items that have been entered.
    return sum;
  }

  double getMean() {
    // Return average of all the items that have been entered.
    // Value is Double.NaN if count == 0.
    return sum / count;  
  }
  
  double getStandardDeviation() {  
    // Return standard deviation of all the items that have been entered.
    // Value will be Double.NaN if count == 0.
    double mean = getMean();
    return sqrt( squareSum/count - mean*mean );
  }

  double getMin() {  
    return min;
  }

  double getMax() {  
    return max;
  }

};  // end of class StatCalc

#include <cstdlib>
#include <time.h>

int main() 
{

  StatCalc s1;  // lege StatCalc Objekt an

  srandom(time(0)); // setup random generator

  for ( int i=0; i<1000; i++ ) {
    double xrnd = random()*2./RAND_MAX - 1.; // Zufallszahlen zwischen [-1,1]
    s1.enter(xrnd);
  }

  cout << s1.getCount() << "   "
       << s1.getMean()  << "   "
       << s1.getStandardDeviation()  << "   "
       << s1.getMax()  << "   "
       << s1.getMin()  << "   "
       << endl;




  return(0);
}


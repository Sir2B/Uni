#include <iostream> // pre-prozessor command
#include <cmath> // pre-prozessor command
#include "StatCalc.h"
using namespace std; // declare namespace



StatCalc::StatCalc() : count(0), sum(0.), squareSum(0.) {} // default constructor

  void StatCalc::enter(double num) {// Add the number to the dataset.

	if (first)
	  {
		max=num;
		min=num;
		first=false;
	  }

	count++;
    sum += num;
    squareSum += num*num;
    if(num > max)
    {
    	max=num;
    }
    if(num < min)
       {
       	min=num;
       }
    }

  void StatCalc::initfirst()
  {
	  first=true;
  }


  int StatCalc::getCount() {
    // Return number of items that have been entered.
    return count;
  }

  double StatCalc::getSum() {
    // Return the sum of all the items that have been entered.
    return sum;
  }

  double StatCalc::getMean() {
    // Return average of all the items that have been entered.
    // Value is Double.NaN if count == 0.
    return sum / count;
  }

  double StatCalc::getStandardDeviation() {
    // Return standard deviation of all the items that have been entered.
    // Value will be Double.NaN if count == 0.
    double mean = getMean();
    return sqrt( squareSum/count - mean*mean );
  }

  double StatCalc::getMax()
  {
	  return max;
  }

  double StatCalc::getMin()
  {
	  return min;
  }


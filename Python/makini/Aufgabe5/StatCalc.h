
class StatCalc
{
private:
 int count;   // Number of numbers that have been entered.
 double sum;  // The sum of all the items that have been entered.
 double squareSum;  // The sum of the squares of all the items.
 //double numalt=0;
 double max;
 double min;
 bool first;

public:
StatCalc();
void enter(double num);
int getCount();
void initfirst();
double getSum();
double getMean();
double getStandardDeviation();
double getMax();
double getMin();
};

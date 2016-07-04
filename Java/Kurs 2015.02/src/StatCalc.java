
/* 
   An object of class StatCalc can be used to compute several simple statistics
   for a set of numbers.  Numbers are entered into the dataset using
   the enter(double) method.  Methods are provided to return the following
   statistics for the set of numbers that have been entered: The number
   of items, the sum of the items, the average, and the standard deviation.
*/



public class StatCalc {
    private int count;   // Number of numbers that have been entered.
    private double sum;  // The sum of all the items that have been entered.
    private double squareSum;  // The sum of the squares of all the items.
    private double min;
    private double max;

    public void enter(double num) {

        // Add the number to the dataset.
        if (count == 0){
            min = num;
            max = num;
        }
        count++;
        sum += num;
        squareSum += num*num;

        if (num < min) min = num;
        if (num > max) max = num;
    }

    public int getCount() {
          // Return number of items that have been entered.
       return count;
    }

    public double getSum() {
          // Return the sum of all the items that have been entered.
       return sum;
    }

    public double getMean() {
          // Return average of all the items that have been entered.
          // Value is Double.NaN if count == 0.
       return sum / count;
    }
    public double getMin() {
        return min;
    }
    public double getMax() {
        return max;
    }

    public double getStandardDeviation() {
         // Return standard deviation of all the items that have been entered.
         // Value will be Double.NaN if count == 0.
       double mean = getMean();
       return Math.sqrt( squareSum/count - mean*mean );
    }

}  // end of class StatCalc

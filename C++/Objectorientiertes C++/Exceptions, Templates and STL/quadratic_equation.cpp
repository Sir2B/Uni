#include <vector>  // vector headers
#include <iostream>
#include <cmath>
#include <stdexcept>

using namespace std;

double root(double A, double B, double C)
{
    // Returns the larger of the two roots of
    // the quadratic equation A*x*x + B*x + C = 0.
    // (Throws an exception if A == 0 or B*B-4*A*C < 0.)
    if (A == 0)
    {
        throw ("A can't be zero.");
    }
    else
    {
        double disc = B*B - 4*A*C;
        if (disc < 0)
            throw ("Discriminant < zero.");
        return  (-B + sqrt(disc)) / (2*A);
    }
}
void quadratic_equation()
{
    cout << "solves the quadratic equation A*x*x + B*x + C = 0." << endl;
    double A, B, C;
    double x;
    cout << "A = "; cin >> A;
    cout << "B = "; cin >> B;
    cout << "C = "; cin >> C;

    try
    {
        x = root( A, B, C);
    }
    catch (char const *message )
    {
        cout << "root failed:  " << message << endl;  // print error
    }
    cout << "For the equation " << A << "*x^2 +" << B << "*x + " << C << " = 0" << endl;
    cout << " x = " << x << endl;

}

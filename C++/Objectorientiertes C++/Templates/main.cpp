#include <iostream>

using namespace std;

template <class T>
T Max(const T & x, const T & y)
{
    return (x > y ? x:y);
}

template <class T>
T Min(const T & x, const T & y)
{
    return (x < y ? x:y);
}

template <class T>
T Quadrat(const T & x)
{
    return x*x;
}

template <class T>
T Pow(const T & x, const int & n)
{
    if (n < 0)
    {
        throw("Pow: Error x^n just implemented for n>=0");
    }
    T sum = 1;
    for (int i = 0; i < n ; i++)
    {
        sum *= x;
    }
    return sum;
}

int main()
{
    double a=3.2,b=4.2;
    int c=4,d=7;
    string s="Hallo",t="Hello";
    cout << "Max(a,b) :" << Max(a,b) <<  endl;
    cout << "Min(c,d) :" << Min(c,d) <<  endl;
    cout << "Max(s,t) :" << Max(s,t) <<  endl;
    cout << "5^9 = " << Pow(5,9) << endl;
    cout << "4.1^4 = " << Pow (4.1, 4) << endl;

    cout << "4.1^4.1 = " << Pow (4.1, 4.1) << endl;
    try
    {
        cout << "4.1^-4.1 = " << Pow (4.1, -4.1) << endl;
    }
    catch (char const *message )
    {
        cout << "Error in main: " << message <<endl;
    }
}

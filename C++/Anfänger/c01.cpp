#include <iostream>
#include <cmath>

using namespace std;

template <class X, class Y> X exp(const X &x, const Y &y)
{
	return(pow(x,y));
}
template <class T> T quadrat(const T &r)
{
	return(r*r);
}
template <class X, class Y> X Min(const X &x, const Y &y)
{
	return((x<y ? x:y));
}
template <class X> X Abs(const X &x)
{
	return((x>-x ? x:-x));
}

int main()
{
	int a=1, b=3;
	double c=.5, d=1.5, e=-.3;
	cout << quadrat(c) << endl;
	cout << pow(b,c) << endl;
	cout << exp(b,c) << endl;
	cout << Min(e,b) << endl;
	cout << Abs(a) << endl;
}

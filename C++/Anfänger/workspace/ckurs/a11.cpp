#include <iostream>
using namespace std;

void swap (int *x, int *y)
{
	int tmp;
	tmp=*x;
	*x=*y;
	*y=tmp;
}

/*
void swap2 (int & x, int & y)
{
int tmp = x;
x=y;
y=tmp;
}

//ausruf mit swap2(a,b);
*/


int main()
{
	int a, b;
	cin >> a;
	cin >> b;
	swap(&a,&b);
	cout << a<< endl<< b << endl;
	return(0);

}

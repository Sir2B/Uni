#include <iostream>
using namespace std;
int main()
{
	int error = 0;
	for (int n=1; n<= 200; n++)
		{
			int sum1 = 0;
			int sum2 = 0;

			for (int i=1; i<=n; i++)
				{
					sum1 = sum1 + i*i*i;
				}
			for (int i=1; i<=n; i++)
				{
					sum2 = sum2 + i;
				}
			cout << sum1 << " " << sum2*sum2 << endl;	

			if (sum1=! sum2*sum2)
				{
				error+=1;
				}
		}
	cout << "\n" << error <<endl;
	
}

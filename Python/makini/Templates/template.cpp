#include <iostream>

using namespace std;


int main ()
{
	int ar[7][4][2][13];
	int ar2[7][4][2][13];
	&ar2[0][0][0][0]= &ar[7][4][2][13]+1;
   cout << &ar[0][0][0][0] << endl;
   cout << &ar[7][4][2][13] << endl;
   cout << dec << (&ar[7][4][2][13]-&ar[0][0][0][0]) << endl;
}

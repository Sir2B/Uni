#include "BigInt.h"
#include <iostream>
#include <Windows.h>
using namespace std;

int main()
{
	//BigInt a = "234578997624315";
	BigInt a = "2555555555555";
	//BigInt b = "23987489367823";
	BigInt b = "211111";
	BigInt c = a + b;
	BigInt d = a * b;
	cout << "a = "<< a << endl;
	cout << b.Mal10()+a << endl;
	cout << "b = " << b << endl;
	cout << "a + b = " << c << endl;
	cout << "a - b = " << a-b << endl;
	cout << "a * b = " << d << endl;
	

	system("PAUSE");
	return 0;
}

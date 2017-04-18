/*
 * a11.cpp
 *
 *  Created on: Mar 11, 2014
 *      Author: Tobias.Dummbert
 */

#include <iostream>

using namespace std;

void swap (int *p1, int *p2)
{
	 int tmp;
	 tmp = *p1;
	 *p1=*p2;
	 *p2=tmp;

}

int main2()
{

int a = 7;
int b = 5;


cout << a  << " " << b << endl;
swap (&a,&b);

cout << a  << " " << b << endl;

}

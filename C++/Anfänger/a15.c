/*
 * a15.cpp
 *
 *  Created on: Mar 11, 2014
 *      Author: Tobias.Obermayer
 */

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	//numbers.dat einlesen und in array speichern
	ifstream werte("empty.dat");
	int laenge=100;
	char x[laenge];
	char y;
	int n=0;

	/*
	int xmin=0, xmax=0;
	while (werte >> y && n <laenge)
	{
		if (n==0) xmax=xmin=xmin;

		if (x<xmin)...
		if (x>xmax)...

		x[n]=y;
		n++;
	}
	*/
	while (werte >> y && n <laenge)
	{
		x[n]=y;
		cout << (int) x[n] << endl;
		n++;
	}
	
	/*
	for (int i = 0; i<laenge; i++)
	{
		werte >> x[i];
	}
	*/

	//kleinster Wert
	float klein=x[0];
	for (int i = 1; i<laenge; i++)
	{
		if (klein > x[i])
			{klein=x[i];}
	}
	cout << "Kleinster Wert: " << klein << endl;

	//größter Wert
	float gros=x[0];
	for (int i = 1; i<laenge; i++)
	{
		if (gros < x[i])
			{gros=x[i];}
	}
	cout << "Großter Wert: " << gros << endl;

	
	//Ausgabe
	/*
	for (int i =0; i <laenge; i++)
	{
		cout << x[i] << endl;
	} 
	*/

return(0);
}


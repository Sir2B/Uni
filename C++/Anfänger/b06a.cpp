#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	ifstream kant("kant.txt");
	//string zeile[100000];
	string zeiler;
	int zeilenzaehler=-1;
	int Vernunftzaehler=0;

	while (!kant.eof())
	{
		zeilenzaehler++;
		getline(kant, zeiler);
		/*for (int i = 0; i <= zeiler.size(); i++)
		{
			if (zeiler[i]>='A' && zeiler[i] <='Z')
				zeiler[i]+=32;
		}
		*/ //Groß zu Kleinbuchstaben

		for (int i = 0; i <= zeiler.size(); i++)
		{
			if (zeiler[i]=='V' && zeiler[i+1] =='e' && zeiler[i+2] =='r' && zeiler[i+3] =='n' 
			&& zeiler[i+4] =='u' && zeiler[i+5] =='n' && zeiler[i+6] =='f' && zeiler[i+7] =='t' && (zeiler[i+8] > 'z' || zeiler[i+8]<'A' || (zeiler[i+8]<'a' && zeiler[i+8]>'Z')))
				Vernunftzaehler++;
		}

		//cout << zeiler << endl;
		
	}
	cout << zeilenzaehler <<endl;
	cout << Vernunftzaehler <<endl;
}

// BigInt.cpp   implementation file for class BigInt
#include <iostream>
#include <cstring>
#include "BigInt.h"

using namespace std;

#define MAX(a,b) ( (a) > (b) ? ( a ) : ( b ) )
BigInt::BigInt() { ndig = 0; }
BigInt::BigInt(const char * str)
{
	int len = strlen(str);
	ndig = 0;
	while (len >= 0) {
		int c = str[len--];
		if (c >= '0' && c <= '9') {
			number[ndig++] = c - '0';
		}
	}
}
BigInt BigInt::operator + (const BigInt & x) const
{
	BigInt t;
	t.ndig = MAX(this->ndig, x.ndig) + 1;
	int sum = 0, carry = 0;
	for (int i = 0; i < t.ndig; i++) {
		carry = sum / 10;
		sum = carry;
		if (i < this->ndig)	sum += this->number[i];

		if (i < x.ndig)  sum += x.number[i];

		t.number[i] = sum % 10;
	}
	if (carry == 0)  t.ndig--;
	return t;
}

BigInt BigInt::operator - (const BigInt & x) const
{
	BigInt t;

	t.ndig = this->ndig;
	t.number[0] = 0;
	for (int i = 0; i < t.ndig; i++)
	{
		if (i < x.ndig)
		{
			
			if (this->number[i]>x.number[i]) t.number[i] = this->number[i] - x.number[i];
			else
			{
				t.number[i + 1] = 0;
				t.number[i] += this->number[i] + 10 - x.number[i];
				t.number[i + 1] = -1;
			}
		}
		else t.number[i] = this->number[i];
	}


	//int sum = 0, carry = 0;
	//for (int i = 0; i < t.ndig; i++) {
	//	carry = sum / 10;
	//	sum = carry;
	//	if (i < this->ndig)	sum += this->number[i];

	//	if (i < x.ndig)  sum += x.number[i];

	//	t.number[i] = sum % 10;
	//}
	//if (carry == 0)  t.ndig--;
	return t;
}

BigInt BigInt::operator * (const BigInt & x) const
{
	BigInt Ergebnis;
	
	Ergebnis.ndig = ndig + x.ndig;

	for (BigInt tmp2 = x; tmp2 == "0"; tmp2 = tmp2 - "1")
	{
		Ergebnis = Ergebnis + this;
	}
}

/*BigInt BigInt::operator * (const BigInt & x) const
{
	BigInt tmp2, tmp3;
	BigInt ergebnis;
	ergebnis.ndig = tmp2.ndig = this->ndig + x.ndig;
	int sum = 0, carry = 0;
	int tmp0, tmp1;
	int zahl1 = this->number[0];
	ergebnis.number[0] = 0;
	tmp2.number[0] = 0;
	for (int n = (this->ndig-1); n >= 0; n--)
	{
		
		zahl1 = this->number[n];

		for (int i = 0; i < x.ndig; i++)
		{
			tmp2.number[i + 1] = 0;
			tmp1 = tmp2.number[i];
			tmp1 += zahl1*x.number[i];
			
			if (tmp1 >= 10)
			{
				int gemerkt = tmp1 - (tmp1 % 10);
				tmp2.number[i] = tmp1 - gemerkt;
				tmp2.number[i + 1] = (gemerkt / 10);
			}
			else
			{
				tmp2.number[i] = tmp1;
			}

		}
		if (tmp2.number[x.ndig] == 0)	tmp2.ndig--;

		if (n == (this->ndig-1))
		{
			tmp3 = tmp2;
		}
		else
		{
			tmp3 = tmp3.Mal10() + tmp2;
		}
		
	}
	ergebnis = tmp3;
	//if (ergebnis.number[ergebnis.ndig] == 0)	ergebnis.ndig--;
	return ergebnis;
}*/

bool BigInt::operator == (const BigInt & x) const
{
	bool ergebnis=true;
	for (int i = 0; i < ndig; i++)
	{
		if (x.number[i] != number[i])
		{
			ergebnis = false;
			break;
		}

	}

	return ergebnis;
}


std::ostream & operator << (std::ostream &s, const BigInt &x)
{
	for (int i = x.ndig; i >0; i--)
	{
		s << x.number[i -1];
	}
	return s;
	//print();
}

BigInt BigInt::Mal10()
{
	BigInt t;
	t.ndig = this->ndig + 1;
	for (int i = t.ndig; i > 0; i--)
	{
		t.number[i] = this->number[i - 1];
	}
	t.number[0] = 0;

	return t;
}

void BigInt::print() const
{
	for (int i = ndig; i > 0; i--) {
		cout << number[i - 1];
	}
	cout << endl;
}


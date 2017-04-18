 // bigint.h   implementation file for class bigint
 #include <iostream>
 #include <cstring>
 #include "bigint.h"

 using namespace std;

 #define MAX(a,b) ( (a) > (b) ? ( a ) : ( b ) )
 bigint::bigint() {  ndig = 0; }
 bigint::bigint(const char * str)
 {
   int len = strlen(str);
   ndig = 0;
   while ( len >= 0 ) {
     int c = str[len--];
     if ( c >= '0' && c <= '9' ) {
       number[ndig++] = c - '0';
     }
   }
 }

 bigint bigint::operator + (const bigint & x ) const
 {
   bigint t;
   t.ndig = MAX( this->ndig, x.ndig) + 1;
   int sum = 0, carry = 0;
   for ( int i = 0; i < t.ndig; i++ ) {
     carry = sum/10;
     sum = carry;
     if ( i < this->ndig )
        sum += this->number[i];

     if ( i < x.ndig )  sum += x.number[i];

     t.number[i] = sum % 10;
   }
   if ( carry == 0 )  t.ndig --;
   return t;
 }
 void bigint::print() const
   {
     for ( int i = ndig; i > 0; i-- ) {
       cout << number[i-1];
       }
     cout << endl;
 }

 std::ostream &operator << ( std::ostream &s, const bigint &x)
 {
	 ndig=0;
	 while ( len >= 0 ) {
	      int c = str[len--];
	      if ( c >= '0' && c <= '9' ) {
	        number[ndig++] = c - '0';
	        cout << "haha lustig";

 }

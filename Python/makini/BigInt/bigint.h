
#include <iostream>
 // bigint.hxx  header file for class bigint;
 class bigint
 {
 private:
   int number[100];           // reserve string with 100 chars
   int ndig;                  // count digits
 public:
   bigint();                  // default constructor
   bigint(const char * s);          // standard constructor
   //   bigint(const bigint & x ); // copy constructor, spaeter
   //   ~ bigint();                 // destructor, spaeter
   void print() const;
   bigint  operator + (const bigint & x ) const;
   bigint  operator - (const bigint & x ) const;
   friend std::ostream &operator << ( std::ostream &s, const bigint &x);
 };
 std::ostream &operator << ( std::ostream &s, const bigint &x);

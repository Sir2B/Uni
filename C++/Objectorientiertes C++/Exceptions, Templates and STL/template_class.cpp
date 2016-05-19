#include <iostream>
template < class T1, class T2>
class pair_
{
public:
    T1 first;
    T2 second;
    pair_(const T1& x,const T2&y): first(x),second(y) {}
};
void template_class()
{
    pair_ <double,int> p1(3.14,7);
    pair <int,double> p2(9,4.4);
    cout << "p1: " << p1.first << " " << p1.second << endl;
    cout << "p2: " << p2.first << " " << p2.second << endl;
};

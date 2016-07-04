

#include <iostream>

using namespace std;

int main()
{
    auto func = [] () { cout << "Hello, world!\n"; };           // do not forget the last ;
    func(); // now call the function
}

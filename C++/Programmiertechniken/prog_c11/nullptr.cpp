

// based on cppreference.com
#include <cstddef>
#include <iostream>
#include <memory>
 
template<class F, class A>
void Fwd(F f, A a)				// template forward function
{
    f(a);
}
 
void g(int* i)
{
    std::cout << "Function g called\n";
}

void f(std::nullptr_t nullp)
{
   std::cout << "null pointer overload\n";
} 


int main()
{
    g(NULL);           	// Fine
    g(0);              	// Fine
 
    Fwd(g, nullptr);   	// Fine
//  Fwd(g, NULL);  	// ERROR: No function f(int)
    f(nullptr);		// Fine
    // the purpose of the following two lines is to show that a nullptr can be deleted without error
    // in practice this means there is no reason the check whether a pointer is a nullptr before delete
    int* iptr = nullptr;
    delete iptr;	// harmless
    iptr = nullptr; delete[] iptr;	// harmless
    return 0;
}

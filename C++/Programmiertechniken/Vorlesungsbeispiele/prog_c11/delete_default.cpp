#include <iostream>



struct noncopyable
{
  noncopyable() =default;	// needed because explicit writing of the (albeit deleted) copy constructor
                            // prevents the default constructor; this can be fixed by defaulting it with
                            // no performance penalty
  noncopyable(const noncopyable&) =delete;	// deleted copy construction; calling it results in compile-time error
  noncopyable& operator=(const noncopyable&) =delete;	// deleted assignment
};


template<typename T>
void fun_int_only(T) = delete;

void fun_int_only(int) { return;}		// repeat for const int, int&,... if needed

int main() {
    return 0;
    //fun_int_only(4.0);               // compile time error
    fun_int_only(4);                  // OK
}



template<typename T>
void f(ParamType param);

f(expr);

template<typename T>
void f(const T& param);
int x = 27;  f(x);      // x is an int; call f with an int; T is int, ParamType is const int&



const int cx = x;       // cx is a const int
const int& rx = x;      // rx is a reference to x as a const int

template<typename T>
void f(T& param);       // param is a reference

f(x);                   // T is int,       param's type is int&
f(cx);                  // T is const int, param's type is const int&
f(rx);                  // T is const int, param's type is const int&
                        
                        
template<typename T>
void f(const T& param);  // param is now a ref-to-const

f(x);                    // T is int, param's type is const int&
f(cx);                   // T is int, param's type is const int&
f(rx);                   // T is int, param's type is const int&


template<typename T>
void f(T param);         // param is now passed by value

f(x);                    // T's and param's types are both int
f(cx);                   // T's and param's types are again both int
f(rx);                   // T's and param's types are still both int




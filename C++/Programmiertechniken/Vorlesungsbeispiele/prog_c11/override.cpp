

// from cppreference.com
struct A
{
    virtual void foo();
    void bar();
};
 
struct B : A
{
    //void foo() const override; // Error: B::foo does not override A::foo
                               // (signature mismatch)
    void foo() override; // OK: B::foo overrides A::foo
    //void bar() override; // Error: A::bar is not virtual
};


struct C
{
    virtual void foo() final; // C::foo is final
    //void bar() final; // Error: non-virtual function cannot be final
};

struct D final : C // struct D is final
{
    //void foo(); // Error: foo cannot be overridden as it's final in C
};

/*
struct E : D // Error: D is final
{
};
*/


int main() {
}

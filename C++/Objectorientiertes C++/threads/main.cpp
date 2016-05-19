#include <iostream>

using namespace std;

void func(int x)
{
    cout << "Innerhalb des threads" << x << endl;
}

int square(int x)
{
    return x * x;
}


#include <future>
#include <chrono>
void tasks()
{
    auto a = async(&square, 10);
    int v = a.get();

    cout << "The thread returned " << v << endl;
}

#include <thread>
void threads()
    thread th(func, 100);
dr{
    th.join();
    cout << "Ausserhalb des threads" << endl;
}

int main()
{
    //threads();
    tasks();
    return 0;
}

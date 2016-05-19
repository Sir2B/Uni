#include <vector>
#include <iostream>
using namespace std;

int vec(){
    vector<int> v;
    for (int i = 10; i < 100; i+=5){
        v.push_back(i);
        cout << i << endl;
    }

    vector<int>::iterator vp = v.begin();
    cout << *(vp+5) << endl;
}

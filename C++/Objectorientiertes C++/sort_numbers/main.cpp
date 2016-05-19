#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <stdlib.h>
using namespace std;

int main()
{
    string line;
    ifstream myfile("numbers.dat");
    vector<double> numberVector;
    //if (myfile.is_open())
    {
        while ( getline (myfile,line) )
        {
            //cout << line << '\n';
            numberVector.push_back(atof(line.c_str()));
        }
        myfile.close();
        //cout << "finished" << endl;
    }
    sort(numberVector.begin(), numberVector.end());
    cout << * numberVector.end() << endl;
    cout << numberVector.size() << endl;
    for (int i = 0; i< numberVector.size(); i++){
        cout << numberVector[i] << endl;
    }

}

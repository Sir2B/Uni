#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>

using namespace std;

int main()
{
	map < int , string > pers;

	ifstream file ("vorwahl.txt");
	double x;
	string str;
	str = "1";
	unsigned int i;
	vector <int> nums;

	//double xmin(0),xmax=0;
	//int n=0;
	i=100;
	while (!file.eof())
	{

		file >> x;
		nums.push_back(x);
		cout << nums.back();

		file >> str;
		pers[x] = str;

		cout << pers[nums[i]] << endl;
	}
	//file.close();

	for (i=0;i<nums.size();i++)
	{
		cout << pers[nums[i]] << endl;
	}
}

#include <iostream>
#include <numeric>
#include <cmath>
#include <vector>

double var(double a1, double a2)
{
  return a1+a2*a2;
}

void print_vector(const std::vector<double>& v)
{
  std::cout << "[";
  for(size_t i = 0; i < v.size()-1; i++)
    std::cout << v[i] << " , ";
  std::cout << v[v.size()-1] << " ]" << std::endl;
}

int main ()
{
  
  std::vector<int> v1(10);
  for(int i=0; i<10; i++)
    v1[i] = i;
  std::vector<int> v2(v1);
  std::vector<int> v3 = {0,1,2,3,4,5,6,7,8,9};
  
  
  std::vector<double> temp_list;
  double temp_val;
  while (std::cin >> temp_val)
    temp_list.push_back(temp_val);
  
  std::cout << "Es gibt " << temp_list.size() << " Datenpunkte" << std::endl;
  print_vector(temp_list);
  
  double mean = 0;
  mean = std::accumulate(temp_list.begin(), temp_list.end(), mean);
  double mean2 = 0;
  mean2 = std::accumulate(temp_list.begin(), temp_list.end(), mean2, var);

  std::cout << "Die Durchschnittstemperatur in MUC betraegt " << mean/static_cast<double>(temp_list.size()) << " und schwankt mit einer Standardabweichung von " << sqrt(mean2/static_cast<double>(temp_list.size())-pow(mean/static_cast<double>(temp_list.size()),2.)) << " um die Durchschnittstemperatur" << std::endl;
  
  std::vector<int> v;
  for(int i=0; i<100; i++)
    v.push_back(i);
  std::cout << "The size of the vector " << v.size() << std::endl;
  std::cout << "The capacity of the vector " << v.capacity() << std::endl;
  std::cout << "Number of possible elements you can add without reallocating the vector " << v.capacity() - v.size() << std::endl;
  
  size_t max_size = 1e7;
  std::vector<int> w;
  std::cout << "The size of the vector " << w.size() << std::endl;
  std::cout << "The capacity of the vector " << w.capacity() << std::endl;
  w.reserve(max_size);
  std::cout << "The size of the vector " << w.size() << std::endl;
  std::cout << "The capacity of the vector " << w.capacity() << std::endl;
  
  std::vector <double> x(10,1.);
  std::vector <double> y(10,2.);
  std::cout << "x = ";
  print_vector(x);
  std::cout << "y = ";
  print_vector(y);
  
  std::swap(x,y);
  
  std::cout << "x = ";
  print_vector(x);
  std::cout << "y = ";
  print_vector(y);
  
  return 0;
}

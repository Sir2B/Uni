#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>

void print_vector(const std::vector<double>& v)
{
  std::cout << "[";
  for(size_t i = 0; i < v.size()-1; i++)
    std::cout << v[i] << " , ";
  std::cout << v[v.size()-1] << " ]" << std::endl;
}

void print_vector(const std::vector<int>& v)
{
  std::cout << "[";
  for(size_t i = 0; i < v.size()-1; i++)
    std::cout << v[i] << " , ";
  std::cout << v[v.size()-1] << " ]" << std::endl;
}

bool compare_argsort(std::pair<int,double> i1, std::pair<int,double> i2)
{
  return i1.second < i2.second;
}

int find_value_in_list(std::vector<double> list, double val)
{
  std::pair<std::vector<double>::iterator,std::vector<double>::iterator> it = std::equal_range (list.begin(), list.end(), val);
  if(it.first-it.second == 0)
    return -1;
  else
    return it.first - list.begin();
}

int main (int argc, char *argv[])
{
  if( argc < 2)
  {
    std::cout << "Die Eingabe der zu suchenden Temperaturen wurde vergessen" << std::endl;
    exit(1);
  }
  std::vector<double> val;
  for(int i=1; i<argc; i++)
    val.push_back(atof(argv[i]));
  
  std::vector<double> temp_list;
  for(;;)
  {
    double temp_val;
    std::cin >> temp_val;
    if(std::cin.fail())
      break;
    temp_list.push_back(temp_val);
  }

  char file_end;
  std::cin >> file_end;
  std::cin.clear();
  
  std::cout << "Es gibt " << temp_list.size() << " Datenpunkte" << std::endl;
  print_vector(temp_list);
  
  std::vector<std::pair<int,double> > argsort_temp_list;
  for(size_t i=0; i<temp_list.size(); i++)
    argsort_temp_list.push_back(std::make_pair(static_cast<int>(i),temp_list[i]));
  
  std::sort(argsort_temp_list.begin(),argsort_temp_list.end(),compare_argsort);
  
  std::vector<double> sorted_temp_list(temp_list.size());
  std::vector<int> sorted_indices(temp_list.size());
  for(size_t i=0; i<temp_list.size(); i++)
  {
    sorted_temp_list[i] = argsort_temp_list[i].second;
    sorted_indices[i] = argsort_temp_list[i].first;
  }
  std::cout << "Die sortierten Temperaturen sind" << std::endl;
  print_vector(sorted_temp_list);
  
  std::cout << "Die Indizes, welche die Temperaturen sortieren" << std::endl;
  print_vector(sorted_indices);
  
  for(size_t i; i<val.size(); i++)
  {
    int idx = find_value_in_list(sorted_temp_list,val[i]);
    if(idx != -1)
      std::cout << "Die Temperatur " << val[i] << " wurde am " << sorted_indices[idx]+1 << ". Tag des Jahres 2015 in MUC gemessen" << std::endl;
    else
      std::cout << "Die Temperatur " << val[i] << " wurde im Jahr 2015 an keinem Tag gemessen" << std::endl;
  }
  
  std::cout << "Die Hoechsttemperatur in Muenchen im Jahr 2015 ist " << sorted_temp_list[temp_list.size()-1] << " und wurde am " << sorted_indices[sorted_indices.size()-1] << ". Tag gemessen" << std::endl;
  std::cout << "Die Tiefsttemperatur in Muenchen im Jahr 2015 ist " << sorted_temp_list[0] << " und wurde am " << sorted_indices[0] << ". Tag gemessen" << std::endl;
  
  temp_list.erase(temp_list.begin()+sorted_indices[sorted_indices.size()-1]);
  temp_list.erase(temp_list.begin()+sorted_indices[0]);
  
  double mean = 0;
  std::cout << "Die Durchschnittstemperatur ohne die beiden Extremwerte ist " << std::accumulate(temp_list.begin(),temp_list.end(),mean)/temp_list.size() << std::endl;
  std::cout << "Das ist korrekt? " << std::accumulate(sorted_temp_list.begin()+1, sorted_temp_list.end()-1, mean)/temp_list.size() << std::endl;
  
  
  return 0;
}

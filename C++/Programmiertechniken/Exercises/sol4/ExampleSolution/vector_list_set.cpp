#include <iostream>
#include <fstream>
#include <chrono>
#include <cmath>
#include <vector>
#include <list>

void comp_random_remove_insert(int n_points, const int* number_elements, int number_inserts)
{
  double run_time_vector[n_points];
  double run_time_list[n_points];
  
  for(int i=0; i<n_points; i++)
  {
    std::vector<int> vector_container(number_elements[i]);
    std::list<int> list_container;
  
    for(int j=0; j<number_elements[i]; j++)
    {
      vector_container[j] = 2*j+1;
      list_container.push_back(2*j+1);
    }
    
    std::chrono::high_resolution_clock::time_point t1 = std::chrono::high_resolution_clock::now();
    for(int j=0; j<number_inserts; j++)
    {
      int insert = number_elements[i]/2;
      auto iter = vector_container.begin();
      std::advance(iter,insert);
      vector_container.insert(iter,2*insert);
      
      iter = vector_container.begin();
      std::advance(iter,insert);
      vector_container.erase(iter);
    }
    std::chrono::high_resolution_clock::time_point t2 = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> time_span = std::chrono::duration_cast<std::chrono::duration<double>>(t2 - t1);
    run_time_vector[i] = time_span.count();
    
    
    int insert = number_elements[i]/2;
    auto iter = list_container.begin();
    std::advance(iter,insert);
    t1 = std::chrono::high_resolution_clock::now();
    for(int j=0; j<number_inserts; j++)
    {
      list_container.insert(iter,2*insert);
      
      --iter;
      iter = list_container.erase(iter);
    }
    t2 = std::chrono::high_resolution_clock::now();
    time_span = std::chrono::duration_cast<std::chrono::duration<double>>(t2 - t1);
    run_time_list[i] = time_span.count();
    
  }
  std::ofstream out("results/remove_insert");
  for(int i=0; i<n_points; i++)
    out << number_elements[i] << " " << run_time_vector[i] << " " << run_time_list[i]  << std::endl;
}

void comp_random_access(int n_points, const int* number_elements, int number_inserts)
{
  double run_time_vector[n_points];
  double run_time_list[n_points];

  srand( 10 );

  for(int i=0; i<n_points; i++)
  {
    std::vector<int> vector_container(number_elements[i]);
    std::list<int> list_container;
    
    for(int j=0; j<number_elements[i]; j++)
    {
      vector_container[j] = 2*j+1;
      list_container.push_back(2*j+1);
    }
    
    std::chrono::high_resolution_clock::time_point t1 = std::chrono::high_resolution_clock::now();
    for(int j=0; j<number_inserts; j++)
    {
      int insert = static_cast<int>(rand()) % number_elements[i];
      vector_container.at(insert);
    }
    std::chrono::high_resolution_clock::time_point t2 = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> time_span = std::chrono::duration_cast<std::chrono::duration<double>>(t2 - t1);
    run_time_vector[i] = time_span.count();
    
    t1 = std::chrono::high_resolution_clock::now();
    for(int j=0; j<number_inserts; j++)
    {
      int insert = static_cast<int>(rand()) % number_elements[i];
      auto iter = list_container.begin();
      std::advance(iter,insert);
      *iter;
      
    }
    t2 = std::chrono::high_resolution_clock::now();
    time_span = std::chrono::duration_cast<std::chrono::duration<double>>(t2 - t1);
    run_time_list[i] = time_span.count();
    
  }
  std::ofstream out("results/random_access");
  for(int i=0; i<n_points; i++)
    out << number_elements[i] << " " << run_time_vector[i] << " " << run_time_list[i] << std::endl;
}


int main ()
{
  
  int n_points = 10;
  int number_operations[n_points];
  int number_elements[n_points];
  
  for(int i=0; i<n_points; i++)
    number_operations[i] = static_cast<int>( (i+1) * 1e3 );
  for(int i=0; i<n_points; i++)
    number_elements[i] = static_cast<int>( (i+1) * 1e3 );
  
  // comparing performance: remove/insert
  int number_inserts = 100000;
  comp_random_remove_insert(n_points, number_elements, number_inserts);
  
  // comparing performance: random access in different containers
  
  comp_random_access(n_points, number_elements, number_inserts);
  
  
  
  
  return 0;
}

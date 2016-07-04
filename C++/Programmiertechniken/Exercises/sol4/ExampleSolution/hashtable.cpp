#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <unordered_map>

int factorial(int n)
{
  int result = 1;
  for(int i=1; i<=n; i++)
    result *= i;
  return result;
}

void print_state(const std::vector<int>& basis_state)
{
  std::cout << "[ ";
  for(size_t i=0; i<basis_state.size()-1; i++)
    std::cout << basis_state[i] << " , ";
  std::cout << basis_state[basis_state.size()-1] << " ]";
}

void set_state(std::vector<int>& state, int i)
{
  int c=0;
  while(i)
  {
    if (i&1)
      state[c]=1;
    else
      state[c]=0;
    i>>=1;
    c++;
  }
  std::reverse(state.begin(),state.end());
}

int get_key(const std::vector<int>& state)
{
  int key=0;
  for(size_t i=0; i<state.size(); i++)
    key += pow(2,state.size()-1-i) * state[i];
  return key;
}

bool states_equal(const std::vector<int>& s1, const std::vector<int>& s2)
{
  return get_key(s1)==get_key(s2);
}

void find_linear(const std::vector<int>& random_state, const std::vector<std::vector<int>>& state_list)
{
  bool found = false;
  for(size_t i=0; i<state_list.size(); i++)
  {
    if(states_equal(random_state,state_list[i]) == true)
    {
      found = true;
      std::cout << "state "; print_state(random_state); std::cout << " was found and has index " << i << std::endl;
      break;
    }
  }
  if(!found)
  {
    std::cout << "state "; print_state(random_state); std::cout << " is not a valid state " << std::endl;
  }
}

bool compare_argsort(std::pair<int,int> i1, std::pair<int,int> i2)
{
  return i1.second < i2.second;
}

int find_value_in_list(std::vector<int> sorted_list, int val)
{
  std::pair<std::vector<int>::iterator,std::vector<int>::iterator> it = std::equal_range (sorted_list.begin(), sorted_list.end(), val);
  if(it.first-it.second == 0)
    return -1;
  else
    return it.first - sorted_list.begin();
}

void find_log(const std::vector<int>& random_state, const std::vector<std::vector<int>>& state_list)
{
  std::vector<std::pair<int,int> > argsort_list;
  for(size_t i=0; i<state_list.size(); i++)
    argsort_list.push_back(std::make_pair(static_cast<int>(i),get_key(state_list[i])));
  
  std::sort(argsort_list.begin(),argsort_list.end(),compare_argsort);
  
  std::vector<int> sorted_list(state_list.size());
  std::vector<int> sorted_indices(state_list.size());
  for(size_t i=0; i<state_list.size(); i++)
  {
    sorted_list[i] = argsort_list[i].second;
    sorted_indices[i] = argsort_list[i].first;
  }
  
  int index = find_value_in_list(sorted_list, get_key(random_state));
  if(index < 0)
  {
    std::cout << "state "; print_state(random_state); std::cout << " is not a valid state " << std::endl;
  }
  else
  {
    std::cout << "state "; print_state(random_state); std::cout << " was found and has index " << sorted_indices[index] << std::endl;
  }

}

void find_constant(const std::vector<int>& random_state, const std::vector<std::vector<int>>& state_list)
{
  std::unordered_map<int,int> key_index_relation;
  for(size_t i=0; i<state_list.size(); i++)
    key_index_relation.insert(std::make_pair(get_key(state_list[i]),i));
  
  
  std::cout << "state "; print_state(random_state); std::cout << " was found and has index " << key_index_relation.at(get_key(random_state)) << std::endl;
  
}

int hash_function(int dec_rep, int number_states)
{
  return dec_rep%number_states;
}

bool compare_hash_val(std::pair<int,int> i1, std::pair<int,int> i2)
{
  return i1.first < i2.first;
}

void find_constant_own_implementation(const std::vector<int>& random_state, const std::vector<std::vector<int>>& state_list)
{
  std::vector<std::pair<int,int>> bucket_list;  // stores hash_val, index
  for(int i=0; i<state_list.size(); i++)
    bucket_list.push_back( std::make_pair( hash_function( get_key(state_list[i]), state_list.size() ), i ) );
  std::sort(bucket_list.begin(), bucket_list.end(), compare_hash_val);
  
  for(size_t i=0; i<bucket_list.size(); i++)
    std::cout << "< " << bucket_list[i].first << "," << bucket_list[i].second << " > ";
  std::cout << std::endl;
  
  std::vector<int> H(bucket_list[bucket_list.size()-1].first,-1);
  for(size_t i=1; i<bucket_list.size(); i++)
    H[bucket_list[bucket_list.size()-1-i].first] = bucket_list.size()-1-i;
  
  for(size_t i=0; i<H.size(); i++)
    std::cout << H[i] << " ";
  std::cout << std::endl;
  
  int hash_val = hash_function( get_key(random_state), state_list.size() );
  int bucket_number = H[ hash_val ];
  int index;
  if(bucket_number < 0)
  {
    std::cout << "state "; print_state(random_state); std::cout << " is not a valid state " << std::endl;
  }
  else
  {
    while(bucket_list[bucket_number].first == hash_val)
    {
      if( states_equal( state_list[bucket_list[bucket_number].second], random_state ) == true )
      {
        
        index = bucket_list[bucket_number].second;
        break;
      }
      bucket_number++;
    }
    std::cout << "state "; print_state(random_state); std::cout << " was found and has index " << index << std::endl;
  }
}

int main ()
{

  int L=6;
  std::vector<std::vector<int>> states;
  std::vector<int> keys;
  
  std::vector<int> new_state(L,0);
  for(int i=0; i<pow(2,L); i++)
  {
    set_state(new_state,i);
    int m=0;
    m = std::accumulate(new_state.begin(),new_state.end(),m);
    if(m==L/2)
    {
      states.push_back(new_state);
      keys.push_back(i);
    }
    std::fill(new_state.begin(),new_state.end(),0);
  }
  
  std::cout << "# of states: " << states.size() << "; should be equal to L!/(L/2)!^2 = " << factorial(L)/factorial(L/2)/factorial(L/2) << std::endl;
  for(size_t i=0; i<states.size(); i++)
  {
    print_state(states[i]);
    std::cout << " ----> key: " << get_key(states[i]) << " ----> index: " << i << std::endl;
  }
  
  std::vector<int> random_state = {1,0,0,1,0,1};
  
  find_linear(random_state, states);
  find_log(random_state, states);
  find_constant(random_state, states);
  find_constant_own_implementation(random_state, states);
  
  return 0;
}

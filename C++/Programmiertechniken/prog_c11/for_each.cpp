

#include<iostream>
#include<vector>
#include<algorithm>   // for_each

using namespace std;

int main() {
  vector<int> v;
  v.push_back( 1 );
  v.push_back( 2 );
  
  for ( auto it = v.begin(); it != v.end(); ++it ) {
    cout << *it << endl;
  }

  for_each( v.begin(), v.end(), [] (int val) {
    cout << val << endl;
  } );
}

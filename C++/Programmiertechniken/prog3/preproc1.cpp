


#define VERSION 1

/* 
The precompiler removes all comments and replaces VERSION below by its value 
Invoke g++ wiht the -E flag
*/


int main() {
  if (VERSION == 1) {
    // OK
  }
  else {
    // NOT OK
  }
  return 0;
}

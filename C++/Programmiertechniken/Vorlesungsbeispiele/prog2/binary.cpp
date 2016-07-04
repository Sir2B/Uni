#include<iostream>

template<typename T>
void printBin(const T& t){
  size_t nBytes=sizeof(T);
  char* rawPtr((char*)(&t));
  bool* rev; rev = new bool[nBytes*CHAR_BIT];
  int inc = nBytes*CHAR_BIT - 1;
  for(size_t byte=0; byte<nBytes; byte++){
    for(size_t bit=0; bit<CHAR_BIT; bit++){
      rev[inc] = (((rawPtr[byte])>>bit)&1);
      inc--;
    }
  }
  for (size_t byte=0; byte<nBytes*CHAR_BIT; byte++) std::cout << rev[byte];
  delete rev;
  std::cout<<std::endl;
};

int main(void){
  for(int32_t i=-15; i<16; i++){
    std::cout<<i<<": ";
    printBin(i);
  }
  //std::cout << -1 << ": "; printBin(-1);
  return 0;
}


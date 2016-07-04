// queue

#include <iostream>       // std::cout
#include <queue>          // std::queue

int main ()
{
  std::queue<int> myqueue;

  myqueue.push(100);
  myqueue.push(20);
  myqueue.push(10);

  myqueue.front() -= myqueue.back();    // 100 - 10 = 90

  std::cout << "myqueue.front() is now " << myqueue.front() << '\n';
  for (int i=myqueue.size()-1; i >=0; i--) {
      std::cout << myqueue.front() << "\n";
      myqueue.pop();
  }
  return 0;
}

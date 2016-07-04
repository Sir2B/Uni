#include <string>
#include <iostream>

class Simulation {    // example of an abstract base class and use of the keyword virtual
public:
  Simulation() {};
  virtual std::string name() const = 0; 
  virtual void run() = 0;
};

class PredatorPrey : public Simulation {
public:
  std::string name() const; 
  void run();
};


std::string PredatorPrey::name() const {
  return static_cast<std::string>("carnivorous");
}

void PredatorPrey::run() {
  /* ... */
  return;
}


int main() {
  //Simulation MySim;			// Error, base class is abstract
  PredatorPrey NewSim;			// OK
  std::cout << NewSim.name() << "\n";
  Simulation& Mysim = NewSim;           // OK, since it is a reference
  return 0;
}


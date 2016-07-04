#include <string>
#include <iostream>

class Simulation {    // example of a base class
public:
  Simulation() : name("hi") {};
  void set_name(const std::string & s) {name = s;};
  void print(std::ostream & os) const { os << name << "\n";}
  std::string name;
};

class PredatorPrey : public Simulation {
public:
  void RK4() { /* ... */}
private:
  double a,b;
};


int main() {
  Simulation MySim;
  MySim.set_name("new simulation"); 	// OK
  MySim.print(std::cout);		// OK
  PredatorPrey NewSim;
  NewSim.print(std::cout); 		// OK
  NewSim.RK4(); // OK
  return 0;
}


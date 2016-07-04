#include <string>
#include <iostream>

class Simulation {    // example of a base class with protected members
public:
  Simulation() : name("hi") {};
  void set_name(const std::string & s) {name = s;};
  void print(std::ostream & os) const { os << name << "\n";}
protected:
  std::string name;
};

class PredatorPrey : public Simulation {
public:
  void RK4() { std::cout << "RK4 calculation of " << name << "\n";}
private:
  double a,b;
};


int main() {
  Simulation MySim;
  MySim.set_name("new simulation"); 	// OK
  MySim.print(std::cout);		// OK
  PredatorPrey NewSim;
  NewSim.set_name("carnivorous");
  NewSim.print(std::cout); 		// OK
  NewSim.RK4(); // OK
  return 0;
}


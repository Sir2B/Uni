#include <string>
#include <iostream>

class Simulation {    // example of a base class
public:
  Simulation() : name("hi") {std::cout << name << "\n";};
  Simulation(const std::string& s) : name(s) {std::cout << name << "\n";};
protected:
  std::string name;
};

class PredatorPrey : public Simulation {
public:
  PredatorPrey(const std::string& s)  {name = s; std::cout << name << "\n";}
  void RK4() { /* ... */}
private:
  double a,b;
};

class Ising : public Simulation {
public:
  Ising(const std::string& s) : Simulation(s)  {name = s; std::cout << name << "\n";}
  void MonteCarloRun() { /* ... */}
private:
  int N;
};


int main() {
  Simulation MySim("new simulation");
  std::cout << "\n\n";
  PredatorPrey NewSim("carnivorous");
  std::cout << "\n\n";
  NewSim.RK4(); // OK
  Ising MCSim("spinning");
  
  return 0;
}


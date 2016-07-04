#include <string>
#include <iostream>

class Simulation {
public:
  Simulation() {};
  virtual std::string name() const = 0; 
  virtual void run() = 0;
};

class PredatorPrey : public Simulation {
public:
  std::string name() const;     // as before
  void run();                   // as before
};


std::string PredatorPrey::name() const {
  return "carnivorous";
}

void PredatorPrey::run() {
  /* ... */
  return;
}

class Ising : public Simulation {
public:
  std::string name() const;     // as before
  void run();                   // as before
};

std::string Ising::name() const {
  return "spinning";
}

void Ising::run() {
  /* ... */
  return;
}

int main() {
  PredatorPrey MyPP;			
  Ising MyIsing;
  Simulation* sim1 = &MyPP;                 // polymorphism
  Simulation* sim2 = &MyIsing;              // polymorphism
  std::cout << sim1->name() << "\t" << sim2->name() << "\n";
  return 0;
}


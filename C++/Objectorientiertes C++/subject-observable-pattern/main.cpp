#include <list>
#include <iterator>
#include <iostream>
#include <cstdlib>
using namespace std;

class Subject;
// Observer: just an interface
class Observer {
public:
     Observer(){};
     virtual ~Observer(){};
     virtual void update(Subject* ) = 0;
};
class Subject {
public:
  Subject();
  virtual ~Subject(){};
  virtual void attach(Observer*);
  virtual void detach(Observer*);
  virtual void notify();
  virtual void setChanged();
private:
  list<Observer*> observers; // list to hold observers
  bool changed;
};

void Subject::setChanged() {
  changed = true ;
}

Subject::Subject() : changed(false) {}

void Subject::attach (Observer* o) {
  observers.push_back( o);
}

void Subject::detach (Observer* o) {
  observers.remove(o);
}

void Subject::notify () {
  // notify observers if changed flag is set
  if ( changed ) {
    list<Observer*>::iterator i = observers.begin();
    for ( ; i!= observers.end(); i++ ) {
      (*i)->update(this);
    }
    changed = false;
  }
}

// real classes using the Observer
class Sensor : public Subject   // simulates temperature sensor
{
private:
    int temp;
public:
    Sensor();
    void takeReading();
    int getReading();
};

Sensor::Sensor()
{
    temp = 20; // set some start value
}

void Sensor::takeReading()
{
    double d;  // randomly change temperature in 50% of times
    d = rand()*1./(RAND_MAX+1.0);
    if(d>0.75)
    {
        temp++;
        setChanged();
    }
    else if (d<0.25)
    {
        temp--;
        setChanged();
    }
    cout << " [Temp: " << temp  << "] ";
}
int Sensor::getReading()
{
    return temp;
}

class Display : public Observer
{
public:
    virtual void update(Subject * o);
};
void Display::update(Subject * o)
{
    Sensor * s = dynamic_cast< Sensor *>(o);
    if ( s )
    {
        cout << "New Temp: " << s->getReading();
    }
}
#include <time.h>
// Get current date/time, format is YYYY-MM-DD.HH:mm:ss
const std::string currentDateTime() {
    time_t     now = time(0);
    struct tm  tstruct;
    char       buf[80];
    tstruct = *localtime(&now);
    // Visit http://en.cppreference.com/w/cpp/chrono/c/strftime
    // for more information about date/time format
    strftime(buf, sizeof(buf), "%X", &tstruct);

    return buf;
}

class GUI: public Observer{
public:
    virtual void update(Subject * o);
    };
    void GUI::update(Subject * o){
        Sensor * s = dynamic_cast<Sensor *>(o);
        time_t timev;
        if (s)
        {
            cout << "\n   the other Observer: Time:" << currentDateTime() << " Temp: " << s->getReading();
        }
    }

int main()
{
    Sensor *sensor = new Sensor();   // subject
    Observer *display = new Display(); // Observer
    Observer *display2 = new GUI(); // Observer2
    // register observer with observable class
    sensor->attach(display);
    sensor->attach(display2);

    // Simulate measuring temp over time
    for(int i=0; i < 20; i++)
    {
        sensor->takeReading();
        sensor->notify();
        cout << endl;
    }
    return 0;
}

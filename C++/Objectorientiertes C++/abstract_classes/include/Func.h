#ifndef FUNC_H
#define FUNC_H


class  Func { // pure abstract class
public:
  virtual double value( double x) = 0;
};

class Nullstelle {
public:
  double find( double x1, double x2, Func &f );
};


#endif // FUNC_H

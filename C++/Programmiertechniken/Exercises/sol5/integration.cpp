#include <iostream>
#include <cassert>
#include <limits>
#include <cmath>
#include <fstream>
#include <iomanip>

//#define NDEBUG

using std::cout;
using std::cerr;
using std::endl;


/* Ex 5.1 ********************************************************************/

/*! Example of integrand function */ 
double linear(double x) {
    return x;
}


/*! Simple Simpson integrator
 *  
 *  @param integrand Function pointer to the integrand function.
 *  @param xmin Lower bound of the integration domain.
 *  @param xmax Upper bound of the integration domain.
 *  @param npoints Number of points used to discretise the domain of integration.
 */
double simpson1(double (*integrand)(double),
        const double xmin, const double xmax, const size_t npoints)
{
    // check that nsteps is even
    assert(npoints % 2 == 0);
 
    double result = 0;
    double dx = (xmax - xmin) / npoints;
    double x = xmin;

    result += integrand(x);
    for(size_t i=1; i<npoints-2; i+= 2) {
        x += dx;
        result += 4 * integrand(x);
        x += dx;
        result += 2 * integrand(x);
    }
    x += dx;
    result += 4 * integrand(x);
    x += dx;
    result += integrand(x);

    result *= dx / 3.0;
    return result;
}

/* Ex 5.2 ********************************************************************/

/*! Functor of a second order polynormial */
class Poly2Functor
{
    private:
    const double _a;
    const double _b;
    const double _c;

    public:
    /*! Constructor
     *  
     *  The coefficients of the polynomial are saved upon construction. */
    Poly2Functor(double a, double b, double c): _a(a), _b(b), _c(c) {}
    /*! Call operator
     *
     *  Returns the evaluation of the polynomial at the requested point x. */
    double operator() (double x) {return _a + _b * x + _c * x * x;}
};

/*! Simpson integrator v2
 *
 *  Now the function is passed via a reference to a functor instead of a
 *  function pointer.
 */
template <typename Functor>
double simpson2(Functor &integrand,
        const double xmin, const double xmax, const size_t npoints)
{
    // check that nsteps is even
    assert(npoints % 2 == 0);
 
    double result = 0;
    double dx = (xmax - xmin) / npoints;
    double x = xmin;

    result += integrand(x);
    for(size_t i=1; i<npoints-2; i+= 2) {
        x += dx;
        result += 4 * integrand(x);
        x += dx;
        result += 2 * integrand(x);
    }
    x += dx;
    result += 4 * integrand(x);
    x += dx;
    result += integrand(x);

    result *= dx / 3.0;
    return result;
}


/* Ex 5.3 ********************************************************************/

/*! Simpson integrator v3
 *
 *  We also template the type of the domain bounds.
 *  We use the <limits> library to check whether the type being passed
 *  represents a real or an integer.
 */
template <typename Functor, typename Scalar>
double simpson3(Functor &integrand,
        const Scalar xmin, const Scalar xmax, const size_t npoints)
{
    // check that nsteps is even
    assert(npoints % 2 == 0);
 
    double result = 0;
    double x = xmin;
    double dx;
    if (std::numeric_limits<Scalar>::is_integer) {
        // We only cast to double if the bounds are passed with integer types.
        dx = double(xmax - xmin) / npoints;
    }
    else {
        dx = (xmax - xmin) / npoints;
    }

    result += integrand(x);
    for(size_t i=1; i<npoints-2; i+= 2) {
        x += dx;
        result += 4 * integrand(x);
        x += dx;
        result += 2 * integrand(x);
    }
    x += dx;
    result += 4 * integrand(x);
    x += dx;
    result += integrand(x);

    result *= dx / 3.0;
    return result;
}



/* Ex 5.4 ********************************************************************/

/*! Riemann integrator (rectangles) */
template <typename Functor, typename Scalar>
double riemann(Functor &integrand,
        const Scalar xmin, const Scalar xmax, const size_t npoints)
{
    double result = 0;
    double x = xmin;
    double dx;
    if (std::numeric_limits<Scalar>::is_integer) {
        // We only cast to double if the bounds are passed with integer types.
        dx = double(xmax - xmin) / npoints;
    }
    else {
        dx = (xmax - xmin) / npoints;
    }
    for(size_t i=0; i<npoints; i++) {
        result += integrand(x) * dx;
        x += dx;
    }
    return result;
}

/*! Trapezoid integrator */
template <typename Functor, typename Scalar>
double trapezoid(Functor &integrand,
        const Scalar xmin, const Scalar xmax, const size_t npoints)
{
    double result = 0;
    double x = xmin;
    double dx;
    if (std::numeric_limits<Scalar>::is_integer) {
        // We only cast to double if the bounds are passed with integer types.
        dx = double(xmax - xmin) / npoints;
    }
    else {
        dx = (xmax - xmin) / npoints;
    }
    result += 0.5 * (integrand(xmin) + integrand(xmax));
    for (size_t i=1; i<npoints; i++) {
        x += dx;
        result += integrand(x);
    }
    result *= dx;
    return result;
}

class SinFunctor
{
    private:
    const double _omega;

    public:
    SinFunctor(double omega): _omega(omega) {}
    double operator() (double x) {return std::sin(_omega * x);}
};


class ExpSinSqFunctor
{
    public:
    ExpSinSqFunctor() {}
    double operator() (double x)
    {
        double dummy = std::sin(x);
        return std::exp(- dummy * dummy);
    }
};



int main() {

    // function pointer to integrand
    double (*integrand) (double);
    integrand = &linear;

    cerr << "Ex 5.1\n";
    cerr << "integral of x from 0 to 1\n";
    cerr << simpson1(integrand, 0, 1, 1000) << endl;

    cerr <<  "Ex 5.2\n";
    Poly2Functor mypoly2(1, 0.5, 2.5);
    cerr << "integral of 1 + x/2 + x^2 * 2.5 from 0 to 1\n";
    cerr << simpson2(mypoly2, 0, 1, 1000) << endl;

    cerr << "Ex 5.3\n";
    cerr << "integral of 1 + x/2 + x^2 * 2.5 from 0 to 1\n";
    int xmin = 0;
    int xmax = 1;
    cerr << simpson3(mypoly2, xmin, xmax, 1000) << endl;


    cerr << "Ex 5.4\n"
         << "Performance of different integrators\n";

    // Define test functions
    Poly2Functor constant(0, 0, 0); // f(x) = 0
    Poly2Functor poly1(0, 1, 0);    // f(x) = x
    Poly2Functor poly2(0, 0, 1);    // f(x) = x^2
    SinFunctor sinx(1);             // f(x) = sin(x)
    SinFunctor sin5x(5);            // f(x) = sin(5x)
    ExpSinSqFunctor expsinsq;  // f(x) = exp(-sin^2(x))

    std::ofstream file_constant("constant.dat");
    std::ofstream file_poly1("poly1.dat");
    std::ofstream file_poly2("poly2.dat");
    std::ofstream file_sinx("sinx.dat");
    std::ofstream file_sin5x("sin5x.dat");
    std::ofstream file_expsinsq("expsinsq.dat");

    file_constant << std::setprecision(15);
    file_poly1    << std::setprecision(15);
    file_poly2    << std::setprecision(15);
    file_sinx     << std::setprecision(15);
    file_sin5x    << std::setprecision(15);
    file_expsinsq << std::setprecision(15);

    double result = 0;

    file_constant << "#Npoints\tRiemann\tTrapez\tSimpson\n";
    for(size_t n=4; n<(1<<18); n*=2) {
        file_constant << n << "\t"
            <<   riemann(constant, 0, 1, n) << "\t"
            << trapezoid(constant, 0, 1, n) << "\t"
            <<  simpson3(constant, 0, 1, n) << "\n";
    }
    file_constant.close();

    file_poly1 << "#Npoints\tRiemann\tTrapez\tSimpson\n";
    result = .5;
    for(size_t n=4; n<(1<<18); n*=2) {
        file_poly1 << n << "\t"
            << std::fabs(  riemann(poly1, 0, 1, n) - result) << "\t"
            << std::fabs(trapezoid(poly1, 0, 1, n) - result) << "\t"
            << std::fabs( simpson3(poly1, 0, 1, n) - result) << "\n";
    }
    file_poly1.close();

    file_poly2 << "#Npoints\tRiemann\tTrapez\tSimpson\n";
    result = 1. / 3.;
    for(size_t n=4; n<(1<<18); n*=2) {
        file_poly2 << n << "\t"
            << std::fabs(  riemann(poly2, 0, 1, n) - result) << "\t"
            << std::fabs(trapezoid(poly2, 0, 1, n) - result) << "\t"
            << std::fabs( simpson3(poly2, 0, 1, n) - result) << "\t"
            << "\n";
    }
    file_poly2.close();

    file_sinx << "#Npoints\tRiemann\tTrapez\tSimpson\n";
    result = 1 - std::cos(1);
    for(size_t n=4; n<(1<<18); n*=2) {
        file_sinx << n << "\t"
            << std::fabs(  riemann(sinx, 0, 1, n) - result) << "\t"
            << std::fabs(trapezoid(sinx, 0, 1, n) - result) << "\t"
            << std::fabs( simpson3(sinx, 0, 1, n) - result) << "\t"
            << "\n";
    }
    file_sinx.close();

    file_sin5x << "#Npoints\tRiemann\tTrapez\tSimpson\n";
    result = (1 - std::cos(5)) / 5.;
    for(size_t n=4; n<(1<<18); n*=2) {
        file_sin5x << n << "\t"
            << std::fabs(  riemann(sin5x, 0, 1, n) - result) << "\t"
            << std::fabs(trapezoid(sin5x, 0, 1, n) - result) << "\t"
            << std::fabs( simpson3(sin5x, 0, 1, n) - result) << "\t"
            << "\n";
    }
    file_sin5x.close();

    file_expsinsq << "#Npoints\tRiemann\tTrapez\tSimpson\n";
    result = 0.77982019932192;
    for(size_t n=4; n<(1<<18); n*=2) {
        file_expsinsq << n << "\t"
            << std::fabs(  riemann(expsinsq, 0, 1, n) - result) << "\t"
            << std::fabs(trapezoid(expsinsq, 0, 1, n) - result) << "\t"
            << std::fabs( simpson3(expsinsq, 0, 1, n) - result) << "\t"
            << "\n";
    }
    file_expsinsq.close();

    return 0;
}


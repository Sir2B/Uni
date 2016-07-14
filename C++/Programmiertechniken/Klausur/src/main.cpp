
#include <iostream>
#include <cmath>
#include <limits>

using std::cout;
using std::cerr;
using std::endl;


template <typename Functor, typename LowerFunctor, typename UpperFunctor>
double riemann_2d(Functor& integrand, const double xmin, 
                  const double xmax, LowerFunctor& ymin, 
                  UpperFunctor& ymax, const size_t npoints)
{
	double result = 0;
    double x = xmin;
    double dx;

    dx = (xmax - xmin) / npoints;

	for(size_t i=0; i<npoints; i++) {
		double y_min = ymin(x);
		double y_max = ymax(x);
		double dy = (y_max - y_min) /npoints;
		double y = y_min;

		for (size_t j=0; j<npoints; j++)
		{
    		result += integrand(x, y) * dx * dy;
			y += dy;
		}
        x += dx;
    }

	return result;
}

/*! Riemann integrator (rectangles) */
template <typename Return, typename Functor, typename Scalar>
Return riemann(Functor &integrand,
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

class MyFunctor
{
	private:
	public:
	MyFunctor() {}
	double operator () (double x, double y)
	{
		double wurzel = std::sqrt(x*x+y*y);
		if (wurzel == 0)
		{
			//todo: was soll dann passieren?
			return 0;
		}
		return std::sin(wurzel)/wurzel;
	}
	double operator () (double x)
	{
		return operator()(x, 0);
	}
};

class Grenzen
{
	private:
		int _sign;
	public:
	Grenzen(int sign): _sign(sign) {}
	double operator () (double x)
	{
		return std::sqrt(M_PI*M_PI-x*x) * _sign;
	}
};

template <typename Functor>
double numeric_solution(Functor& functor, int npoints)
{
	double rmin = 0;
	double rmax = M_PI;
	double phi_min = 0;
	double phi_max = 2*M_PI;
	
	double r = riemann<double>(functor, rmin, rmax, npoints);
	
	return r * phi_max;
	
}

int main(int argc, char** argv)
{
	int npoints;
	
	if (argc != 2)
	{
		cout << "not an valid parameter" << endl;
		return 0;
	}

	npoints = std::atoi(argv[1]);
	std::string s = std::to_string(npoints);
	if (s != argv[1])
	{
		cout << "not an valid parameter" << endl;
		return 0;
	}

	auto myfunctor = MyFunctor();
	double xmin = -M_PI;
	double xmax = M_PI;
	auto ymin = Grenzen(-1);
	auto ymax = Grenzen(1);
	
	
	cout << riemann_2d (myfunctor, xmin, xmax, ymin, ymax, npoints) << endl;
	cout << numeric_solution (myfunctor, npoints) << endl;

	
	return 0;
}


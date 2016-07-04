#include <iostream>
#include <ostream>
#include <valarray>

using std::ostream;
using std::cout;

// 1(b) ***********************************************************************
class HarmonicOscillator
{
    private:
    const double k;
    double x;
    double p;
    public:
    HarmonicOscillator(const double _k): k(_k) {}
    double xdot() {return p;}
    double pdot() {return -k*x;}
    double xdot(double _x, double _p) {return _p;}
    double pdot(double _x, double _p) {return -k*_x;}
    const double& get_x() const {return x;}
    const double& get_p() const {return p;}
    double& set_x() {return x;}
    double& set_p() {return p;}

};

ostream& operator<< (ostream& os, HarmonicOscillator &ho) {
    os << ho.get_x() << "\t" << ho.get_p();
    return os;
}

// 1(c) ***********************************************************************

void Euler(HarmonicOscillator &ho, double dt)
{
    double xdot = ho.xdot();
    double pdot = ho.pdot();
    ho.set_x() += xdot * dt;
    ho.set_p() += pdot * dt;
}

// 1(e) ***********************************************************************

void EulerSymplectic(HarmonicOscillator &ho, double dt)
{
    ho.set_x() += ho.xdot() * dt;
    ho.set_p() += ho.pdot() * dt;
}


void RungeKutta2(HarmonicOscillator &ho, double dt)
{
    double x_n_plus_half = ho.get_x() + ho.xdot() * dt / 2;
    double p_n_plus_half = ho.get_p() + ho.pdot() * dt / 2;

    ho.set_x() += dt * ho.xdot(x_n_plus_half, p_n_plus_half);
    ho.set_p() += dt * ho.pdot(x_n_plus_half, p_n_plus_half);
}


void RungeKutta4(HarmonicOscillator &ho, double dt)
{
    double x_k1 = dt * ho.xdot();
    double p_k1 = dt * ho.pdot();
    double x_k2 = dt * ho.xdot(ho.get_x() + x_k1/2., ho.get_p() + p_k1/2.);
    double p_k2 = dt * ho.pdot(ho.get_x() + x_k1/2., ho.get_p() + p_k1/2.);
    double x_k3 = dt * ho.xdot(ho.get_x() + x_k2/2., ho.get_p() + p_k2/2.);
    double p_k3 = dt * ho.pdot(ho.get_x() + x_k2/2., ho.get_p() + p_k2/2.);
    double x_k4 = dt * ho.xdot(ho.get_x() + x_k3   , ho.get_p() + p_k3);
    double p_k4 = dt * ho.pdot(ho.get_x() + x_k3   , ho.get_p() + p_k3);
    
    ho.set_x() += (x_k1 + 2 * (x_k2 + x_k3) + x_k4) / 6.;
    ho.set_p() += (p_k1 + 2 * (p_k2 + p_k3) + p_k4) / 6.;
}

// 1(f) ***********************************************************************

using arrayd = std::valarray<double>;

template <size_t d>
class HarmonicOscillatorTPL
{
    private:
    arrayd k = arrayd(d);
    arrayd x = arrayd(d);
    arrayd p = arrayd(d);
    public:
    HarmonicOscillatorTPL() {}

    void setk(const double ki, const size_t i) {k[i] = ki;}
    void setx(const double xi, const size_t i) {x[i] = xi;}
    void setp(const double pi, const size_t i) {p[i] = pi;}

    arrayd xdot() {return p;}
    arrayd pdot() {return -k*x;}
    arrayd xdot(const arrayd _x, const arrayd _p) {return _p;}
    arrayd pdot(const arrayd _x, const arrayd _p) {return -k*_x;}
    const arrayd get_x() const {return x;}
    const arrayd get_p() const {return p;}
    arrayd& set_x() {return x;}
    arrayd& set_p() {return p;}
};

template <size_t d>
ostream& operator<< (ostream& os, HarmonicOscillatorTPL<d> ho)
{
    const arrayd &x = ho.get_x();
    const arrayd &p = ho.get_p();
    for(size_t i=0; i<d-1; i++) {
        os << x[i] << "\t" << p[i] << "\t";
    }
    os << x[d-1] << "\t" << p[d-1];
    return os;
}



template <typename Hamiltonian>
void EulerTPL(Hamiltonian &ho, double dt)
{
    arrayd xdot = ho.xdot();
    arrayd pdot = ho.pdot();
    ho.set_x() += xdot * dt;
    ho.set_p() += pdot * dt;
}


template <typename Hamiltonian>
void EulerSymplecticTPL(Hamiltonian &ho, double dt)
{
    ho.set_x() += ho.xdot() * dt;
    ho.set_p() += ho.pdot() * dt;
}


template <typename Hamiltonian>
void RungeKutta2TPL(Hamiltonian &ho, double dt)
{
    arrayd x_n_plus_half = ho.get_x() + ho.xdot() * dt / 2;
    arrayd p_n_plus_half = ho.get_p() + ho.pdot() * dt / 2;

    ho.set_x() += dt * ho.xdot(x_n_plus_half, p_n_plus_half);
    ho.set_p() += dt * ho.pdot(x_n_plus_half, p_n_plus_half);
}


template <typename Hamiltonian>
void RungeKutta4TPL(Hamiltonian &ho, double dt)
{
    arrayd x_k1 = dt * ho.xdot();
    arrayd p_k1 = dt * ho.pdot();
    arrayd x_k2 = dt * ho.xdot(ho.get_x() + x_k1/2., ho.get_p() + p_k1/2.);
    arrayd p_k2 = dt * ho.pdot(ho.get_x() + x_k1/2., ho.get_p() + p_k1/2.);
    arrayd x_k3 = dt * ho.xdot(ho.get_x() + x_k2/2., ho.get_p() + p_k2/2.);
    arrayd p_k3 = dt * ho.pdot(ho.get_x() + x_k2/2., ho.get_p() + p_k2/2.);
    arrayd x_k4 = dt * ho.xdot(ho.get_x() + x_k3   , ho.get_p() + p_k3);
    arrayd p_k4 = dt * ho.pdot(ho.get_x() + x_k3   , ho.get_p() + p_k3);
    
    ho.set_x() += (x_k1 + 2 * (x_k2 + x_k3) + x_k4) / 6.;
    ho.set_p() += (p_k1 + 2 * (p_k2 + p_k3) + p_k4) / 6.;
}


 
int main()
{
    HarmonicOscillator ho(1.0);
    ho.set_x() = 1;
    ho.set_p() = 0;

    HarmonicOscillator hosymp(1.0);
    hosymp.set_x() = 1;
    hosymp.set_p() = 0;

    HarmonicOscillator hork2(1.0);
    hork2.set_x() = 1;
    hork2.set_p() = 0;

    HarmonicOscillator hork4(1.0);
    hork4.set_x() = 1;
    hork4.set_p() = 0;

    double dt = 0.1;
    for (double t=0; t<20; t+=0.1) {
        Euler(ho, dt);
        EulerSymplectic(hosymp, dt);
        RungeKutta2(hork2, dt);
        RungeKutta4(hork4, dt);
        cout << t     << "\t"
             << ho    << "\t" << hosymp << "\t"
             << hork2 << "\t" << hork4 << "\n";
    }

    cout << "\n\n\n";

    HarmonicOscillatorTPL<2> ho2d;
    ho2d.setk(4, 0);
    ho2d.setk(9, 1);
    ho2d.setx(1, 0);
    ho2d.setx(1, 1);
    ho2d.setp(1, 0);
    ho2d.setp(1, 1);
    for (double t=0; t<20; t+=0.1) {
        // EulerTPL(ho2d, dt);
        // EulerSymplecticTPL(ho2d, dt);
        // RungeKutta2TPL(ho2d, dt);
        RungeKutta4TPL(ho2d, dt);
        cout << t     << "\t"
             << ho2d << "\n";
    }

    return 0;
}


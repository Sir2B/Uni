#include <iostream>
#include <cmath>
#include "vec.hpp"
#include "mat.hpp"

using namespace Vec;

vec<2,double> rotate(vec<2,double> v, double phi) {
    return {v[0] * cos(phi) - v[1] * sin(phi),
            v[0] * sin(phi) + v[1] * cos(phi)};
}

int main () {
    vec<3,double> zero;
    vec<3,double> ones(1);
    const char *string = "hello";
    vec<5,char> u(string);
    vec<3,double> v = { 1, 2, 3};
    vec<3,double> w(v);
    std::cout << zero << std::endl
              << ones << std::endl
              << u << std::endl
              << v << std::endl
              << w << std::endl;
    v *= 2.;
    w += ones;
    std::cout << v << " * " << w << " = " << (v*w) << std::endl;
    vec<3,double> x = cross(v, w);
    std::cout << x << " * " << v << " = " << x*v << std::endl;

    vec<2,int> e1 = {1, 0};
    vec<2,double> r = rotate(e1, M_PI/4);
    std::cout << r << std::endl;
    std::cout << vec<2,double>(e1) * r << std::endl;

    mat<2,2,int> m = {{ 1, 2},
                      { 3, 4}};
    mat<2,2,int> p = {{ 0, 1},
                      { 1, 0}};
    std::cout << m * p << std::endl
              << p * m << std::endl;

    return 0;
}

#pragma once
#include <iostream>

namespace Vec {

    template <size_t N, typename T = double>
    class vec {
        private:
            // fixed-size stack-allocated memory
            T data[N];
        public:
            // copy assignment operator
            template <typename T2>
            vec& operator=(const vec<N,T2>& x) {
                for (size_t i = 0; i < N; ++i)
                    data[i] = x[i];
                return *this;
            }


            // constructors

            // default constructor
            vec() : data{} {
                // `:` marks beginning of initialization part of constructor
                // definition,  `data{}` initializes data array with zeros,
                // nothing else left to do here
            }

            // copy constructor -- call copy assignment
            template <typename T2>
            vec(const vec<N,T2>& x) {
                *this = x;
            }

            // construct with same value in each element
            vec(const T& val) {
                for (size_t i = 0; i < N; ++i)
                    data[i] = val;
            }

            // construct from continguous memory starting from a pointer
            vec(const T* p) {
                for (size_t i = 0; i < N; ++i)
                    data[i] = p[i];
            }

            // construct from curly-brace expression
            vec(std::initializer_list<T> il) {
                size_t i;
                const T* it;
                for (i = 0, it = il.begin(); it != il.end() && i < N; ++i, ++it)
                    data[i] = *it;
                for (; i < N; ++i)
                    data[i] = T();
            }

            template <size_t N_, typename T_>
            friend std::ostream& operator<< (std::ostream&, const vec<N_,T_>&);


            // operators

            // random access
            inline const T& operator[](size_t i) const {
                return data[i];
            }

            inline T& operator[](size_t i) {
                return data[i];
            }

            // unary sign operators
            vec operator+() const {
                return vec(*this);
            }

            vec operator-() const {
                vec res;
                for (size_t i = 0; i < N; ++i)
                    res.data[i] = -data[i];
                return res;
            }

            // add / subtract from this vector
            vec& operator+= (const vec& rhs) {
                for (size_t i = 0; i < N; ++i)
                    data[i] += rhs.data[i];
                return *this;
            }

            vec& operator-= (const vec& rhs) {
                for (size_t i = 0; i < N; ++i)
                    data[i] -= rhs.data[i];
                return *this;
            }

            // multiply by a scalar
            vec& operator*= (const T& val) {
                for (size_t i = 0; i < N; ++i)
                    data[i] *= val;
                return *this;
            }

            vec& operator/= (const T& val) {
                for (size_t i = 0; i < N; ++i)
                    data[i] /= val;
                return *this;
            }
    };


    // dot product
    template <size_t N, typename T>
    T operator*(const vec<N,T>& lhs, const vec<N,T>& rhs) {
        T sum;
        for (size_t i = 0; i < N; ++i)
            sum += lhs[i] * rhs[i];
        return sum;
    }


    // cross product
    template <typename T>
    vec<3,T> cross(const vec<3,T>& lhs, const vec<3,T>& rhs) {
        return {lhs[1] * rhs[2] - lhs[2] * rhs[1],
                lhs[2] * rhs[0] - lhs[0] * rhs[2],
                lhs[0] * rhs[1] - lhs[1] * rhs[0]};
    }


    // scalar multiplication
    template <size_t N, typename T>
    vec<N,T> operator* (const T& val, const vec<N,T>& rhs) {
        vec<N,T> res(rhs);
        res *= val;
        return res;
    }

    template <size_t N, typename T>
    vec<N,T> operator* (const vec<N,T>& lhs, const T& val) {
        vec<N,T> res(lhs);
        res *= val;
        return res;
    }

    template <size_t N, typename T>
    vec<N,T> operator/ (const vec<N,T>& lhs, const T& val) {
        vec<N,T> res(lhs);
        res /= val;
        return res;
    }


    // addition & subtraction operators
    template <size_t N, typename T>
    vec<N,T> operator+ (const vec<N,T>& lhs, const vec<N,T>& rhs) {
        vec<N,T> res(lhs);
        res += rhs;
        return res;
    }

    template <size_t N, typename T>
    vec<N,T> operator- (const vec<N,T>& lhs, const vec<N,T>& rhs) {
        vec<N,T> res(lhs);
        res -= rhs;
        return res;
    }


    // (in)equality operators
    template <size_t N, typename A, typename B>
    bool operator== (const vec<N,A>& lhs, const vec<N,B>& rhs) {
        for (size_t i = 0; i < N; ++i)
            if (lhs[i] != rhs[i])
                return false;
        return true;
    }

    template <size_t N, typename A, typename B>
    bool operator!= (const vec<N,A>& lhs, const vec<N,B>& rhs) {
        return !(lhs == rhs);
    }


    // stream operators
    template <size_t N, typename T>
    std::ostream& operator<< (std::ostream& os, const vec<N,T>& rhs) {
        os << "(" << rhs.data[0];
        for (size_t i = 1; i < N; ++i)
            os << ", " << rhs.data[i];
        os << ")";
        return os;
    }
}

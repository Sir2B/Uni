#pragma once
#include <iostream>
#include <initializer_list>
#include <cmath>
#include "vec.hpp"

namespace Vec {

    template <size_t M, size_t N = M, typename T = double>
    class mat {
        private:
            // fixed-size stack-allocated memory
            vec<N,T> rows[M];
        public:
            // copy assignment operator
            template <typename T2>
            mat& operator=(const mat<M,N,T2>& x) {
                for (size_t i = 0; i < M; ++i)
                    rows[i] = x[i];
                return *this;
            }


            // constructors

            // default constructor
            mat() : rows{} { }

            // construct with same value in each element
            mat(const T& val) {
                for (size_t i = 0; i < M; ++i)
                    rows[i] = vec<N,T>(val);
            }

            // construct from continguous memory starting from a pointer
            // assuming row-major order
            mat(const T* p) {
                for (size_t i = 0; i < M; ++i, p += N)
                    rows[i] = vec<N,T>(p);
            }

            // copy constructor -- call copy assignment
            template <typename T2>
            mat(const mat<M,N,T2>& x) {
                *this = x;
            }

            // construct from curly-brace expression
            mat(std::initializer_list<vec<N,T>> il) {
                size_t i;
                const vec<N,T>* it;
                for (i = 0, it = il.begin(); it != il.end() && i < M; ++i, ++it)
                    rows[i] = *it;
                for (; i < M; ++i)
                    rows[i] = vec<N,T>();
            }


            // operators

            // random access
            inline const vec<N,T>& operator[](size_t i) const {
                return rows[i];
            }

            inline vec<N,T>& operator[](size_t i) {
                return rows[i];
            }

            const vec<M,T> col(size_t j) const {
                vec<M,T> res;
                for (size_t i = 0; i < M; ++i)
                    res[i] = rows[i][j];
                return res;
            }

            // unary sign operators
            mat operator+() const {
                return mat(*this);
            }

            mat operator-() const {
                mat res;
                for (size_t i = 0; i < M; ++i)
                    res.rows[i] = -rows[i];
                return res;
            }

            // add / subtract from this vector
            mat& operator+= (const mat& rhs) {
                for (size_t i = 0; i < M; ++i)
                    rows[i] += rhs.rows[i];
                return *this;
            }

            mat& operator-= (const mat& rhs) {
                for (size_t i = 0; i < M; ++i)
                    rows[i] -= rhs.rows[i];
                return *this;
            }

            // multiply by a scalar
            mat& operator*= (const T& val) {
                for (size_t i = 0; i < M; ++i)
                    rows[i] *= val;
                return *this;
            }

            mat& operator/= (const T& val) {
                for (size_t i = 0; i < M; ++i)
                    rows[i] /= val;
                return *this;
            }
    };


    // matrix product
    template <size_t M, size_t N, typename T>
    vec<M,T> operator* (const mat<M,N,T>& lhs, const vec<N,T>& rhs) {
        vec<M,T> res;
        for (size_t i = 0; i < M; ++i)
            res[i] = lhs[i] * rhs;
        return res;
    }

    template <size_t M, size_t N, typename T>
    vec<N,T> operator* (const vec<M,T>& lhs, const mat<M,N,T>& rhs) {
        vec<N,T> res;
        for (size_t i = 0; i < N; ++i)
            res[i] = lhs * rhs.col(i);
        return res;
    }

    template <size_t M, size_t N, size_t P, typename T>
    mat<M,P,T> operator* (const mat<M,N,T>& lhs, const mat<N,P,T>& rhs) {
        mat<M,P,T> res;
        for (size_t i = 0; i < M; ++i)
            res[i] = lhs[i] * rhs;
        return res;
    }


    // scalar multiplication
    template <size_t M, size_t N, typename T>
    mat<M,N,T> operator* (const T& val, const mat<M,N,T>& rhs) {
        mat<M,N,T> res(rhs);
        res *= val;
        return res;
    }

    template <size_t M, size_t N, typename T>
    mat<M,N,T> operator* (const mat<M,N,T>& lhs, const T& val) {
        mat<M,N,T> res(lhs);
        res *= val;
        return res;
    }

    template <size_t M, size_t N, typename T>
    mat<M,N,T> operator/ (const mat<M,N,T>& lhs, const T& val) {
        mat<M,N,T> res(lhs);
        res /= val;
        return res;
    }


    // addition & subtraction operators
    template <size_t M, size_t N, typename T>
    mat<M,N,T> operator+ (const mat<M,N,T>& lhs, const mat<M,N,T>& rhs) {
        mat<M,N,T> res(lhs);
        res += rhs;
        return res;
    }

    template <size_t M, size_t N, typename T>
    mat<M,N,T> operator- (const mat<M,N,T>& lhs, const mat<M,N,T>& rhs) {
        mat<M,N,T> res(lhs);
        res -= rhs;
        return res;
    }


    // (in)equality operators
    template <size_t M, size_t N, typename A, typename B>
    bool operator== (const mat<M,N,A>& lhs, const mat<M,N,B>& rhs) {
        for (size_t i = 0; i < M; ++i)
            if (lhs[i] != rhs[i])
                return false;
        return true;
    }

    template <size_t M, size_t N, typename A, typename B>
    bool operator!= (const mat<M,N,A>& lhs, const mat<M,N,B>& rhs) {
        return !(lhs == rhs);
    }


    // stream operators
    template <size_t M, size_t N, typename T>
    std::ostream& operator<< (std::ostream& os, const mat<M,N,T>& rhs) {
        os << "(" << rhs[0];
        for (size_t i = 1; i < M; ++i)
            os << ", " << rhs[i];
        os << ")";
        return os;
    }
}

g++ -c cmpl.cpp
g++ -c cmpl2.cpp
rm *.a
ar rc libcmpl.a cmpl.o cmpl2.o
g++ -o cmpl_main main.cpp -L. -lcmpl

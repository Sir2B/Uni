cmake_minimum_required (VERSION 2.6)
project (Tutorial)
# should we use our own complex functions?
option (USE_MYCMPL 
        "Use Tutorial provided complex implementation" ON) 

if (USE_MYCMPL)
  add_library(ComplexFunctions STATIC cmpl.cpp cmpl2.cpp)
  set (EXTRA_LIBS ${EXTRA_LIBS} ComplexFunctions)
endif (USE_MYCMPL)


# add the executable
add_executable (Tutorial main.cpp)
target_link_libraries (Tutorial  ${EXTRA_LIBS})

install (TARGETS Tutorial DESTINATION bin)
install (FILES cmpl.h DESTINATION include)
install (TARGETS ComplexFunctions DESTINATION lib)

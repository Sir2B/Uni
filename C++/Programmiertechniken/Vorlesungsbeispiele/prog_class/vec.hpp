#ifndef GUARD_VEC
#define GUARD_VEC

#include <stddef.h>			// for size_t and ptrdiff_t
#include <memory>			// for allocator class
#include <algorithm>
#include <assert.h>


template <class T> class Vec {
public:
  typedef T* iterator;
  typedef const T* const_iterator;
  typedef std::size_t size_type;
  typedef T value_type;
  typedef T& reference;
  typedef const T& const_reference;

  Vec() { create(); }
  explicit Vec(size_type n, const T& t = T()) { create(n, t);}
  Vec(const Vec& v) { create(v.begin(), v.end()); }
    
  Vec& operator=(const Vec&);
  
    
  ~Vec() { uncreate();}

  T& operator[](size_type i) { return data[i];}
  const T& operator[] (size_type i) const { return data[i]; }

  Vec& operator+=(const Vec& );
  
  Vec& operator*=(const T&);
    
  void push_back(const T& val) {
    if (avail == limit)
      grow();
    unchecked_append(val); 
  }

  size_type size() const { return avail - data;}

  iterator begin() { return data;}
  const_iterator begin() const { return data;}
  
  iterator end() { return avail;}
  const_iterator end() const { return avail;}  

  template <class In> void insert(iterator, In, In);
  template <class In> void assign(In, In);

private:
  iterator data;    // first element in the Vec
  iterator avail;   // one past the last element in the Vec
  iterator limit;   // one past the allocated memory

  // facilities for memory allocation
  std::allocator<T> alloc; // object to handle memory allocation

  // allocate and initialize the underlying array
  void create();
  void create(size_type, const T&);
  void create(const_iterator, const_iterator);

  // destroy the elements in the array and free the memory
  void uncreate();

  // support functions for push_back
  void grow();
  void unchecked_append(const T&);
};

template <class T> 
void Vec<T>::create() {
  data = avail = limit = 0;
}

template <class T>
void Vec<T>::create(size_type n, const T& val) {
    data = alloc.allocate(n);
    limit = avail = data +n;
    std::uninitialized_fill(data, limit, val);
}

template<class T>
void Vec<T>::create(const_iterator i, const_iterator j) {
    data = alloc.allocate(j-i);
    limit = avail = std::uninitialized_copy(i,j,data);
}

template<class T>
void Vec<T>::uncreate() {
    if (data) {
        // destroy in reverse order the elements that were constructed
        iterator it = avail;
        while (it != data)
        alloc.destroy(--it);
        // return the space that was allocated
        alloc.deallocate(data, limit - data);
    }
    data = limit=avail = 0;
}

template<class T>
void Vec<T>::grow() {
    // when growing, allocate twice as much space as currently in use
    size_type new_size = max(2 * (limit - data), ptrdiff_t(1));
    
    // allocate new space and copy existing elements into the new space
    iterator new_data = alloc.allocate(new_size);
    iterator new_avail = std::uninitialized_copy(data, avail, new_data);
    
    // return the old space
    uncreate();
    
    // reset pointers to point to the newly allocated space
    data = new_data;
    avail = new_avail;
    limit = data + new_size;
}

template <class T>
void Vec<T>::unchecked_append(const T& val) {
    alloc.construct(avail++, val);
}

template <class T>
Vec<T>& Vec<T>::operator=(const Vec<T>& rhs) {
    // check for self-assignment
    if (&rhs != this) {
        // free the array on the left-hand side
        uncreate();
        // copy elements from the right-hand to the left-hand side
        create(rhs.begin(), rhs.end());
    }
    return *this;
}

template <class T> template <class In>
void Vec<T>::insert(iterator p, In i, In j) {
    size_type new_size = (avail - data) + (j - i);
    iterator new_data = alloc.allocate(new_size);
    std::uninitialized_copy(data, p, new_data);
    std::uninitialized_copy(i, j, new_data + (p - data));
    iterator new_avail = std::uninitialized_copy(p, avail, new_data + (p - data) + (j - i));
    
    uncreate();
    
    data = new_data;
    avail = new_avail;
    limit = data + new_size;
}

template <class T> template <class In>
void Vec<T>::assign(In i, In j) {
    uncreate();
    create(i, j);
}

template <class T>
inline Vec<T>& Vec<T>::operator+=(const Vec<T>& v2) {
  assert(avail - data >= v2.avail - v2.data);
  Vec<T>::iterator it = data;
  for (Vec<T>::iterator it1 = v2.data; it1 != v2.avail; ++it1, ++it) (*it)+= (*it1);
  return *this;
}

template <class T>
Vec<T> operator+(const Vec<T>& v1, const Vec<T>& v2) {
  Vec<T> vnew = v1;
  vnew += v2;
  return vnew;
}

template <class T>
inline Vec<T>& Vec<T>::operator*=(const T& alpha) {
  for (Vec<T>::iterator it = data; it != avail; ++it) (*it) *= alpha;
  return *this;
}


#endif

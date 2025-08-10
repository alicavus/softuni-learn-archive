#pragma once
#include <deque>

template<typename T>
class Array : public std::deque<T>{
    public:
    Array(size_t size) : std::deque<T>(size){};

    size_t getSize() const{
        return this->size();
    }
};
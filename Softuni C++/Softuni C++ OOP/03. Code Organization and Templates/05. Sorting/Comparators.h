#pragma once

#include <iostream>
#include <sstream>

template<typename T>
struct LessThan{
    bool operator()(const T& left, const T& right) const{
        return left < right;
    }
};

template<typename T, typename Comparator>
struct Reverse {
    bool operator()(const T& left, const T& right) const{
        Comparator cp;
        return !cp(left, right);
    }
};
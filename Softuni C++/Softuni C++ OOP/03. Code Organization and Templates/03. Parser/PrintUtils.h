#ifndef PRINT_UTILS_H
#define PRINT_UTILS_H

#include <iostream>
#include <vector>


template<typename T>
void printVector(const std::vector<T>&v){
    typename std::vector<T>::const_iterator vcit = v.begin();
    while(vcit != v.end())
        std::cout << *vcit++ << ' ';
    std::cout << std::endl;
}





#endif // !PRINT_UTILS_H
#pragma once

#include <iostream>

template<typename T>
void printContainer(typename T::iterator itBeg, typename T::iterator itEnd){
    while(itBeg != itEnd)
        std::cout << *itBeg++ << ' ';
    std::cout << std::endl;
}
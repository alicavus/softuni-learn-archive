#pragma once

#include <iostream>
#include <sstream>
#include <vector>

template<typename T>
std::vector<T> split(const std::string& line, const char sep){
    std::vector<T> v;
    std::istringstream inpst(line);

    std::string currTok;
    while(getline(inpst, currTok, sep)){
        std::istringstream ist(currTok);
        T currValue;
        ist >> currValue;
        v.push_back(currValue);
    }
    
    return v;
}

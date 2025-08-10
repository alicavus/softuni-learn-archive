#pragma once

#include <iostream>
#include <sstream>
#include <vector>

template<typename T>
std::string join(std::vector<T>& v, const std::string &joinStr){
    std::ostringstream ostr;
    typename std::vector<T>::const_iterator vcit = v.begin();
    bool bFirst = true;
    while(vcit != v.end()){
        if(bFirst)
            bFirst = false;
        else 
            ostr << joinStr;
        ostr << *vcit;
        vcit++;
    }
    return ostr.str();
}

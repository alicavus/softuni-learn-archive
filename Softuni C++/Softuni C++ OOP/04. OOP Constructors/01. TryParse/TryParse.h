#pragma once

#include<sstream>

bool tryParse(std::string& str, int &n){
    std::istringstream istr(str);
    istr >> n;
    return (bool) istr;
}
#ifndef OPERATORS_H
#define OPERATORS_H

#include <ostream>
#include <vector>
#include <string>
#include <sstream>

std::vector<std::string>& operator<<(std::vector<std::string>& v, std::string s) {
    v.push_back(s);
    return v;
}

/*
std::string& operator+(std::string& s, int n){
    std::ostringstream ostr;
    ostr << n << ". ";
    s += ostr.str();
    return s;
}
*/

std::string& operator+(std::string& s, int n){
    std::ostringstream ostr;
    ostr << n;
    s += ostr.str();
    return s;
}

std::ostream& operator<<(std::ostream& ostr, const std::vector<std::string>&v){
    for(const std::string& s : v)
        ostr << s << std::endl;
    
    return ostr;
}

#endif // !OPERATORS_H
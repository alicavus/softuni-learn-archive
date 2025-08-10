#pragma once

#include <istream>
#include <sstream>

template<typename T>
class Parser{
    private:
    std::istream& istr;
    std::string stopLine;

    public:
    Parser(std::istream& istr, const std::string& stopLine)
    : istr(istr), stopLine(stopLine){}

    bool readNext(T& data){
        std::string buf;
        getline(istr, buf);

        if(buf == stopLine)
            return false;
        std::istringstream istr(buf);
        istr >> data;
        return (bool) istr;
    }
};
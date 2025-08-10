#ifndef PARSER_H
#define PARSER_H

#include <istream>
#include <sstream>

template<typename T>
class Parser{
    private:
    std::istream& inpstr;
    std::string stopLine;

    public:
    Parser(std::istream& inpstr, const std::string& stopLine)
    : inpstr(inpstr), stopLine(stopLine){}

    bool readNext(T& data){
        std::string buf;
        getline(inpstr, buf);

        if(buf == stopLine)
            return false;
        std::istringstream istr(buf);
        istr >> data;
        return (bool) istr;
    }

};


#endif // !PARSER_H
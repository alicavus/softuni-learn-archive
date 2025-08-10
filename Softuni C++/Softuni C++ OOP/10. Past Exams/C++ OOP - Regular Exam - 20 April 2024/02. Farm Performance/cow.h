#pragma once

#include "animal.h"

class Cow : public Animal{
    unsigned milkPerDay;

    public:
    Cow(std::istream & istr) : milkPerDay(0) {
        istr >> milkPerDay;
    }

    virtual unsigned getResult(unsigned weeks) const {
        return milkPerDay * 7 * weeks;
    };

    virtual std::string getDescription() const { return "Cow"; }
        
    virtual std::string getInfo() const {
        std::ostringstream ostr;
        ostr << '<' << milkPerDay << ">";

        return ostr.str();
    }
};


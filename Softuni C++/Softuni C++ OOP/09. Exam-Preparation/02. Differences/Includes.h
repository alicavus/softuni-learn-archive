#pragma once

#include <vector>
#include <iostream>
#include <sstream>
#include <iomanip>
#include "City.h"

std::istream& operator>>(std::istream& istr, City& city){
	unsigned int censusYear;
	std::string name;
	size_t population;
    istr >> name >> population >> censusYear;
    city = City(censusYear, name, population);

    return istr;
}

class CityDiff{
    City left;
    City right;

    public:
    CityDiff(City left, City right): left(left), right(right){}


    friend std::ostream& operator<<(std::ostream& ostr, CityDiff cdiff);
};

CityDiff operator-(const City left, const City right){
    return CityDiff(left, right);
}

std::ostream& operator<<(std::ostream& ostr, CityDiff cdiff){
    if(cdiff.left.getName() == cdiff.right.getName())
        ostr << cdiff.left.getName() << " (" << cdiff.left.getCensusYear() << " vs. " << cdiff.right.getCensusYear() << ")" << std::endl;
    else
        ostr << cdiff.left.getName() << " (" << cdiff.left.getCensusYear() << ") vs. " 
        << cdiff.right.getName() << " (" << cdiff.right.getCensusYear() << ")" << std::endl;
    
    ostr << "population: " << std::showpos << static_cast<long long>(cdiff.left.getPopulation()) - static_cast<long long>(cdiff.right.getPopulation()) << std::endl;
    
    return ostr;
}
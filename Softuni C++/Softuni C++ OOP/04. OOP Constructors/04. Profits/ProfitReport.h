#pragma once

#include <sstream>
#include <map>

std::string getProfitReport(
        const Company* fromInclusive,
        const Company* toInclusive,
        const std::map<int, ProfitCalculator> profitCalculatorsByCompany){
    std::ostringstream ostr;
    bool bFirst = true;
    while(fromInclusive <= toInclusive){
        //fromInclusive ->
        if(bFirst)
            bFirst = false;
        else
            ostr << std::endl;
        
        ostr << fromInclusive -> getName() << " = " << profitCalculatorsByCompany.at(fromInclusive -> getId()).calculateProfit(*fromInclusive++);
    }
    return ostr.str();
}
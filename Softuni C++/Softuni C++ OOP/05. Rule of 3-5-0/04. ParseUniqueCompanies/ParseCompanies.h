#ifndef PARSE_COMPANIES_H
#define PARSE_COMPANIES_H

#include "Company.h"
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <utility>
#include <memory>
#include <list>

Company* parseUniqueCompanies(std::string inpStr, int& numCompanies, std::string (*func)(const Company& c)){
    std::istringstream inpstr(inpStr);
    int companyId;
    std::string companyName, companyUniqId;
    std::vector<std::pair<std::string, Company>>companiesVect;
    while(inpstr >> companyId >> companyName){
        Company c = Company(companyId, companyName);
        companyUniqId = func(c);
        if(find_if(companiesVect.begin(), companiesVect.end(), [companyUniqId](const std::pair<std::string, Company>& p){
            return p . first ==  companyUniqId;
        }) == companiesVect.end())
            companiesVect.push_back({companyUniqId, std::move(c)});
    }
    numCompanies = companiesVect.size();
    Company* allocator = new Company[numCompanies];
    int currIdx = 0;
    std::vector<std::pair<std::string, Company>>::iterator it = companiesVect.begin();
    for(;it != companiesVect.end(); ++it, ++currIdx){
        allocator[currIdx] = it->second;
    }

    return allocator;
}

#endif // !PARSE_COMPANIES_H
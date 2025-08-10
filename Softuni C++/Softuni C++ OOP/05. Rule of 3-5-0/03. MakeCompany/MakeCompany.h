#ifndef MAKE_COMPANY_H
#define MAKE_COMPANY_H

#include "Company.h"
#include <vector>
#include <memory>
#include <utility>

std::shared_ptr<Company> makeCompany(std::vector<std::string> properties){
    std::vector<std::pair<char, char> > employees;
    std::string companyId, companyName;
    if(properties.size() >= 2){
        companyId = properties[0];
        companyName = properties[1];
    }

    for(size_t idx = 2; idx < properties.size(); ++idx){
        std::string emploee = properties[idx];
        if(emploee.size() == 2)
            employees.push_back({emploee[0], emploee[1]});
    }

    std::shared_ptr<Company> c = std::make_shared<Company>(std::stoi(companyId), companyName, std::move(employees));
    return c;
}

#endif // !MAKE_COMPANY_H
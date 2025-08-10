#include "Company.h"
#include "Register.h"

Register::Register(size_t numCompanies)
: numAdded(0), companiesArray(new Company[numCompanies]){}

Register::~Register(){
    delete[] companiesArray;
}

void Register::add(const Company& c){
    companiesArray[numAdded++] = c;
}

Company Register::get(int companyId) const{
    for(int companyIdx = 0; companyIdx < numAdded; ++companyIdx){
        if(companyId == companiesArray[companyIdx].getId())
            return companiesArray[companyIdx];
    }
    return Company();
}


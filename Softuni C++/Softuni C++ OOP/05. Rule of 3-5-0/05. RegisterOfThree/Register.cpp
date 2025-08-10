#include "Register.h"
#include <algorithm> 



Register::Register(size_t numCompanies){
    numAdded = 0;
    companiesArray = new Company[numCompanies]{};
}

Register::~Register(){
    delete[] companiesArray;
}

Register& Register::operator=(const Register& other){
    if(this != &other){
        delete[] companiesArray;
        companiesArray = new Company[other.numAdded];
        std::copy(other.companiesArray, other.companiesArray+other.numAdded, companiesArray);
        numAdded = other.numAdded;
    }
    
    return *this;
}

Register::Register(const Register& other){
    numAdded = 0;
    delete[] companiesArray;
    companiesArray = new Company[other.numAdded];
    std::copy(other.companiesArray, other.companiesArray+other.numAdded, companiesArray);
    numAdded = other.numAdded;
}


void Register::add(const Company& c){
    companiesArray[numAdded++] = c;
}

Company Register::get(int companyId) const{
    for(size_t idx = 0; idx < numAdded; ++idx)
        if(companiesArray[idx].getId() == companyId)
            return companiesArray[idx];
    return Company();
}
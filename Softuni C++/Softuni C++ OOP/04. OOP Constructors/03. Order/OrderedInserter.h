#pragma once

#include <vector>
#include <algorithm>
#include "Company.h"

class cmp{
    public:
    bool operator()( const Company*& lhs, const Company*& rhs ) const{
        return lhs->getId() < rhs -> getId();
    }
};

class OrderedInserter{
    std::vector<const Company*>* companiesPtr;

    void sort(){
        std::sort(this->companiesPtr->begin(), this->companiesPtr->end(), cmp());
    }

    public:
    OrderedInserter(std::vector<const Company*>& companies){
        this->companiesPtr = &companies;
    }

    void insert(const Company*&& c){
        this->companiesPtr -> push_back(c);
        this->sort();
    }
};
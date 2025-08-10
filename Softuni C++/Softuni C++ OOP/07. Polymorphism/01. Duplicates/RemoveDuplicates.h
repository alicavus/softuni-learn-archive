#pragma once

#include "Company.h"
#include <iostream>
#include <string>
#include <sstream>
#include <list>
#include <set>
#include <algorithm>

void removeDuplicates(std::list<Company*>& companies){
    std::set<Company*>uniqueCompanies;
    for(std::list<Company*>::iterator lit = companies.begin(); lit != companies.end();){
        Company* curr = *lit;
        auto it = std::find_if(uniqueCompanies.begin(), uniqueCompanies.end(), [curr](Company* c){
            return (curr->getName() == c->getName());
        });
        if(it != uniqueCompanies.end())
            lit = companies.erase(lit);
        else
            uniqueCompanies.insert(*lit++);
    }
}
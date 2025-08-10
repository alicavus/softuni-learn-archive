#ifndef REMOVE_INVALID_H
#define REMOVE_INVALID_H

#include "Company.h"
#include <vector>
#include <list>

void removeInvalid(std::list<Company*>& companies){
    companies.remove_if([](Company*& c){
        if(c->getId() < 0){
            delete c;
            c = nullptr;
            return true;
        }
        return false;
    });
}

#endif // !REMOVE_INVALID_H
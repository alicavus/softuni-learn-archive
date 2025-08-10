#ifndef FIND_H
#define FIND_H

#include "Company.h"
#include <vector>
#include <algorithm>

Company* find(const std::vector<Company*>& v, int id){
    std::vector<Company*>::const_iterator cit = v.begin();
    while(cit != v.end()){
        if((*cit)->getId() == id)
            return *cit;
        cit++;
    }
    return nullptr;
}

#endif // !FIND_H
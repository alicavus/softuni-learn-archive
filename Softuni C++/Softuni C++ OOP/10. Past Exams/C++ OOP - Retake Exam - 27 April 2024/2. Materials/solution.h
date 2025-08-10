#pragma once

#include "storage.h"
#include <sstream>

std::ostream& operator<<(std::ostream& ostr, Storage& s){
    ostr << "Storage: ";
    bool bFirst = true;
    auto it = s.begin();
    if(it == s.end())
        ostr << "Empty";
    for(;it != s.end(); ++it){
        if(bFirst)
            bFirst = false;
        else
            ostr << ", ";
        ostr << it->first << ": " << it->second;
    }
    return ostr;
}

bool Storage::operator<= (Store & contents){
    for(const std::pair<std::string, unsigned>&p : contents){
        if(!storage.count(p.first))
            return false;
        if(storage.at(p.first) < p.second)
            return false;
    }

    return true;
}

Storage& Storage::operator>>(Store & contents){
    for(auto it = contents.begin(); it != contents.end(); ++it){
        storage[it->first] -= it->second;
        if(storage[it->first] == 0)
            storage.erase(it->first);
    }
    return *this;
}
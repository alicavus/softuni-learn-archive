#include "Supplemental.h"
#include <algorithm>

std::string Supply::getInfo() const{
    std::ostringstream ostr;
    ostr << getName() << ":" << getQuantity();
    return ostr.str();
}

bool Supplements::insert(Supplement * sup){
    auto res = data.insert({sup->getName(), std::unique_ptr<Supplement>(sup)});
    return res.second;
}

Supplement* Supplements::get(const std::string & name){
    auto it = data.find(name);
    if(it != data.end())
        return it->second.get();
    return nullptr;
}

std::string Supplements::getInfo() const{
    std::ostringstream ostr;
    ostr << "[";
    if(!data.size())
        return "[empty]";
    
    bool bFirst = true;
    for(const auto& s : data){
        if(bFirst)
            bFirst = false;
        else
            ostr << ", ";
        ostr << s.second->getInfo();
    }
    ostr << "]";
    return ostr.str();
}
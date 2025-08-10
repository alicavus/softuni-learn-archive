#include "Command.h"
#include <sstream>

std::string Command::abortMessage(const std::string & invalidId) const{
    std::ostringstream ostr;
    ostr << "Aborting on " << getName() << " due to invalid ID \"" << invalidId << "\". "; 
    ostr << "Lost pieces ";
    
    unsigned totalMaterial(0), totalTime(0);

    for(const auto& m : proc.storage){
        ostr << m.first << ", ";
        totalMaterial += m.second.mat;
        totalTime += m.second.time;
    }
    
    ostr << "lost material " << totalMaterial << ", wasted time " << totalTime << ".";

    proc.setErrorId(invalidId);

    return ostr.str();
}

std::string Command::successMessage() const{
    std::ostringstream ostr;
    if(proc.storage.empty())
        return "";
    
    unsigned totalMaterial(0), totalTime(0);
    
    ostr << "Packing and shipping new order: \"";

    bool bFirst = true;
    for(const auto& piece : proc.storage){
        if(bFirst)
            bFirst = false;
        else
            ostr << ", ";
        ostr << piece.first;
        totalMaterial += piece.second.mat;
        totalTime += piece.second.time;
    }
    
    ostr << "\". Production material: " << totalMaterial;
    ostr << ", production time: " << totalTime << ".";
    
    proc.setSuccess(ostr.str());

    return ostr.str();
}
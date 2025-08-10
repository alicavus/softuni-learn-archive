#include "Noise.h"
#include <sstream>

void Noise::newNoise(size_t time){
    number++;
    last = time;
    each = (last - first) / number;
}

std::string Noise::getNewNoiseStatistics(void) const{
    std::ostringstream ostr;
    ostr << number;
    if(number > 1){
        ostr << ", each ";
        if(each > 1){
            ostr << each << " minutes";
        }
        else ostr << "minute";
    }
    return ostr.str();
}

std::string Noise::getFinalStatistics(void) const{
    std::ostringstream ostr;
    ostr << number;
    if(number > 1){
        ostr << ", from " << first << " till " << last << ", each ";
        if(each > 1)
            ostr << each << " minutes";
        else
            ostr << "minute";
    }
    else
        ostr << " at " << first;
    
    return ostr.str();
}
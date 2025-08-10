#include "Noises.h"
#include <sstream>

std::string Noises::registerNoise(const std::string & time_, const std::string & noise_){
    std::ostringstream ostr;
    size_t time = stringToTime(time_);
    
    if(noises.count(noise_))
        noises[noise_].newNoise(time);
    else
        noises[noise_] = Noise(time);
    
    ostr << noise_ << ": " << noises[noise_].getNewNoiseStatistics();
    return ostr.str();
}

void Noises::printStatistics(std::ostream & ostr) const{
    ostr << "----" << std::endl;
    if(! noises.size()){
        ostr << "No noises." << std::endl;
    }
    for(const auto& pair : noises)
        ostr << pair.first << ": " << pair.second.getFinalStatistics() << std::endl;
}
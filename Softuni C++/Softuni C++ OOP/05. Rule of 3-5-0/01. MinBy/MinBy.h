#ifndef MIN_BY_H
#define MIN_BY_H

#include <vector>
#include <string>

std::string minBy(const std::vector<std::string>& values,
                bool (*compare)(const std::string& a,
                const std::string& b)){
    std::string minValue = "";
    for(const std::string& value : values){
        if(!minValue.size())
            minValue = value;
        else if((*compare)(value, minValue))
            minValue = value;

    }
    return minValue;
}

#endif //  MIN_BY_H
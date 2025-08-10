#pragma once

#include "City.h"
#include <vector>
#include <map>

const City* initCity(std::string name, size_t population){
    const City* city = new City(name, population);
    return city;
}

std::map<size_t, const City*> groupByPopulation(std::vector<const City*>& cities, size_t& totalPopulation){
    std::map<size_t, const City*> res;
    totalPopulation = 0;
    for(const City* c : cities){
        size_t currPopulation = c->getPopulation();
        res[currPopulation] = c;
        totalPopulation += currPopulation;
    }
    return res;
}




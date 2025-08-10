#pragma once

#include <iostream>
#include <sstream>
#include <list>
#include <memory>

struct Tree{
    static size_t cnt;
    virtual const std::string getName() const = 0;
    virtual const std::string getLeaves() const = 0;
    virtual const std::string getProduction() const = 0;
    virtual const std::string getGreatness() const = 0;

    virtual ~Tree() = default;

    void outputTree(std::ostream& ostr){
        ostr << ++cnt << ". " << getName() << " tree with ";
        ostr << getLeaves() << " leaves, which produces " << getProduction();
        ostr << " and is great for " << getGreatness() << "." << std::endl;
    }
};
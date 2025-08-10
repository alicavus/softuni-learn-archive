#pragma once
#include <iostream>
#include <sstream>
#include <list>
#include <memory>

class Tree{

    public:
    static size_t cnt;

    virtual const std::string getName() const = 0;
    virtual const std::string getLeaves() const = 0;
    virtual const std::string getProduction() const = 0;
    virtual const std::string getGreatness() const = 0;

    void outputTree(std::ostream& ostr){
        ostr << ++Tree::cnt << ". " << getName() << 
        " tree with " << getLeaves() << 
        " leaves, which produces " << getProduction() << 
        " and is great for " << getGreatness() << "." << std::endl;
    }

};
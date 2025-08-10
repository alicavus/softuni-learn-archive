#ifndef FILTER_FACTORY_H
#define FILTER_FACTORY_H

#include "Filter.h"

class RemoveRangeOfLetters : public Filter{
    char _start;
    char _end;
    protected:
    virtual bool shouldFilterOut(char symbol) const{
        return symbol >= _start && symbol <= _end;
    }

    public:
    RemoveRangeOfLetters() : _start('a'), _end('z'){}
    RemoveRangeOfLetters(const std::string& filterDefinition) : _start('a'), _end('z'){
        if(filterDefinition.size() == 3 && filterDefinition[1] == '-'){
            _start = std::min(filterDefinition[0], filterDefinition[2]);
            _end = std::max(filterDefinition[0], filterDefinition[2]);
        }
    }
};

class RemoveUppercaseLetters : public Filter{
    protected:
    virtual bool shouldFilterOut(char symbol) const{
        return symbol >= 'A' and symbol <= 'Z';
    }
};

class RemoveLowercaseLetters : public Filter{
    protected:
    virtual bool shouldFilterOut(char symbol) const{
        return symbol >= 'a' and symbol <= 'z';
    }
};

class RemoveDigits : public Filter{
    protected:
    virtual bool shouldFilterOut(char symbol) const{
        return symbol >= '0' and symbol <= '9';
    }
};

class FilterFactory{
    public:
    Filter* buildFilter(std::string& filterDefinition) const{
        return new RemoveRangeOfLetters(filterDefinition);
        //return nullptr;
    }

};

#endif // !FILTER_FACTORY_H
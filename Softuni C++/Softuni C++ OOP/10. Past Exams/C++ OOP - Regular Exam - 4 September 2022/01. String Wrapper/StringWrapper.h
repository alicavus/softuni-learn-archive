#pragma once

#include <iostream>
#include "InputParser.h"

class StringWrapper{
    Input _data;
    public:
    StringWrapper() : _data(){}
    StringWrapper(Input i) : _data(i){}
    StringWrapper(const std::string& line): _data(){
        _data.line = line;
    }
    StringWrapper(char letter, int rep): _data(){
        _data.letter = letter;
        _data.repetitions = rep;
    }

    StringWrapper getContent() const{
        return StringWrapper(_data);
    }

    StringWrapper& append(const StringWrapper& other){
        if(other._data.line.size())
            _data.line.append(other._data.line);
        if(other._data.letter != '\0')
            _data.letter = other._data.letter;
        if(other._data.repetitions !=  0)
            _data.repetitions = other._data.repetitions;
        return *this;
    }

    void printContent(){
        std::string res = _data.line;
        int rep = _data.repetitions;
        while(rep-- > 0)
            res.push_back(_data.letter);
        std::cout << res << std::endl;
    }
};

Input readInput(void){
    Input i;
    std::cin >> i.line >> i.letter >> i.repetitions;
    return i;
}
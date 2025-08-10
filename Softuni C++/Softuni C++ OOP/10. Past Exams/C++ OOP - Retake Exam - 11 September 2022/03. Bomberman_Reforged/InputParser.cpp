#include <iostream>
#include <sstream>
#include <algorithm>
#include "InputParser.h"

FieldData InputParser::readField() const{
    FieldData fd;
    size_t cntRows, cntCols;
    std::cin >> cntRows >> cntCols;
    fd.reserve(cntRows);
    fd.resize(cntRows);
    for(size_t rIdx = 0; rIdx < cntRows; ++rIdx){
        getline(std::cin >> std::ws, fd[rIdx]);
    }
    return fd;
}

std::vector<Command> InputParser::readCommands() const{
    std::vector<Command> commands;
    size_t cntCommands;
    std::cin >> std::ws >> cntCommands;
    
    while(cntCommands--){
        Command c;
        std::string inputLine, currCmd;
        std::getline(std::cin >> std::ws, inputLine);
        std::transform(inputLine.begin(), inputLine.end(), inputLine.begin(), ::tolower);
        std::istringstream istr(inputLine);
        istr >> currCmd;
        if(currCmd == "power"){
            istr >> currCmd;
            if(currCmd == "up")
                c.type = CommandType::POWER_UP;
            else if(currCmd == "down")
                c.type = CommandType::POWER_DOWN;
            else
                c.type = CommandType::UNKNOWN;
        }
        else if(currCmd == "bomb"){
            c.type = CommandType::PLACE_BOMB;
            istr >> c.bombRow >> c.bombCol >> std::ws;
        }
        else
            c.type = CommandType::UNKNOWN;
    commands.push_back(c);
    }
    return commands;
}
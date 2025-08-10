#include <iostream>
#include <string>
#include <unordered_map>
#include "NoteName.h"
#include "SolfegeNoteNaming.h"

NoteName SolfegeNoteNaming::operator()(const std::string& name) const{
    std::unordered_map<std::string, char>noteMap = {
        {"La", 'A'}, {"Si", 'B'}, {"Do", 'C'}, {"Re", 'D'}, {"Mi", 'E'}, {"Fa", 'F'}, {"Sol", 'G'}};
    char englishName = (noteMap.find(name) != noteMap.end())? noteMap.at(name) : '?';
    return NoteName(englishName);
}
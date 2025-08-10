#pragma once

#include <iostream>
#include <string>
#include "NoteName.h"

class SolfegeNoteNaming{
    public:
    NoteName operator()(const std::string& name) const;
};
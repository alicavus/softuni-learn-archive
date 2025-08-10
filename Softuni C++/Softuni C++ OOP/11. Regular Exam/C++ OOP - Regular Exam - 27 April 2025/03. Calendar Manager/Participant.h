#pragma once

#include <iostream>
#include <string>

struct Participant{
    virtual std::string getId() const = 0;
    virtual std::string toString() const = 0;
    virtual void readFrom(std::istream & is) = 0;

    virtual ~Participant() = default;
};
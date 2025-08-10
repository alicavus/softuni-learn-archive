#ifndef _PARTICIPANT_H_
#define _PARTICIPANT_H_

#include <iostream>
#include <sstream>
#include <set>

struct Participant{
    virtual std::string getId() const = 0;
    virtual std::string toString() const = 0;
    virtual void readFrom(std::istream & is) = 0;

    virtual ~Participant() = default;
};

#endif //!  _PARTICIPANT_H_
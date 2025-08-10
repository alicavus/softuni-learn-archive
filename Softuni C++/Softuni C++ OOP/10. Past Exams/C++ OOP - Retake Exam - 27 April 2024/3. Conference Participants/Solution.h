#ifndef Solution_H
#define Solution_H

#include "Participant.h"
#include <iostream>
#include <sstream>

std::ostream& operator<<(std::ostream& ostr, const Participant* part){
    ostr << part->print();
    return ostr;
}

std::ostream& operator<<(std::ostream& ostr, const Participant::Vector& vect){
    if(vect.empty())
        ostr << "- none" << std::endl;
    
    for(std::vector<Participant *>::const_iterator it = vect.begin(); it != vect.end(); ++it)
        ostr << "- " << *it << std::endl;

    return ostr;
}


#endif // ! Solution_H
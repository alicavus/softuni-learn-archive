#ifndef Sponsor_H
#define Sponsor_H

#include <sstream>

class Sponsor : public Participant{
    protected:
        std::string company;

    public:
        static Participant::Vector all;

        Sponsor(std::istream& istr) : Participant(istr){
            istr >> company;
            all.push_back(this);
        }
};


#endif // ! Sponsor_H
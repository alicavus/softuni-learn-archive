#ifndef SilverEmployee_H
#define SilverEmployee_H

#include "Sponsor.h"

class SilverEmployee : public Sponsor {

    public:
        SilverEmployee(std::istream & istr) : Sponsor(istr) {
            istr >> accountId;
        }

        virtual Type getType() const override { return Type(Participant::Type::SilverEmployee); }

        virtual std::string print() const override {
            std::ostringstream ostr;

            ostr << "Silver: " << Participant::print() << " | " << company << " | " << accountId;

            return ostr.str();
        }

    protected:

        std::string accountId;

};





#endif // ! SilverEmployee_H
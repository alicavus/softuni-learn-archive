#ifndef __YACHT__H__
#define __YACHT__H__

#include "Info.h"
#include "Named.h"
#include "Dockable.h"
#include "Supplemental.h"
#include <sstream>

class Yacht: public Info, public Named, public Dockable{
    std::string name;
    Supplements passengers;
    Supplements supplies;

    public:
    Yacht(std::string& name): name(name){}
    virtual ~Yacht() = default;

    virtual std::string getName() const override{
        return name;
    }

    virtual std::string getInfo() const override{
        std::ostringstream ostr;
        ostr << "passengers [" << passengers.getInfo();
        ostr << "] and supplies [" << supplies.getInfo() << "]";
        return ostr.str();
    }
    
    virtual std::string dock() const override{
        std::ostringstream ostr;
        ostr << "Yacht " << getName() << " successfully docked.";
        return ostr.str();
    }
    virtual std::string undock() const override; //inplemented!
    virtual bool onSupplementArrival(Supplement *s) override; //inplemented!

};

#endif
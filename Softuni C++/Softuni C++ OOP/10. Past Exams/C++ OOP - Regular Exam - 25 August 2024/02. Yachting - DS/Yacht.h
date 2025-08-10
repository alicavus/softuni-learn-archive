#ifndef YACHT_H
#define YACHT_H

#include "Dockable.h"
#include "Info.h"
#include "Named.h"
#include "Supplemental.h"

class Yacht : public Dockable, public Info, public Named {
private:
    std::string name;
    Supplements passengers;
    Supplements supplies;

public:
    Yacht(const std::string& name);
    virtual ~Yacht() = default;

    std::string dock() const override;
    std::string undock() const override;
    bool onSupplementArrival(Supplement* s) override;
    std::string getName() const override;
    std::string getInfo() const override;
};

#endif
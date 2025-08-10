#include "Yacht.h"
#include <sstream>

Yacht::Yacht(const std::string& name) : name(name) {}

std::string Yacht::dock() const {
    return "Yacht " + name + " successfully docked.";
}

std::string Yacht::getName() const {
    return name;
}

std::string Yacht::getInfo() const {
    return "passengers " + passengers.getInfo() + " and supplies " + supplies.getInfo();
}
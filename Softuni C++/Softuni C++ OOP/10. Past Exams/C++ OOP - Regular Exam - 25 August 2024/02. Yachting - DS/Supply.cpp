#include "Supplemental.h"

std::string Supply::getInfo() const {
    return getName() + ":" + std::to_string(getQuantity());
}
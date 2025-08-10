#include "Supplemental.h"
#include <vector>
#include <algorithm>

bool Supplements::insert(Supplement* sup) {
    std::string name = sup->getName();
    if (data.find(name) != data.end()) return false;
    data[name].reset(sup);
    return true;
}

Supplement* Supplements::get(const std::string& name) {
    auto it = data.find(name);
    return (it != data.end()) ? it->second.get() : nullptr;
}

std::string Supplements::getInfo() const {
    std::vector<std::string> passengers, supplies;
    for (const auto& entry : data) {
        Supplement* sup = entry.second.get();
        if (dynamic_cast<Passenger*>(sup)) {
            passengers.push_back(sup->getName());
        } else if (Supply* s = dynamic_cast<Supply*>(sup)) {
            supplies.push_back(s->getInfo());
        }
    }
    std::sort(passengers.begin(), passengers.end());
    std::sort(supplies.begin(), supplies.end());
    
    std::ostringstream oss;
    oss << "[";
    if (!passengers.empty()) {
        for (size_t i = 0; i < passengers.size(); ++i) {
            if (i > 0) oss << ", ";
            oss << passengers[i];
        }
    } else oss << "empty";
    oss << "] and supplies [";
    if (!supplies.empty()) {
        for (size_t i = 0; i < supplies.size(); ++i) {
            if (i > 0) oss << ", ";
            oss << supplies[i];
        }
    } else oss << "empty";
    oss << "]";
    return oss.str();
}
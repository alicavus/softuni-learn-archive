#ifndef SOLUTION_H
#define SOLUTION_H

#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <cmath>
#include <limits>
#include <algorithm>

#include "classes.h"


std::vector<Match> match(std::vector<Dog>& dogs, std::vector<Employee>& employees) {
    std::vector<Match> matches;
    std::vector<bool> dogUsed(dogs.size(), false);
    std::vector<bool> employeeUsed(employees.size(), false);

    for (size_t i = 0; i < employees.size(); ++i) {
        int bestDiff = std::numeric_limits<int>::max();
        int bestIndex = -1;

        for (size_t j = 0; j < dogs.size(); ++j) {
            if (dogUsed[j]) continue;

            int diff = employees[i].getStrength() - dogs[j].getPower();
            if (diff < 0) continue;

            if (diff < bestDiff) {
                bestDiff = diff;
                bestIndex = j;
            }
        }

        if (bestIndex != -1) {
            matches.emplace_back(dogs[bestIndex], employees[i]);
            dogUsed[bestIndex] = true;
            employeeUsed[i] = true;
        }
    }

    // Remove matched dogs and employees
    auto dogIt = dogs.begin();
    for (int i = 0; i < dogUsed.size();) {
        if (dogUsed[i]) {
            dogIt = dogs.erase(dogIt);
            dogUsed.erase(dogUsed.begin() + i);
        } else {
            ++i;
            ++dogIt;
        }
    }

    auto empIt = employees.begin();
    for (int i = 0; i < employeeUsed.size();) {
        if (employeeUsed[i]) {
            empIt = employees.erase(empIt);
            employeeUsed.erase(employeeUsed.begin() + i);
        } else {
            ++i;
            ++empIt;
        }
    }

    return matches;
}

template <typename T>
void print(std::ostream& out, const T& container, const std::string& title) {
    out << title << "\n";

    if (container.empty()) {
        out << "none.\n";
        return;
    }

    for (const auto& item : container) {
        out << "- " << item.getInfo() << "\n";
    }
}

#endif

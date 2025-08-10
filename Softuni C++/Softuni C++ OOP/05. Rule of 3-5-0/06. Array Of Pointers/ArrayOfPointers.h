#ifndef ARRAY_OF_POINTERS_H
#define ARRAY_OF_POINTERS_H

#include "Company.h"
#include <vector>
#include <memory>

class ArrayOfPointers {
    std::vector<Company*> _data;

    void clear() {
        for (Company* c : _data) {
            delete c;
        }
        _data.clear();
    }

public:
    ArrayOfPointers() = default;

    ~ArrayOfPointers() {
        clear();
    }

    ArrayOfPointers(const ArrayOfPointers& other) {
        if (this != &other) {
            clear();
            for (const Company* c : other._data) {
                _data.push_back(new Company(*c));
            }
        }
    }

    ArrayOfPointers& operator=(const ArrayOfPointers& other) {
        if (this != &other) {
            clear();
            for (const Company* c : other._data) {
                _data.push_back(new Company(*c));
            }
        }
        return *this;
    }

    void add(Company* c) {
        _data.push_back(c);
    }

    Company* get(size_t idx) {
        if (idx >= _data.size()) {
            return nullptr;
        }
        return _data[idx];
    }

    size_t getSize() const {
        return _data.size();
    }
};

#endif  // ARRAY_OF_POINTERS_H
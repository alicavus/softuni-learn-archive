#include "IndexedSet.h"

#include <set>

void IndexedSet::clearIndex(){
    if (valuesArray){
        delete[] valuesArray;
        valuesArray = nullptr;
    }
}

void IndexedSet::buildIndex(){
    clearIndex();
    valuesArray = new Value[valuesSet.size()];
    size_t idx = 0;
    for (const Value& v : valuesSet)
        valuesArray[idx++] = v;
}

IndexedSet::IndexedSet() : valuesSet(), valuesArray(nullptr){}

IndexedSet::IndexedSet(const IndexedSet& other) : valuesSet(other.valuesSet), valuesArray(nullptr) {}

IndexedSet::~IndexedSet(){
    clearIndex();
    valuesSet.clear();
}

void IndexedSet::add(const Value& v){
    if(valuesSet.insert(v).second)
        clearIndex();
}

size_t IndexedSet::size() const{
    return valuesSet.size();
}

const Value& IndexedSet::operator[](size_t index){
    if (valuesArray == nullptr)
        buildIndex();
    
    return valuesArray[index];
}

IndexedSet& IndexedSet::operator=(const IndexedSet& other){
    if(this != &other){
        clearIndex();
        valuesSet = other.valuesSet;
    }
    return *this;
}


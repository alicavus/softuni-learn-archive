#include "Range.h"
#include "algorithm"

//Constructors
Range::Range(): rangeFirst(0), rangeLength(0), valueCounts(nullptr){}

//Copy constructor
Range::Range(const Range& other): Range(){
    *this = other;
}

//Copy assignement constructor
Range& Range::operator=(const Range& other){
    if(this != &other){
        clear();
        rangeFirst = other.rangeFirst;
        rangeLength = other.rangeLength;
        valueCounts = copyValues(other);
    }
    return *this;
}

Range::~Range(){
    clear();
}

void Range::clear(){
    if(!empty()){
        delete[] valueCounts;
        valueCounts = nullptr;
        rangeFirst = rangeLength = 0;
    }
}

bool Range::empty() const{
    return valueCounts == nullptr;
}


void Range::add(T value){
    T first = rangeFirst;
    T last = rangeFirst + rangeLength - 1;

    if(empty())
        resize(value, value);
    
    else if(value < rangeFirst)
        resize(value, last);
    
    else if(value > last)
        resize(first, value);
    
    valueCounts[getIndex(value)]++;    
}

void Range::resize(T first, T last){
    T newRangeFirst = first;
    T newRangeLength = last - first + 1;
    size_t* newValueCounts = new size_t[newRangeLength]{0};

    if(!empty()){
       std::copy(valueCounts, valueCounts+rangeLength, newValueCounts + (rangeFirst - first));
       clear();
    }

    rangeFirst = first;
    rangeLength = newRangeLength;
    valueCounts = newValueCounts;    
}

size_t Range::getCount(T value) const{
    if(value >= rangeFirst and value < rangeFirst + rangeLength)
        return valueCounts[getIndex(value)];
    return 0;
}

size_t Range::getIndex(T value) const{
    return value - rangeFirst;
}
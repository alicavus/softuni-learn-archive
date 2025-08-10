#pragma once

#include "Vector.h"


class VectorLengthComparer{
    public:
    bool operator()(const Vector& val1, const Vector& val2) const{
        return val1.getLength() < val2.getLength();
    }
};

template<typename T1, typename T2>
class ReverseComparer{
    public:
    bool operator()(const T1& val1, const T1& val2) const{
        return T2()(val2, val1);
    }
};
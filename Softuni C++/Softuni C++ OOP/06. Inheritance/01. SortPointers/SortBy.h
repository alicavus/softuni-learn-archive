#pragma once

#include "Company.h"
#include <iostream>

void sortBy(Company** begin, Company** end, bool(*comp)(const Company& a, const Company& b)){
    for(Company** iIdx = begin; iIdx < end; ++iIdx)
        for(Company** jIdx = begin; jIdx < end; ++jIdx)
            if(comp(**iIdx, **jIdx))
                std::swap(**iIdx, **jIdx);
}


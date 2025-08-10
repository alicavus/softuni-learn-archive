#pragma once

#include "Aggregator.h"
#include <climits>

class  MinAggregator : public StreamAggregator{
    int aggrMin;
    protected:
    virtual void aggregate(int next) {
        aggrMin = std::min(aggrMin, next);
        aggregationResult = aggrMin;
	}
    public:
    MinAggregator(std::istream& stream) : StreamAggregator(stream), aggrMin(INT_MAX){}

};
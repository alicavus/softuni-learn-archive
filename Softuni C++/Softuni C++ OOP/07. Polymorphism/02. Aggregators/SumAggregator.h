#pragma once

#include "Aggregator.h"

class SumAggregator : public StreamAggregator{
    protected:
    virtual void aggregate(int next) {
        aggregationResult += next;
	}
    public:
    SumAggregator(std::istream& stream) : StreamAggregator(stream){}

};
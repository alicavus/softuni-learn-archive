#pragma once

#include "Aggregator.h"

class AverageAggregator : public StreamAggregator{
    int aggregationSum;
    size_t aggregationCnt;
    protected:
    virtual void aggregate(int next) {
        aggregationSum += next;
        aggregationCnt++;
        aggregationResult = aggregationCnt? aggregationSum / aggregationCnt : 0;
	}
    public:
    AverageAggregator(std::istream& stream) : StreamAggregator(stream), aggregationSum(0), aggregationCnt(0){}

};
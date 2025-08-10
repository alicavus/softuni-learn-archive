#include <iostream>
#include <sstream>
#include <vector>
#include <deque>
#include <set>
#include <unordered_map>
#include <algorithm>

void readRanges(std::istream &inp, std::vector<std::pair<int, int>>&ranges, char endChar){
    int from, to;
    for(; inp >> from >> to;){
        ranges.push_back(std::pair<int, int>(from, to));
        char c;
        if(inp.peek() == endChar)
            inp >> c;
    }
}

bool isInRange(const std::vector<std::pair<int, int>>&ranges, int number){
    bool isFound = false;
    for(int left=0, right = ranges.size()-1; left <= right){
        if(number >= )
    }
}

int main(){
    std::vector<std::pair<int, int>>ranges;
    readRanges(std::cin, ranges, '.');
    sort(ranges.begin(), ranges.end());


    return 0;
}
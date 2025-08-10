#include <iostream>
#include <sstream>
#include <vector>
#include <unordered_set>
#include <unordered_map>

int main(){
    std::vector<std::vector<int>>messageParts;
    std::unordered_set<int>separators;
    std::string inputBuff;

    {
        std::string sepBuff;
        getline(std::cin, sepBuff);
        std::istringstream inpstr(sepBuff);
        for(int currSep; inpstr >> currSep;)
            separators.insert(currSep);
    }
    
    std::string msgBuff;
    getline(std::cin, msgBuff);

    std::istringstream instr(msgBuff);
    std::vector<int>currPart;
    for(int currNum; instr >> currNum;){
        if(separators.count(currNum)){
            if(! currPart.empty())
                messageParts.push_back(move(currPart));
        }
        else currPart.push_back(currNum);
    }
    if(! currPart.empty())
        messageParts.push_back(move(currPart));
    
    
    std::unordered_map<int, int>occurences;
    for(const std::vector<int>&currPart : messageParts){
        std::unordered_set<int>uniqueNumbers;
        for(const int &currNum : currPart)
            uniqueNumbers.insert(currNum);
        
        for(const int &currNum : uniqueNumbers)
            occurences[currNum]++;
    }

    for(int searchNum; std::cin >> searchNum;){
        if(searchNum == 0)
            break;
        std::cout << occurences[searchNum] << std::endl;
    }
        
    
    
    return 0;
}
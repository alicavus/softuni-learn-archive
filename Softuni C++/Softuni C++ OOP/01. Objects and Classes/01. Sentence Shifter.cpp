#include <iostream>
#include <sstream>
#include <string>
#include <vector>

typedef std::vector<std::string> wordsType;

class Shifter{
    wordsType words;


    public:
    Shifter(std::istream &istr){
        std::string inputData;
        getline(istr, inputData);
        std::string currStr;
        std::istringstream inpstr(inputData);
        for(;inpstr >> currStr;)
            this -> words.push_back(currStr);
    }

    void getShiftedSentence(std::istream &istr, std::ostream &ostr){
        size_t cntShift;
        istr >> cntShift;
        size_t wordsSize = this -> words.size();
        for(size_t idx = wordsSize - cntShift; idx < wordsSize; ++idx)
            ostr << this->words.at(idx) << std::endl;
        for(size_t idx = 0; idx < wordsSize - cntShift; ++idx)
            ostr << this->words.at(idx) << std::endl;
    }
};

int main(){
    Shifter sh(std::cin);
    sh.getShiftedSentence(std::cin, std::cout);
    return 0;
}
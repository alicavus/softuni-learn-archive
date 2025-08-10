#ifndef ExtractorInitialization_h
#define ExtractorInitialization_h

#include "Extractor.h"
#include <sstream>
#include <memory>

class DigitsExtractor : public Extractor{
    public:
    DigitsExtractor(std::istringstream& lineIn): Extractor(lineIn){}

    protected:
    virtual bool process(char symbol, std::string& output){
        if(symbol >= '0' and symbol <= '9'){
            output = std::string(1, symbol);
            return true;
        }
        return false;
    }
};

class QuoteExtractor: public Extractor{
    std::string result;
    bool isExtracting;

    public:
    QuoteExtractor(std::istream & istr) : Extractor(istr), isExtracting(false) {};

    protected:
    virtual bool process(char symbol, std::string & output){
        if(isExtracting) {
            if (symbol=='"'){
                output=result;
                result.erase();
                isExtracting = false;
                return true;
            }
            else
                result += symbol;
        }
        else if (symbol=='"')
            isExtracting = true;
        
        return false;
    }

};

class NumbersExtractor : public Extractor{
    std::string result;

    public:
    NumbersExtractor(std::istringstream& lineIn): Extractor(lineIn){}

    protected:
    virtual bool process(char symbol, std::string & output){
        if (isdigit(symbol)) {
            result += std::string(1,symbol);
            return false;
        }
        else if (result.size()) {
            output = result;
            result.erase();
            return true;
        }
        return false;
    }
};

std::shared_ptr<Extractor> getExtractor(const std::string& extractType, std::istringstream& lineIn){
    std::shared_ptr<Extractor> res = nullptr;
    if(extractType == "digits"){
        res = std::make_shared<DigitsExtractor>(lineIn);
        //res = std::shared_ptr<Extractor>(new DigitsExtractor(lineIn));
    }
    else if(extractType == "numbers"){
        res = std::make_shared<NumbersExtractor>(lineIn);
        //res = std::shared_ptr<Extractor>(new NumbersExtractor(lineIn));
    }
    else if(extractType == "quotes"){
        res = std::make_shared<QuoteExtractor>(lineIn);
        //res = std::shared_ptr<Extractor>(new QuoteExtractor(lineIn));
    }
    return res;
}

#endif //! ExtractorInitialization_h
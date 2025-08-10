#include "BigInt.h"
#include <iostream>

bool isDivisibleBy45(std::string bigValue){
    int sumDigits = 0;
    int lastDigit = 0;
    for(const char& c : bigValue){
        lastDigit = c - '0';
        sumDigits += lastDigit;
    }
    if(sumDigits % 9 == 0 and (lastDigit == 0 or lastDigit == 5))
        return true;

    return false;
}


int main(){

    std::string startInclusiveDigits, endExclusiveDigits;
    std::cin >> startInclusiveDigits >> endExclusiveDigits;

    BigInt startInclusiveBig(startInclusiveDigits), endExclusiveBig(endExclusiveDigits);

    while(startInclusiveBig < endExclusiveBig){
        if(isDivisibleBy45(startInclusiveBig.getDigits()))
            std::cout << startInclusiveBig << std::endl;
        startInclusiveBig += 1;
    }
    return 0;
}
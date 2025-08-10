#include <iostream>
#include <algorithm>
#include "Noise.h"
#include "Noises.h"

int main(){
    std::string time;
    std::string noiseWord;

    Noises noises;

    while(true){
        std::cin >> time >> noiseWord;
        std::string cmdToLower{noiseWord};
        std::transform(noiseWord.begin(), noiseWord.end(), cmdToLower.begin(), ::tolower);
        if(cmdToLower == "theend")
            break;
        std::cout << noises.registerNoise(time, noiseWord) << std::endl;
    }

    noises.printStatistics(std::cout);

    return 0;
}
#include <iostream>
#include <sstream>
#include <unordered_map>

typedef struct{
    int startRIdx;
    int startCIdx;
    int endRIdx;
    int endCIdx;
}glitchType;


int main(){
    int S;
    std::cin >> S;
    char matrix[S][S];
    char matrixOutput[S][S];
    std::unordered_map<char, glitchType>glitches;

    for(int rIdx = 0; rIdx < S; ++rIdx){
        for(int cIdx = 0; cIdx < S; ++cIdx){
            char c;
            std::cin >> c;
            matrix[rIdx][cIdx] = c;
            matrixOutput[rIdx][cIdx] = '.';

            if(c != '.'){
                if(! glitches.count(c)){
                    glitches[c].startRIdx = rIdx;
                    glitches[c].startCIdx = cIdx;

                    glitches[c].endRIdx = rIdx;
                    glitches[c].endCIdx = cIdx;

                    continue;
                }

                glitches[c].endRIdx = rIdx;
                glitches[c].endCIdx = cIdx;
            }
        }
    }

    for(const std::pair<char, glitchType>&glitch : glitches){
        int centerRIdx = (glitch.second.startRIdx + glitch.second.endRIdx) / 2;
        int centerCIdx = (glitch.second.startCIdx + glitch.second.endCIdx) / 2;

        matrixOutput[centerRIdx][centerCIdx] = glitch.first;
    }
    
    for(int rIdx = 0; rIdx < S; ++rIdx){
        for(int cIdx = 0; cIdx < S; ++cIdx)
            std::cout << matrixOutput[rIdx][cIdx];
        std::cout << std::endl;
    }

    return 0;
}
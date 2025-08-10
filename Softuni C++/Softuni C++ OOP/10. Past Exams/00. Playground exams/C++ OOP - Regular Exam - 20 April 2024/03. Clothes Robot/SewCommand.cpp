#include "SewCommand.h"

std::string SewCommand::execute(void) const{
    unsigned totalTime(getTime()), totalMaterial(0);
    for(auto& currId : elements){
        if(! existsData(currId))
            return abortMessage(currId);
        
        Processor::TimeAndMaterial tm = getData(currId);
        totalTime += tm.time;
        totalMaterial += tm.mat;
    }

    for(auto& currId : elements)
        eraseData(currId);
    
    insertData(Processor::TimeAndMaterial(totalTime, totalMaterial));
    
    return "";
}
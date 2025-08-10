#ifndef MEMORY_ALLOCATOR
#define MEMORY_ALLOCATOR

#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <memory>

#ifndef DEFINES_H_
#include "Defines.h"
#endif

ErrorCode executeCommand(const std::string &  command, std::vector<int *> & memory){
    std::istringstream inpstr(command);
    std::string cmd;
    int index;

    inpstr >> cmd;

    if(cmd == "Allocate" || cmd == "Deallocate"){
        inpstr >> index;
        if(index < 0 || index >= memory.size())
            return INDEX_OUT_OF_BOUND;
    }

    if(cmd == "Idle") return EXECUTE_IDLE;

    if(cmd == "Allocate"){
        if(memory[index] != nullptr)
            return MEMORY_LEAK;
        memory[index] = new int;
    }

    else if(cmd == "Deallocate"){
        if(memory[index] == nullptr)
            return DOUBLE_FREE;
        delete memory[index];
        memory[index] = nullptr;   
    }
    return  EXECUTE_SUCCESS;
}

void printResult(const ErrorCode errorCode, const std::string & command){
    std::string result;
    switch(errorCode){
        case EXECUTE_SUCCESS:
            result = "success";
            break;
        case EXECUTE_IDLE:
                result = "this exam is a piece of cake! Where is the OOP already?!?";
                break;
        case MEMORY_LEAK:
                result = "memory leak prevented, will not make allocation";
                break;
        case DOUBLE_FREE:
                result = "system crash prevented, will skip this deallocation";
                break;
        case INDEX_OUT_OF_BOUND:
                result = "out of bound";
                break;
    }
    std::cout << command << " - " << result << std::endl;
}

#endif // !MEMORY_ALLOCATOR
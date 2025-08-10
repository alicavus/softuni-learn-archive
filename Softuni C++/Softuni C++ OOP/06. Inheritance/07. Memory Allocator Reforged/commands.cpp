#include "Defines.h"
#include <iostream>
#include <vector>
#include <sstream>
#include <memory>

std::istream& operator>>(std::istream& istr, MemoryType& type){
    std::string result;
    if(result == "Single")
        type = MemoryType::SINGLE;
    else if(result == "Multiple")
        type = MemoryType::MULTIPLE;
    else
        type = MemoryType::UNKNOWN;
    return istr;
}

class Command{
    protected:
    std::vector<MemoryNode>& memory;

    public:
    Command(std::vector<MemoryNode>& memory): memory(memory) {}

    ~Command(){}
};

class MiddleCommandHelper : public Command{
    protected:
    int index;
    MemoryType type;

    public:
    MiddleCommandHelper(std::vector<MemoryNode>& memory, std::istringstream& istr)
    : Command(memory){
        istr >> type >> index;
    }
};

class AllocateCommand : public MiddleCommandHelper{
    public:
    AllocateCommand(std::vector<MemoryNode>& memory, std::istringstream& istr)
    : MiddleCommandHelper(memory, istr){}

    ErrorCode execute(){
        MemoryNode& memoryNode = memory[index];
        if(memoryNode.rawMemory == nullptr){
            memoryNode.memoryType = type;
            memoryNode.rawMemory = new int;
            return ErrorCode::EXECUTE_SUCCESS;
        }
        return ErrorCode::MEMORY_LEAK;
    }
};

class DeallocateCommand : public MiddleCommandHelper{
    public:
    DeallocateCommand(std::vector<MemoryNode>& memory, std::istringstream& istr)
    : MiddleCommandHelper(memory, istr){}

    ErrorCode execute(){
        MemoryNode& memoryNode = memory[index];
        if(memoryNode.rawMemory == nullptr)
            return ErrorCode::DOUBLE_FREE;
        if(memoryNode.memoryType != type)
            return ErrorCode::ALLOCATE_DEALLOCATE_MISMATCH;
        
        delete memoryNode.rawMemory;
        memoryNode.rawMemory = nullptr;
        memoryNode.memoryType = MemoryType::UNKNOWN;
        return ErrorCode::EXECUTE_SUCCESS;
    }
};

ErrorCode executeCommand(const std::string& command, std::vector<MemoryNode>& memory){
    std::istringstream istr(command);
    std::string cmdStr;
    istr >> cmdStr;

    ErrorCode result;
    if(cmdStr == "Allocate")
        result = AllocateCommand(memory, istr).execute();
    else if(cmdStr == "Deallocate")
        result = DeallocateCommand(memory, istr).execute();
    return result;
}

void printResult(const ErrorCode errorCode, const std::string& command){
    std::ostringstream ostr;
    ostr << command << " - ";
    switch(errorCode){
        case ErrorCode::EXECUTE_SUCCESS:
            ostr << "success";
            break;
        case ErrorCode::DOUBLE_FREE:
            ostr << "system crash prevented, will skip this deallocation";
            break;
        case ErrorCode::MEMORY_LEAK:
            ostr << "memory leak prevented, will not make allocation";
            break;
        case ErrorCode::ALLOCATE_DEALLOCATE_MISMATCH:
            ostr << "Warning allocate/deallocate mismatch, will skip this deallocation";
            break;
    }
    std::cout << ostr.str() << std::endl;
}


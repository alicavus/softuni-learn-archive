#pragma once

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include "CalculationEngine.h"
#include "InputInterpreter.h"

class DivisionOperation: public Operation {
    std::vector<int> operands;
    int result;
public:
    void addOperand(int operand) override {
        this->operands.push_back(operand);

        if (this->isCompleted()) {
            this->result = this->operands[0] / this->operands[1];
        }
    }

    bool isCompleted() override {
        return this->operands.size() == 2;
    }

    int getResult() override {
        return this->result;
    }
};

class MemorySaveOperation :  public Operation {
    std::stack<int> memory;
    public:
    void addOperand(int operand) override {
        this->memory.push(operand);
    }

    bool isCompleted() {
        return false;
    }

    int getResult() override {
        if(memory.empty())
            return 0;
        int top = memory.top();
        memory.pop();
        return top;
    }
};

class MemoryReadOperation :  public Operation {
    MemorySaveOperation & ms;
    public:
    MemoryReadOperation(MemorySaveOperation & ms) : ms(ms) {};

    void addOperand(int operand) override {}

    bool isCompleted() {
        return true;
    }

    virtual int getResult() override {
        return ms.getResult();
    }

};

class CustomInterpreter : public InputInterpreter {
    protected:
    std::shared_ptr<MemorySaveOperation> ms;

    public:
    CustomInterpreter(CalculationEngine & engine)
    : InputInterpreter(engine),
    ms(std::make_shared<MemorySaveOperation>()){};

    virtual std::shared_ptr<Operation> getOperation(std::string operation) override {
        if(operation == "/")
            return std::make_shared<DivisionOperation>();
        else if(operation == "ms")
            return ms;
        else if(operation == "mr")
            return std::make_shared<MemoryReadOperation>(*ms.get());
        else
            return InputInterpreter::getOperation(operation);
    }
};

std::shared_ptr<InputInterpreter> buildInterpreter(CalculationEngine& engine){
    std::shared_ptr<InputInterpreter> cust = std::make_shared<CustomInterpreter>(engine);
    return cust;
}
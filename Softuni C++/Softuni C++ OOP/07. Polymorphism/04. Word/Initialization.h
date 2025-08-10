#pragma once

#include "CommandInterface.h"

class CustomCommandInterface : public CommandInterface{
    class CutTransform : public TextTransform{
        std::string content;
        public:
        virtual void invokeOn(std::string& text, int startIndex, int endIndex) override {
            content = text.substr(startIndex, endIndex - startIndex);
            text.erase(startIndex, endIndex-startIndex);
        }
        const std::string& getContent() const{
            return content;
        }
    };

    class PasteTransform : public TextTransform{
        protected:
        std::shared_ptr<CutTransform> cutTransform;

        public:
        PasteTransform(std::shared_ptr<CutTransform> cutTransform) : cutTransform(cutTransform) {}

        virtual void invokeOn(std::string & text, int startIndex, int endIndex) override {
            text.erase(startIndex, endIndex - startIndex);
            text.insert(startIndex, cutTransform->getContent());
        }
    };
    protected:
    std::shared_ptr<CutTransform> cutTransform;

    public:
    CustomCommandInterface(std::string& text) : CommandInterface(text), cutTransform(std::shared_ptr<CutTransform>(new CutTransform())) {}

    virtual std::vector<Command> initCommands() override {
        std::vector<Command> ci = CommandInterface::initCommands();
        ci.push_back(Command("cut", cutTransform));
        ci.push_back(Command("paste", std::make_shared<PasteTransform>(cutTransform)));

        return ci;
    }
};

std::shared_ptr<CommandInterface> buildCommandInterface(std::string& text){
    std::shared_ptr<CommandInterface> ci = std::make_shared<CustomCommandInterface>(text);
    ci->init();

    return ci;
}
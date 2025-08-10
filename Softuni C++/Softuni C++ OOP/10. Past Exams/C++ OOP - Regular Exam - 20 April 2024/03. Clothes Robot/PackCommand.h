#ifndef _PACK_COMMAND_H_
#define _PACK_COMMAND_H_
#include <iostream>
#include <string>

class PackCommand : public Command{

    public:
    PackCommand(Processor & proc) : Command(proc){}

    virtual std::string getName(void) const override{ return "pack"; }
    virtual void read(std::istream & istr) override {}

    virtual std::string execute(void) const override{
        return successMessage();
    }

};

#endif //! _PACK_COMMAND_H_
#ifndef _IRON_COMMAND_H_
#define _IRON_COMMAND_H_

class IronCommand : public TimedCommand{

    public:
    IronCommand(Processor & proc) : Command(proc), TimedCommand(proc) {}

    virtual std::string getName(void) const override { return "iron"; }

    virtual void read(std::istream & istr) override {
        Command::read(istr);
        TimedCommand::read(istr);
    }

    virtual std::string execute(void) const override{
        if (!existsData(getId()))
            return abortMessage(getId());
        
        Processor::TimeAndMaterial tm = getData(getId());

        tm.time += getTime();

        eraseData(getId());

        insertData(tm);

        return "";
    }

};

#endif //!  _IRON_COMMAND_H_
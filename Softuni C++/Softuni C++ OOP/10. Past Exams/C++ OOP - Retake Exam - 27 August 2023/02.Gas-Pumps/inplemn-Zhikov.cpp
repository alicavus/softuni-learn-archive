#include "commands.h"
#include <math.h>



// class EndCommand::EndCommand : public Command {

//     public:

      //  EndCommand(std::istream & istr) : Command(istr) {} ;

        void EndCommand::process(void) {
            //todo

            outputTicks(std::cout);
            std::cout<<": Final gas quantity: "<<GasReservoir::get().getQuantity()<<" kg3"<<std::endl;
            //Hour 0035: Final gas quantity: 20 kg3
        }; 

//         virtual ~EndCommand() override {};
// };



// class InitCommand:: : public Command {

//     int initQ;

//     public:

        InitCommand::InitCommand(std::istream & istr) : Command(istr) {istr>>initQ;};

        void InitCommand::process(void) { //todo
        GasReservoir::get();
        GasReservoir::get().setQuantity(initQ);

        outputTicks(std::cout);
        std::cout<<": Gas quantity: "<<GasReservoir::get().getQuantity()<<" kg3"<<std::endl;

         };

        InitCommand:: ~InitCommand()  {};
// };



// class TwoParametersCommand : public Command {
//     private:
//         int par1, par2;
//     public:
//         TwoParametersCommand(std::istream & istr) : Command(istr) {
//             istr >> par1 >> par2;
//         }

//         int getPar1(void) const { return par1; }
//         int getPar2(void) const { return par2; }
// };

// class InCommand : public TwoParametersCommand {

//     public:

        InCommand::InCommand(std::istream & istr) : TwoParametersCommand(istr) {}; //todo

        void InCommand::process(void) {
            //todo
            GasReservoir::get().addCycles(this->getPar2());
            int prev=GasReservoir::get().getQuantity();
            prev+=getPar1()*getPar2();
            GasReservoir::get().setQuantity(prev);

            outputTicks(std::cout);
            std::cout<<": Pumping in "<<getPar1()<<" kg3 for "<<getPar2()<<" hours, remaining "<<GasReservoir::get().getQuantity()<<" kg3"<<std::endl;
            //Hour 0030: Pumping in 5 kg3 for 30 hours, remaining 20150 kg3
        };

        InCommand:: ~InCommand() {}; //todo
// };

// class OutCommand : public TwoParametersCommand {

//     public:

        OutCommand::OutCommand(std::istream & istr) : TwoParametersCommand(istr) {};//todo

        void OutCommand::process(void) {
            //todo
            GasReservoir::get().addCycles(this->getPar2());

            outputTicks(std::cout);
            if (GasReservoir::get().getQuantity()==0) {
                std::cout<<": Gas Storage Empty."<<std::endl;
            }
            else if (GasReservoir::get().getQuantity()>=(getPar1()*getPar2())) {
                std::cout<<": Delivering out "<<(getPar1()*getPar2())<<" kg3, remaining "<<
                GasReservoir::get().getQuantity()-(getPar1()*getPar2())<<" kg3"<<std::endl;
            }
            else {
                std::cout<<": Delivering out "<<GasReservoir::get().getQuantity()<<" kg3 (shortage "<<abs(GasReservoir::get().getQuantity()-(getPar1()*getPar2())) <<" kg3), remaining "<<
                "0 kg3"<<std::endl;
            }
            
            int currQ=GasReservoir::get().getQuantity();
            currQ-=(getPar1()*getPar2());
            if (currQ>0) {
            GasReservoir::get().setQuantity(currQ);
            }
            else {
                GasReservoir::get().setQuantity(0);
            };

        };

        OutCommand:: ~OutCommand() {};//todo
// };

// class DemandCommand : public TwoParametersCommand {

//     public:

        DemandCommand::DemandCommand(std::istream & istr) : TwoParametersCommand(istr) {}; //todo

        void DemandCommand::process(void) {
            //todo
            outputTicks(std::cout);
            if (GasReservoir::get().getQuantity()>=(getPar1()*getPar2())) {
                    std::cout<<": CHECK: OK."<<std::endl;
            }
            else if (GasReservoir::get().getQuantity()==0) {
                    std::cout<<": CHECK: Gas Storage Empty."<<std::endl;
            }
            else {
                std::cout<<": CHECK: Shortage of "<<(getPar1()*getPar2())-GasReservoir::get().getQuantity()<<
                ": availability "<<GasReservoir::get().getQuantity()/getPar2()<<" for "<<getPar2()
                <<" hours"<<std::endl;
                //Hour 0095: CHECK: Shortage of 16800: availability 40 for 30 hours
            };
        };

        DemandCommand:: ~DemandCommand() {}; //todo
// };


#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <memory>
#include <algorithm>
#include <cmath>

#include "defines.h"
#include "command.h"
#include "commands.h"

InitCommand::InitCommand(std::istream & istr)
: Command(istr) {
    size_t quantity;
    istr >> quantity;
    GasReservoir::get().setQuantity(quantity);
}

InitCommand::~InitCommand(){};

void InitCommand::process(void)
{
    GasReservoir& g = GasReservoir::get();
    std::cout << "Hour " << std::setfill('0') << std::setw(4) << g.getCycles() <<
     ": Gas quantity: " << g.getQuantity() << " kg3" << std::endl;
}

InCommand::InCommand(std::istream & istr)
: TwoParametersCommand(istr){}

InCommand::~InCommand(){}

void InCommand::process(void)
{
    GasReservoir& g = GasReservoir::get();
    g.addCycles(getPar2());
    g.setQuantity(g.getQuantity() + getPar1()*getPar2());

    std::cout << "Hour " << std::setfill('0') << std::setw(4) << g.getCycles() <<
     ": Pumping in " << getPar1() << " kg3 for " << getPar2() << 
     " hours, remaining " << g.getQuantity() << " kg3" << std::endl;
}


OutCommand::OutCommand(std::istream & istr)
: TwoParametersCommand(istr){}

OutCommand::~OutCommand(){}

void OutCommand::process(void)
{
    GasReservoir& g = GasReservoir::get();

    size_t currAvailableGas = g.getQuantity();
    size_t currDemand = getPar1()*getPar2();

    int shortage = currDemand - currAvailableGas;
    size_t currDelivering = (shortage > 0) ? currAvailableGas : currDemand;

    g.addCycles(getPar2());
    g.setQuantity(g.getQuantity() - currDelivering);

    std::cout << "Hour " << std::setfill('0') << std::setw(4) << g.getCycles() << ": ";
    if(! currAvailableGas)
        std::cout << "Gas Storage Empty." << std::endl;
    else{
        std::cout << "Delivering out " << currDelivering << " kg3";
        if(shortage > 0)
            std::cout << " (shortage "<< shortage <<" kg3)";
        std::cout <<  ", remaining " << g.getQuantity() << " kg3" << std::endl;     
    }
}

DemandCommand::DemandCommand(std::istream & istr)
: TwoParametersCommand(istr){}

DemandCommand::~DemandCommand(){}

void DemandCommand::process(void)
{
    GasReservoir& g = GasReservoir::get();
    size_t currAvailableGas = g.getQuantity();
    size_t currDemand = getPar1()*getPar2();

    std::cout << "Hour " << std::setfill('0') << std::setw(4) << g.getCycles() << ": CHECK: ";

    if(! currAvailableGas)
        std::cout << "Gas Storage Empty.";
    else if(currDemand <= currAvailableGas)
        std::cout << "OK.";
    else{
        size_t shortage = currDemand - currAvailableGas;
        double availability = std::floor(currAvailableGas / getPar2());
        std::cout << "Shortage of " << shortage;
        std::cout << ": availability " << availability << " for " << getPar2() << " hours";
    }
    std::cout << std::endl;

}

void EndCommand::process(void)
{
    GasReservoir& g = GasReservoir::get();
    std::cout << "Hour " << std::setfill('0') << std::setw(4) << g.getCycles() <<
     ": Final gas quantity: " << g.getQuantity() << " kg3" << std::endl;
}
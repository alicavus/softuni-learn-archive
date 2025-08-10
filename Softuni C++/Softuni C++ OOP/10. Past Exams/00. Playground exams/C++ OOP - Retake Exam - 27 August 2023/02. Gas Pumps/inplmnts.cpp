#include "commands.h"
#include <iostream>
#include <sstream>

InitCommand::InitCommand(std::istream & istr)
: Command(istr){
    GasReservoir& g = GasReservoir::get();
    int quantity;
    istr >> quantity;

    g.setQuantity(quantity);

}
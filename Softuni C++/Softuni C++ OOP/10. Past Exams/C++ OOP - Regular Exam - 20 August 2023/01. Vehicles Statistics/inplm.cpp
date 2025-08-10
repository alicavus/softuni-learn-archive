#include "classes.h"

void Vehicle::printInfo(ostream & output){
    output << this-> numberPlate << ", " << this->color; 
    if(dynamic_cast<TwoWheeler*>(this))
        output << " with 2 wheels.";
    else if(dynamic_cast<CarM*>(this))
        output << " medium car.";
    else if(dynamic_cast<CarL*>(this))
        output << " bigger car.";
    else if(dynamic_cast<TruckXL*>(this))
        output << " truck.";
    else if(dynamic_cast<TruckXXL*>(this))
        output << " big truck.";
}
#include "Defines.h"
#include "Car.h"
#include "AutomaticCar.h"
#include "ManualCar.h"
#include "RaceTrack.h"
#include <algorithm>
#include <iterator>
#include <iostream>

AutomaticCar::AutomaticCar(int maxSpeed, int fuel): Car(maxSpeed, fuel){}

void AutomaticCar::increaseSpeed(int speedIncrease, int fuelConsumtion){
    Car::increaseSpeed(speedIncrease, fuelConsumtion);
}

void AutomaticCar::decreaseSpeed(int speedDecrease){
    Car::decreaseSpeed(2 * speedDecrease );
}

ManualCar::ManualCar(const std::vector<int>& shiftSpeeds, int maxSpeed, int fuel):
Car(maxSpeed, fuel), _shiftSpeeds(shiftSpeeds){}

void ManualCar::increaseSpeed(int speedIncrease, int fuelConsumtion){
    size_t startingShiftIdx = findShiftIdx();

    Car::increaseSpeed(speedIncrease, fuelConsumtion);

    size_t endShiftIdx = findShiftIdx();

    if(endShiftIdx > startingShiftIdx && startingShiftIdx != _shiftSpeeds.size() - 1)
        Car::increaseSpeed(0, fuelConsumtion);

    _currShiftIdx = findShiftIdx();    
}

void ManualCar::decreaseSpeed(int speedDecrease){
    size_t startingShiftIdx = findShiftIdx();
    Car::decreaseSpeed(speedDecrease);
    size_t endShiftIdx = findShiftIdx();

    if(endShiftIdx != startingShiftIdx)
        _currShiftIdx = endShiftIdx;    
}

size_t ManualCar::findShiftIdx() const{
    auto it = std::upper_bound(_shiftSpeeds.begin(), _shiftSpeeds.end(), _curSpeed);
    size_t idx = std::distance(_shiftSpeeds.begin(), it);
    return idx;
}

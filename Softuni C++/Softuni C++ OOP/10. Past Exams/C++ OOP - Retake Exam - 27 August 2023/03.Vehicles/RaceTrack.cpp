#include "Defines.h"
#include "Car.h"
#include "AutomaticCar.h"
#include "ManualCar.h"
#include "RaceTrack.h"
#include <iostream>

bool RaceTrack::isRaceRunning() const{
    for(const auto& car : _cars){
        if(car.get()->isCarRunning() == false)
            return false;
    }
    return true;
}

void RaceTrack::printWinner(){
    int winnerCarIdx = -1;
    int maxDistance = -1;
    int currCarIdx = 0;
    std::vector<Car*> runningCars;

    for(const auto& car : _cars){
        Car* c = car.get();
        int curDistance = c->getDistance();
        if(c->isCarRunning()){
            if(curDistance >= maxDistance){
                if(curDistance > maxDistance){
                    maxDistance = curDistance;
                    if(runningCars.size())
                        runningCars.clear();
                    winnerCarIdx = currCarIdx;
                }
                else
                    winnerCarIdx = -1;
                runningCars.push_back(c);
            }
        }
        currCarIdx++;
    }

    if(winnerCarIdx == -1){
        std::cout << "No winner" << std::endl;
    }
    else{
        std::cout << "Car with index: " << winnerCarIdx << " won!" << std::endl;
    }
}

void RaceTrack::createAutomaticCar(int maxSpeed, int startFuel){
    _cars.push_back(std::make_unique<AutomaticCar>(maxSpeed, startFuel));
}

void RaceTrack::createManualCar(const std::vector<int> &shifts, int maxSpeed, int startFuel){
    _cars.push_back(std::make_unique<ManualCar>(shifts, maxSpeed, startFuel));
}

void RaceTrack::increaseSpeed(int speedIncrease, int fuelConsumtion){
    for(const auto& car : _cars)
        car->increaseSpeed(speedIncrease, fuelConsumtion);
}

void RaceTrack::decreaseSpeed(int speedDecrease){
    for(const auto& car : _cars)
        car->decreaseSpeed(speedDecrease);
}

void RaceTrack::advance(){
    for(const auto& car : _cars)
        car->advance();
}

void RaceTrack::printInfo() const{
    for(size_t idx = 0; idx < _cars.size(); ++idx)
        std::cout << "Car with index: " << idx << " has totalDistance: " << _cars[idx]->getDistance() <<
        ", is running with " << _cars[idx]->getSpeed() << " speed, has " <<
        _cars[idx]->getFuel() << " fuel left" << std::endl;
}
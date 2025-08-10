#include "Viking.h"
#include <iostream>

Viking::Viking(const AirShipType type,
    const int         health,
    const int         baseDamage,
    const int         shipId):

    TerranAirShip(type, health, baseDamage, shipId){}

void Viking::dealDamage( std::vector<std::unique_ptr<AirShip>> & enemyFleet)
{
    AirShip* victim = enemyFleet.back().get();
    victim->takeDamage(_damage);

    if (enemyFleet.back()->getAirShipType()==AirShipType::PHOENIX)
        victim->takeDamage(_damage);
    
    if (!victim->isAlive()) {
        std::cout << "Viking with ID: " << this->getAirShipId() << " killed enemy airship with ID: "
                << victim->getAirShipId() << std::endl;
        enemyFleet.pop_back();
    }

}
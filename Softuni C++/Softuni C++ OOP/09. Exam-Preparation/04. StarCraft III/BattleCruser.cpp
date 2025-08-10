#include "BattleCruser.h"
#include <iostream>

BattleCruser::BattleCruser(const AirShipType type,
    const int         health,
    const int         damage,
    const int         shipId)
    : TerranAirShip(type, health, damage, shipId){}

void BattleCruser::dealDamage(std::vector<std::unique_ptr<AirShip>> & enemyFleet)
{
    AirShip * victim=enemyFleet.back().get();

    int currDamage = _passedTurns % (YAMATO_CANNON_LOADING_TIME+1) ? _damage : _damage * 5;

    victim->takeDamage(currDamage);
    
    if (!victim->isAlive()) {
        std::cout << "BattleCruser with ID: " << this->getAirShipId() << " killed enemy airship with ID: "
                        << victim->getAirShipId() << std::endl;
        enemyFleet.pop_back();
    }
}
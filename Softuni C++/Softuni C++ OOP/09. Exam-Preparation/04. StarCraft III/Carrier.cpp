#include "Carrier.h"
#include <iostream>

Carrier::Carrier(const AirShipType type,
    const int         health,
    const int         damage,
    const int         maxShield,
    const int         shieldRegenerateRate,
    const int         shipId)
    : ProtossAirShip(type, health, damage, maxShield, shieldRegenerateRate, shipId) {}

void Carrier::takeDamage(const int damage)
{
    ProtossAirShip::takeDamage(damage);
    if(_currHealth<_maxHealth)
        _activeInterceptors=DAMAGED_STATUS_INTERCEPTORS;
}

void Carrier::dealDamage(
    std::vector<std::unique_ptr<AirShip>> & enemyFleet)
{
    for (size_t curr = 0; curr < _activeInterceptors; curr++) {
        AirShip * victim=enemyFleet.back().get();
        victim->takeDamage(_damage);
        if (!victim->isAlive()){
            std::cout << "Carrier with ID: " << this->getAirShipId() << " killed enemy airship with ID: "
                                      << victim->getAirShipId() << std::endl;
            enemyFleet.pop_back();
        }
        if (enemyFleet.empty())
            return;
    }
}
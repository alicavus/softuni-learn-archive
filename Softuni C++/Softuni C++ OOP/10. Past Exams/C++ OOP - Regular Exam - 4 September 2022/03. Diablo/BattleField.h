#ifndef BATTLEFIELD_H
#define BATTLEFIELD_H

#include <vector>
#include <memory>
#include "Hero.h"

class BattleField{
    std::vector<std::unique_ptr<Hero>> _heroes;

    public:
    void createHeroes();
    void startBattle();
    void createSpells();
    void printWinner(const std::unique_ptr<Hero> &hero);
};


#endif //! BATTLEFIELD_H

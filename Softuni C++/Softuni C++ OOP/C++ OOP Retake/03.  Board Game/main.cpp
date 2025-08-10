
#include "Soldier.h"
#include "Diagonalee.h"
#include "Fireside.h"
#include "Master.h"
#include "Engine.h"
#include "DangerCalculator.h"

#include <iostream>

//static
Figurine * Figurine::factory(const std::string & type, const Coord & coord) {
    switch(type[0]) {
        case 'S' : return new Soldier(coord);
        case 'D' : return new Diagonalee(coord);
        case 'F' : return new Fireside(coord);
        case 'M' : return new Master(coord);
    }

    return nullptr;
}

int main(void) {

    size_t size;
    std::cin >> size; std::cin.ignore();

    Engine e(size);

    std::string cmd;
    std::string lastDanger;
    while(getline(std::cin, cmd) && cmd != ".") {

        e.read(cmd);

        std::pair<size_t, std::string> danger = e.calculateDanger();
        std::cout << "Danger: " << danger.first << std::endl;
        lastDanger = danger.second;
#ifdef ___DEBUG___
        std::cout << lastDanger;
#endif
    }

    std::cout << lastDanger;

    return 0;
}

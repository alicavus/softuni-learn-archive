#ifndef FIGURINE_H
#define FIGURINE_H

#include "Coord.h"

#include <string>
#include <vector>

class Board;

class Figurine {

        Coord coord;

    public:

        Figurine(const Coord & coord) : coord(coord) {}
        virtual ~Figurine() = default;

        const Coord & getCoord() const { return coord; }

        // returns vector of fields, which are endangered by the Figurine
        virtual std::vector<Coord> endangersFields(const Board & b) const = 0;

        // returns the respective tags (chars) to represent the figurine in a board
        virtual char getNonEndangeredTag(void) const = 0;
        virtual char getEndangeredTag(void) const = 0;

        static Figurine * factory(const std::string & type, const Coord & coord);
};



#endif
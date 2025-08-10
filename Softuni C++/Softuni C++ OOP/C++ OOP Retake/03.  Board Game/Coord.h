#ifndef _COORD_H
#define _COORD_H

#include <string>

class Coord {

    public:

        // holds x (first) and y (second), which are already normalized (e.g. 0-based)
        typedef std::pair<int, int> Pair;

        Coord(const std::string coord = "A1")
            : coord(
                coord[0]-'A',
                coord.size() > 2 ? // below we always subtract 1 from the row, as "A1" is not normalized
                                (coord[1]-'0')*10 + coord[2]-'0' - 1: 
                                coord[1] - '0' - 1 
                ) {}

        Pair toIndex() const { return coord; }

        size_t toLinearIndex(size_t boardSize) const {
            // x (first) and y (second) are already normalized
            return coord.first + (coord.second)*boardSize;
        }

        // return the Coord, which differs that the current point with (dX, dY).
        // for example, to get the upper-right diagonal, dX = 1, dY = -1.
        // if boardSize is specified, the function will also check for going out of bounds
        Coord getDiff(int dX, int dY, int boardSize = 0) const { 
            Pair ret = coord;
            
            ret.first += dX;
            ret.second += dY;

            if (boardSize > 0) {
                if (ret.first >= boardSize)
                    ret.first = -1;
                if (ret.second >= boardSize)
                    ret.second = -1;
            }

            return Coord(ret);
        }

        bool valid(void) const {
            // we assume that any coord with values >=0 is valid.
            return coord.first >= 0 && coord.second >= 0;
        }

    private:
        Coord(Pair coord) : coord(coord) {}
        Pair coord;
};

#endif
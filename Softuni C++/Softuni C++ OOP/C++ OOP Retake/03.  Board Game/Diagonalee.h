#ifndef DIAGONALEE_H
#define DIAGONALEE_H

#include "Figurine.h"

class Diagonalee : public Figurine {

    public:

        Diagonalee(const Coord & coord) : Figurine(coord) {}

        virtual std::vector<Coord> endangersFields(const Board & b) const override {
            std::vector<Coord> res;
            size_t size = b.getSize();
            const Coord & c = getCoord();

            // attack all from the Diagonalee till the top-left end
            Coord next = c.getDiff(-1, -1, size);
            while(next.valid()) {
                res.push_back(next);
                if (b[next] != nullptr)
                    break; // we reached another figurine - cannot endanger after it
                next = next.getDiff(-1, -1, size);
            }

            // attack all from the Fireside till the bottom-right end of the board (size)
            next = c.getDiff(+1, +1, size);
            while(next.valid()) {
                res.push_back(next);
                if (b[next] != nullptr)
                    break; // we reached another figurine - cannot endanger after it
                next = next.getDiff(+1, +1, size);
            }

            // attack all from the Fireside till the top-right end of the board (size)
            next = c.getDiff(+1, -1, size);
            while(next.valid()) {
                res.push_back(next);
                if (b[next] != nullptr)
                    break; // we reached another figurine - cannot endanger after it
                next = next.getDiff(+1, -1, size);
            }

            // attack all from the Fireside till the top-right end of the board (size)
            next = c.getDiff(-1, +1, size);
            while(next.valid()) {
                res.push_back(next);
                if (b[next] != nullptr)
                    break; // we reached another figurine - cannot endanger after it
                next = next.getDiff(-1, +1, size);
            }

            return res;
        }

        virtual char getNonEndangeredTag(void) const override { return 'D'; }
        virtual char getEndangeredTag(void) const override { return 'd'; }

};

#endif
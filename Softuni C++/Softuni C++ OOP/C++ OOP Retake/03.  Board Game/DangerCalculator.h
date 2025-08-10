#ifndef __DANGER_CALCULATOR_H
#define __DANGER_CALCULATOR_H

#include <vector>

#include "Figurine.h"
#include "Board.h"
#include "FigurineCalculator.h"

class DangerCalculator : public FigurineCalculator {

    CharBoard cb;
    size_t size;

    public:

        DangerCalculator(size_t size, const Board & board) : cb(board), size(board.getSize()) {};

        virtual void calculate(const Figurine *f) override {
            std::vector<Coord> endangered = f->endangersFields(cb.getBoard());

            for(Coord & c : endangered) 
                if (c.valid()) {
                    char mark = '*';
                    const Figurine * fa = (cb.getBoard())[c];
                    if (fa != nullptr)
                        mark = fa->getEndangeredTag();
                    cb.mark(c, mark);
                }

        }

        std::pair<size_t, std::string> getDanger(void) const { 
            size_t dangerSize = 0;

            const std::vector<char> & contents = cb.getContents();
            for(char c : contents)
                if (c == '*' || (c >='a' && c <='z'))
                    dangerSize++;

            return std::pair<size_t, std::string>(dangerSize, (std::string)cb);
        }

};

#endif
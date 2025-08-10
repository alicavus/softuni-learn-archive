#ifndef __ENGINE_H
#define __ENGINE_H

#include "Board.h"
#include "DangerCalculator.h"

#include <vector>
#include <memory>
#include <sstream>

class Engine {

    std::vector< std::unique_ptr<Figurine>  > contents;
    Board board;

    public:

        Engine(size_t size) : board(size) { }

        void read(const std::string & str) {
            std::istringstream istr(str);

            std::string coord, type;
            istr >> coord >> type;

            Figurine * f = Figurine::factory(type, Coord(coord));
            contents.emplace_back(std::unique_ptr<Figurine>(f));
            board[coord] = f;
        }

        size_t getSize(void) const { return board.getSize(); }
        const Board & getBoard(void) const { return board; }

        void accept(FigurineCalculator & c) const {
            for (auto & f : contents)
                c.calculate(f.get());
        }

        std::pair<size_t, std::string> calculateDanger(void) const {

            DangerCalculator dc(board.getSize(), board);

            accept(dc);

            return dc.getDanger();

        }

};

#endif
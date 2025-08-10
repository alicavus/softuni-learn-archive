#ifndef __BOARD_H
#define __BOARD_H

#include "Coord.h"
#include "Figurine.h"

#include <vector>
#include <sstream>
#include <iomanip>

class Board {

    size_t size;
    std::vector<Figurine *> board;

    public:

        Board(size_t size) : size(size), board(size*size, nullptr) { }

        Figurine * & operator[](const Coord & index) {
            return board[index.toLinearIndex(size)];
        }

        const Figurine * operator[](const Coord & index) const {
            return board[index.toLinearIndex(size)];
        }

        const std::vector<Figurine *> & getFigurines() const { return board; }

        size_t getSize(void) const { return size; }
};

class CharBoard { 

    protected:

        const Board & board;
        size_t size;
        std::vector<char> contents;

    public:

        CharBoard(const Board & board, char initChar = '.') : board(board), size(board.getSize()), contents(size*size, initChar){
            const std::vector<Figurine *> & figs = board.getFigurines();
            for(auto f : figs) 
                if (f != nullptr) {
                    mark(f->getCoord(), f->getNonEndangeredTag());
                }
        } 

        void mark(const Coord & coord, char c) {
            contents[coord.toLinearIndex(size)] = c;
        }

        void mark(const std::vector<Coord> & coords, char c) {
            for(auto coord : coords)
                mark(coord, c);
        }

        const Board & getBoard(void) const { return board; }
        const std::vector<char> & getContents() const { return contents; }

        operator std::string() const {
            std::ostringstream ostr;
            for(int row = size-1; row >=0; row--) {
                ostr<< std::setw(2) << std::setfill(' ') << row+1 << "|";
                for(size_t col = 0; col < size; col++) {
                    ostr << ' ' << contents[row*size+col];
                }
                ostr << std::endl;
            }
            // now print the final line
            ostr << "  " << std::string(2+size*2, '-') << std::endl << "   ";
            for(int col = 0; col < size; col++)
                ostr << ' ' << char('A' + col);
            ostr << std::endl;
            return ostr.str();
        }

};

#endif
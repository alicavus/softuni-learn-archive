#include <iostream>
#include <vector>
#include "Matrix.h"

int doBasicMath(int a, int b, char op){
    switch(op){
        case '+':
            return a + b;
        case '-':
            return a - b;
        case '*':
            return a * b;
        case '/':
            return (b == 0) ? 0 : a / b;
    }
    return 0;
}

Matrix& Matrix::operator=(const std::vector<std::vector<int>> & data){
    _data.clear();

    std::vector<int> _row;   
    for(const std::vector<int>& row : data){
        for(const int& cell : row)
            _row.push_back(cell);
        _data.push_back(std::move(_row));
        _row.clear();
    }
    return *this;
}

std::vector<std::vector<int>>& doVectMath(std::vector<std::vector<int>>& first, const std::vector<std::vector<int>>& second, char op){
    std::vector<std::vector<int>> mergedVect;

    std::vector<int>mergedRow;
    for(size_t rIdx = 0; rIdx < std::max(first.size(), second.size()); ++rIdx){
        if(rIdx < std::min(first.size(), second.size())){
            for(size_t cIdx = 0; cIdx < std::max(first[rIdx].size(), second[rIdx].size()); ++cIdx){
                if(cIdx < std::min(first[rIdx].size(), second[rIdx].size()))
                    mergedRow.push_back(doBasicMath(first[rIdx][cIdx], second[rIdx][cIdx], op));
                else{
                    if(cIdx < first[rIdx].size())
                        mergedRow.push_back(first[rIdx][cIdx]);
                    else if (cIdx < second[rIdx].size())
                        mergedRow.push_back(second[rIdx][cIdx]);
                }
            }
        }
        else{
            if(rIdx < first.size())
                mergedRow = first[rIdx];
            else if(rIdx < second.size())
                mergedRow = second[rIdx];
        }
        mergedVect.push_back(std::move(mergedRow));
        mergedRow.clear();
    }
    first = std::move(mergedVect);
    return first;
}

Matrix& Matrix::operator+=(const Matrix& other){
    _data = doVectMath(_data, other._data, '+');
    return *this;
}

Matrix& Matrix::operator-=(const Matrix& other){
    _data = doVectMath(_data, other._data, '-');
    return *this;
}

Matrix& Matrix::operator*=(const Matrix& other){
    _data = doVectMath(_data, other._data, '*');
    return *this;
}

Matrix& Matrix::operator/=(const Matrix& other){
    _data = doVectMath(_data, other._data, '/');
    return *this;
}

std::ostream& operator<<(std::ostream & os, const Matrix & matrix){
    for(const std::vector<int>& row : matrix._data){
        for(const int& cell : row)
            os << cell << ' ';
        os << std::endl;
    }
    return os;
}
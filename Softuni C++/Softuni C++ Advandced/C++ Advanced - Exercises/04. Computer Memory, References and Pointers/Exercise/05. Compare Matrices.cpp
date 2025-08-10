#include <iostream>
#include <sstream>
#include <cstring>
#include <memory>

#define maxRows 10
#define maxCols 10

int** readMatrix(int &rowsCnt, int &colsCnt){
    std::cin >> rowsCnt;

    if(rowsCnt > maxRows)
        rowsCnt = maxRows;
    
    int** matrix = new int*[maxRows];
    for(int rIdx = 0; rIdx < rowsCnt; ++rIdx){
        matrix[rIdx] = new int[maxCols];
        std::string curRowBuff;
        getline(std::cin >> std::ws, curRowBuff);
        std::stringstream inpst(curRowBuff);
        colsCnt = 0;
        for(int cIdx = 0; inpst >> matrix[rIdx][cIdx] && cIdx < maxCols; ++cIdx)
            ++colsCnt;

    }
    return matrix;
}

void deallocateMatrix(int** matrix, int&rowsCnt){
    for(int rIdx = 0; rIdx <= rowsCnt; ++rIdx)
            delete[] matrix[rIdx];
    delete[] matrix;
}

bool areMatricesEqual(int** matrixOne, int** matrixTwo, int& rowsCntOne, int& rowsCntTwo, int &colsCntOne, int &colsCntTwo){
    if(rowsCntOne != rowsCntTwo or colsCntOne != colsCntTwo)
        return false;
    for(int rIdx = 0; rIdx < rowsCntOne; ++rIdx)
        for(int cIdx = 0; cIdx < colsCntOne; ++cIdx)
            if(matrixOne[rIdx][cIdx] != matrixTwo[rIdx][cIdx])
                return false;
    return true;
}

int main(){
    int rowsCntOne, rowsCntTwo, colsCntOne, colsCntTwo;
    int** matrixOne = readMatrix(rowsCntOne, colsCntOne);
    int** matrixTwo = readMatrix(rowsCntTwo, colsCntTwo);

    std::cout << (areMatricesEqual(matrixOne, 
    matrixTwo, rowsCntOne, rowsCntTwo, colsCntOne, colsCntTwo)?
    "equal" : "not equal" ) << std::endl;

    deallocateMatrix(matrixOne, rowsCntOne);
    deallocateMatrix(matrixTwo, rowsCntTwo);

    return 0;
}
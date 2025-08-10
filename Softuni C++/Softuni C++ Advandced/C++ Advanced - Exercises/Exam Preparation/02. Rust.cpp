#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <array>

using namespace std;

constexpr size_t arraySize = 10;

void coroseMetal(array<array<char, arraySize>, arraySize>&metalSquare, pair<int, int>cell){
    if (cell.first >= 0 and cell.first < arraySize and cell.second >= 0 and cell.second < arraySize){
        if(metalSquare[cell.first][cell.second] != '#')
            metalSquare[cell.first][cell.second] = '!';
    }
}

void corosionEffect(array<array<char, arraySize>, arraySize>&metalSquare){
    array<array<char, arraySize>, arraySize>metalSquareCopy = metalSquare;
    for(size_t rowIdx = 0; rowIdx < arraySize; ++rowIdx)
        for(size_t colIdx = 0; colIdx < arraySize; ++colIdx)
            if(metalSquare[rowIdx][colIdx] == '!'){
                coroseMetal(metalSquareCopy, pair<int, int>({rowIdx - 1, colIdx}));
                coroseMetal(metalSquareCopy, pair<int, int>({rowIdx, colIdx - 1}));
                coroseMetal(metalSquareCopy, pair<int, int>({rowIdx, colIdx + 1}));
                coroseMetal(metalSquareCopy, pair<int, int>({rowIdx + 1, colIdx}));
            }
    metalSquare = metalSquareCopy;
}

int main(){
    array<array<char, arraySize>, arraySize>metalSquare;
    for(size_t rowIdx = 0; rowIdx < arraySize; ++rowIdx)
        for(size_t colIdx = 0; colIdx < arraySize; ++colIdx)
            cin >> metalSquare[rowIdx][colIdx];
    
    int iterations;
    cin >> iterations;

    while(iterations--)
        corosionEffect(metalSquare);
    
    for(size_t rowIdx = 0; rowIdx < arraySize; ++rowIdx){
        for(size_t colIdx = 0; colIdx < arraySize; ++colIdx){
            cout << metalSquare[rowIdx][colIdx];
        }
        cout << endl;
    }


    return 0;
}
#include <iostream>
#include <sstream>
#include <cstring>
#include <memory>

int minesCount(char** matrix, int &rIdx, int &cIdx, int &N, int &M){
    int cnt = 0;
    for(int curRow = rIdx-1; curRow <= rIdx+1; ++curRow){
        if(curRow < 0 || curRow >= N)
            continue;
        for(int curCol = cIdx-1; curCol <= cIdx+1; ++curCol){
            if(curCol < 0 || curCol >= M)
                continue;
            if(matrix[curRow][curCol] == '!')
                cnt++;
        }
    }
    return cnt;
}

int main(){
    int N, M;
    std::cin >> N >> M;

    char** matrix = new char* [N];
    for(int rIdx = 0; rIdx < N; ++rIdx){
        matrix[rIdx] = new char [M];
        for(int cIdx = 0; cIdx < M; ++cIdx)
            std::cin >> matrix[rIdx][cIdx];
    }

    for(int rIdx = 0; rIdx < N; ++rIdx){
        bool bFirst = true;
        for(int cIdx = 0; cIdx < M; ++cIdx){
            if(! bFirst){
                std::cout << ' ';
                bFirst = false;
            }
            std::cout << minesCount(matrix, rIdx, cIdx, N, M);
        }
        std::cout << std::endl;
    }

    for(int rIdx = 0; rIdx < N; ++rIdx)
        delete[] matrix[rIdx];
    delete[] matrix;
    
    return 0;
}
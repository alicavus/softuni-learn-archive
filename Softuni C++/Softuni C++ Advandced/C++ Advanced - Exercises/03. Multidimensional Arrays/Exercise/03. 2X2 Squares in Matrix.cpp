#include <iostream>
#include <sstream>
#include <queue>
#include <stack>
#include <vector>

using namespace std;

template<typename T> bool cmpFour(T a, T b, T c, T d){
    if(a == b and a == c and a == d)
        return true;
    return false;
}

int main(){
    size_t R, C;
    cin >> R >> C;

    char matrix[R][C];
    
    for(size_t rowIdx = 0; rowIdx < R; ++rowIdx)
        for(size_t colIdx = 0; colIdx < C; ++colIdx)
            cin >> matrix[rowIdx][colIdx];
    
    
    size_t cnt = 0;
    for(size_t rowIdx = 0; rowIdx < R-1; ++rowIdx)
        for(size_t colIdx = 0; colIdx < C-1; ++colIdx)
            if(cmpFour(matrix[rowIdx][colIdx], matrix[rowIdx][colIdx+1], matrix[rowIdx+1][colIdx], matrix[rowIdx+1][colIdx+1]))
                cnt++;
    
    cout << cnt << endl;

    return 0;
}


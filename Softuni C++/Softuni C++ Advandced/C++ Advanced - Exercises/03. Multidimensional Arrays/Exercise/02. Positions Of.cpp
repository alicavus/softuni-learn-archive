#include <iostream>
#include <sstream>
#include <queue>
#include <stack>
#include <vector>

using namespace std;

int main(){
    size_t R, C;
    cin >> R >> C;

    int matrix[R][C];

    queue<pair<int, int>>q;
    
    for(size_t rowIdx = 0; rowIdx < R; ++rowIdx)
        for(size_t colIdx = 0; colIdx < C; ++colIdx)
            cin >> matrix[rowIdx][colIdx];
    
    int N;
    cin >> N;

    for(size_t rowIdx = 0; rowIdx < R; ++rowIdx)
        for(size_t colIdx = 0; colIdx < C; ++colIdx)
            if(matrix[rowIdx][colIdx] == N)
                q.push(make_pair(rowIdx, colIdx));
    
    if(q.empty())
        cout << "not found" << endl;
    
    while(q.size()){
        cout << q.front().first << ' ' << q.front().second << endl;
        q.pop();
    }

    return 0;
}
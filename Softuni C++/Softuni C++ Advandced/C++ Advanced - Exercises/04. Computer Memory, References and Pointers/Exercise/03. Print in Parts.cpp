#include <iostream>
#include <sstream>
#include <memory>

#define maxSize 100000
using namespace std;

int main(){
    int N, M;
    cin >> N >> M;

    unique_ptr<int[]> arr = make_unique<int[]>(maxSize);
    
    for(int rowIdx = 0; rowIdx < N; ++rowIdx)
        for(int colIdx = 0; colIdx < M; ++colIdx)
            cin >> arr[rowIdx*M + colIdx];

    int R, C;
    cin >> R >> C;

    for(int rowIdx = 0; rowIdx < R; ++rowIdx){
        bool bFirst = true;
        for(int colIdx = 0; colIdx < C; ++colIdx){
            if(!bFirst)
                cout << ' ';
            bFirst = false;
            cout << flush << arr[rowIdx*M + colIdx];
        }
        cout << endl;
    }

    return 0;
}
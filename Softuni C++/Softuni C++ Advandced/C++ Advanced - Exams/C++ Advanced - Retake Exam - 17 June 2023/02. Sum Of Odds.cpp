#include <iostream>
#include <sstream>
#include <map>
#include <vector>

using namespace std;

int main(){
    size_t N;
    cin >> N;
    int matrix[N][N];


    int oddSum = 0;
    for(size_t rowIdx = 0; rowIdx < N; ++rowIdx){
        for(size_t colIdx = 0; colIdx < N; ++colIdx){
            cin >> matrix[rowIdx][colIdx];
            if (rowIdx != colIdx && rowIdx + colIdx != N-1 && matrix[rowIdx][colIdx] % 2)
                oddSum += matrix[rowIdx][colIdx];
        }
    }
    cout << "The sum is: " << oddSum << endl;
    return 0;
}
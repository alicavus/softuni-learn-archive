#include <iostream>
#include <sstream>
#include <map>
#include <vector>
#include <set>
#include <cmath>

using namespace std;

int main(){
    int sizeMatrix;
    cin >> sizeMatrix;

    int matrix[sizeMatrix][sizeMatrix];
    
    int sum = 0;
    for(int rowIdx = 0; rowIdx < sizeMatrix; ++rowIdx){
        for(int colIdx = 0; colIdx < sizeMatrix; ++colIdx){
            cin >> matrix[rowIdx][colIdx];
            if(rowIdx != colIdx and rowIdx != sizeMatrix - colIdx - 1){
                if(matrix[rowIdx][colIdx] % 2) sum += matrix[rowIdx][colIdx];
            }
        }
    }
    cout << "The sum is: " << sum << endl;
    return 0;
}

#include <iostream>
#include <sstream>
#include <unordered_map>
#include <vector>
#include <set>
#include <cmath>

using namespace std;

bool isPrime(int num){
    for(int divider = 2; divider <= sqrt(num); ++divider)
        if(num % divider == 0)
            return false;
    return true;
}

int main(){
    int N;
    cin >> N;

    int matrix[N][N];
    for(size_t rIdx = 0; rIdx < N; ++rIdx)
        for(size_t cIdx = 0; cIdx < N; ++cIdx)
            cin >> matrix[rIdx][cIdx];
    
    size_t halfSize = N / 2;

    int sumOfPrimes = 0;

    for(size_t cIdx = 1; cIdx < N-1; ++cIdx){
        size_t rIdx = (cIdx <= N /2)? N - cIdx : cIdx + 1;
        for(; rIdx < N ;++rIdx){
            if(cIdx == rIdx)
                continue;
            
            if(isPrime(matrix[rIdx][cIdx]))
                sumOfPrimes += matrix[rIdx][cIdx];
        }        
    }

    cout << sumOfPrimes << endl;
    return 0;
}
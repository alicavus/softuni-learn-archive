#include <iostream>
#include <sstream>
#include <queue>
#include <stack>
#include <vector>

using namespace std;

void readMatrix(vector<vector<int>>&matrix){
    size_t rowsCount;
    cin >> rowsCount;

    for(size_t rowIdx = 0; rowIdx < rowsCount; ++rowIdx){
        vector<int>row;

        string buf;
        cin.ignore();
        getline(cin, buf);

        istringstream inps(buf);

        for(int num; inps >> ws >> num;)
            row.push_back(num);
        
        if(row.size()) matrix.push_back(row);
    }
}

bool areMatrixesSame(vector<vector<int>>&matrixOne, vector<vector<int>>&matrixTwo){
    if(matrixOne.size() != matrixTwo.size())
        return false;
    
    for(size_t idx = 0; idx < matrixOne.size(); idx++){
        vector<int>::iterator itOne = matrixOne[idx].begin();
        vector<int>::iterator itTwo = matrixTwo[idx].begin();
        while(itOne != matrixOne[idx].end() and itTwo != matrixTwo[idx].end()){
            if(itOne == matrixOne[idx].end() or itTwo == matrixTwo[idx].end())
                return false;
            if(*itOne != *itTwo)
                return false;
            itOne++;
            itTwo++;
        }
    }
    return true;
}

int main(){
    vector<vector<int>>matrixOne;
    vector<vector<int>>matrixTwo;

    readMatrix(matrixOne);
    readMatrix(matrixTwo);

    cout << (areMatrixesSame(matrixOne, matrixTwo)? "" : "not ") << "equal" << endl;


    return 0;
}
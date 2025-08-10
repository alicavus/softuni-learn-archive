#include <iostream>
#include <sstream>
#include <vector>
#include <map>

using namespace std;

int main(){
    string matrix[5];

    for(string studentInfo; getline(cin >> ws, studentInfo) && studentInfo != "END";){
        string studentName;
        int studentRoom;

        istringstream iss(studentInfo);
        iss >> studentName >> studentRoom;

        matrix[studentRoom] += studentName + " ";
    }

    for(string studentName; getline(cin >> ws, studentName) && studentName != "END";){
        bool isFound = false;
        cout << studentName << ':';
        for(size_t roomNo = 1; roomNo <= 4; ++roomNo){
            if(matrix[roomNo].find(studentName) != string::npos){
                isFound = true;
                cout << ' ' << roomNo;
            }
        }
        if(! isFound)
            cout << " Not found!";
        
        cout << endl;
    }
}
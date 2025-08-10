#include <iostream>
#include <sstream>
#include <stack>

using namespace std;

int main(){
    stack<int>s;
    {
        string intNumbers;
        getline(cin >> ws, intNumbers);
        istringstream iss(intNumbers);

        for(int n; iss >> n;)
            s.push(n);
    }

    for(string cmdLine; getline(cin, cmdLine);){
        if(cmdLine == "end") break;

        istringstream iss(cmdLine);
        string cmd;

        iss >> cmd;

        if(cmd == "add"){
            int numberOne, numberTwo;
            iss >> numberOne >> numberTwo;
            s.push(numberOne);
            s.push(numberTwo);
        }

        else if(cmd == "remove"){
            int cntNumbersToRemove;
            iss >> cntNumbersToRemove;

            if(cntNumbersToRemove > s.size()) continue;

            while(cntNumbersToRemove--)
                s.pop();
        }
    }
    
    int sum = 0;
    while(!s.empty()){
        sum += s.top();
        s.pop();
    }

    cout << sum << endl;

    return 0;
}
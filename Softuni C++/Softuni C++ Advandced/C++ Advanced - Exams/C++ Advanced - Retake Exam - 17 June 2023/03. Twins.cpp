#include <iostream>
#include <sstream>
#include <map>
#include <vector>
#include <queue>

using namespace std;

int main(){
    int N;
    cin >> N;
    queue<pair<string, int>>pepiQ, mimiQ;
    for(size_t curr = 0; curr < N; ++curr){
        string buf;
        getline(cin >> ws, buf);
        istringstream iss(buf);
        string cashier, customer;
        int minutes;
        iss >> cashier >> customer >> minutes;
        queue<pair<string, int>>*p = (cashier == "Pepi") ? &pepiQ : (cashier == "Mimi") ? &mimiQ : nullptr;
        p -> push(pair<string, int>({customer, minutes}));
    }
    int T;
    cin >> T;
    for(size_t timeIdx = 0; timeIdx < T; ++timeIdx){
        if(pepiQ.size()){
            pair<string, int>*currClient = &pepiQ.front();
            cout << "Pepi processing " << currClient -> first << endl;
            currClient -> second--;
            if(! currClient -> second) pepiQ.pop();
        }
        else cout << "Pepi Idle" << endl; 

        if(mimiQ.size()){
            pair<string, int>*currClient = &mimiQ.front();
            cout << "Mimi processing " << currClient -> first << endl;
            currClient -> second--;
            if(! currClient -> second) mimiQ.pop();
        }
        else cout << "Mimi Idle" << endl; 
    }
    return 0;
}
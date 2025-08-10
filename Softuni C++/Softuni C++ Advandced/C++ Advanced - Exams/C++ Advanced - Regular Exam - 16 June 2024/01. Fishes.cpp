#include <iostream>
#include <sstream>
#include <queue>
#include <stack>

using namespace std;

template<typename T> void printFishes(T s){
    return;
}

void printStack(stack<string>&s){
    cout << "Flow A:" << endl;

    if(s.empty())
        cout << "<EMPTY>";
    
    while(!s.empty()){
        cout << s.top();
        if(s.size() > 1)
            cout << ", ";
        s.pop();
    }
    cout << endl;
}

void printQueue(queue<string>&q){
    cout << "Flow B:" << endl;

    if(q.empty())
        cout << "<EMPTY>";
    
    while(!q.empty()){
        cout << q.front();
        if(q.size() > 1)
            cout << ", ";
        q.pop();
    }
    cout << endl;
}

int main(){
    stack<string>A;
    queue<string>B;
    {
        string fishName, fishFlow;
        while(true){
            cin >> fishName;

            if(fishName == "end") break;

            cin >> fishFlow;

            if(fishFlow == "A")
                A.push(fishName);
            
            else if(fishFlow == "B")
                B.push(fishName);
        }
    }

    printStack(A);
    printQueue(B);
}
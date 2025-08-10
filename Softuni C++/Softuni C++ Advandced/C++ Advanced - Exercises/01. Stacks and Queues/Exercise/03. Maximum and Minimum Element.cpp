#include <iostream>
#include <sstream>
#include <stack>

using namespace std;

void findMax(stack<int>s){
    if(s.empty())
        return;

    int m = s.top();
    while (! s.empty()){
        m = max(m, s.top());
        s.pop();
    }
    cout << m << endl; 
}

void findMin(stack<int>s){
    if(s.empty())
        return;

    int m = s.top();
    while (! s.empty()){
        m = min(m, s.top());
        s.pop();
    }
    cout << m << endl; 
}

int main(){
    stack<int>s;
    int N;
    cin >> N;

    for(size_t i = 0; i < N; ++i){
        int cmd, number;
        cin >> cmd;
        switch(cmd){
            case 1:
                cin >> number;
                s.push(number);
                break;
            case 2:
                if(!s.empty()) s.pop();
                break;
            case 3:
                findMax(s);
                break;
            case 4:
                findMin(s);
                break;
        }
    }

    while(!s.empty()){
        cout << s.top();
        if(s.size() > 1) cout << ", ";
        s.pop();
    }
    cout << endl;

    return 0;
}
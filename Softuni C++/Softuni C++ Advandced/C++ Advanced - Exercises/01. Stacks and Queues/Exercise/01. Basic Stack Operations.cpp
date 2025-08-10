#include <iostream>
#include <sstream>
#include <stack>

using namespace std;

int main(){
    int N, S, X;
    cin >> N >> S >> X;

    stack<int>s;
    {
        for(size_t i=1; i <=N; ++i){
            int tmp;
            cin >> tmp;
            s.push(tmp);
        }
    }

    while(S--)
        s.pop();
    
    stack<int> s1 = s;

    bool isFound = false;


    if(s.empty())
        cout << 0 << endl;
    
    else {
        int minEl = s1.top();

        while(!s1.empty()){
            if(s1.top() == X) isFound = true;
            minEl = min(minEl, s1.top());
            s1.pop();
        }

        cout << ((isFound) ? "true" : to_string(minEl) )<< endl;

    }
    return 0;
}
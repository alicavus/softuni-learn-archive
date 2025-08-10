#include <iostream>
#include <sstream>
#include <queue>

using namespace std;

int main(){
    int N, S, X;
    cin >> N >> S >> X;

    queue<int>s;
    {
        for(size_t i=1; i <=N; ++i){
            int tmp;
            cin >> tmp;
            s.push(tmp);
        }
    }

    while(S--)
        s.pop();

    bool isFound = false;


    if(s.empty())
        cout << 0 << endl;
    
    else {
        queue<int> s1 = s;
        int minEl = s1.front();

        while(!s1.empty()){
            if(s1.front() == X) isFound = true;
            minEl = min(minEl, s1.front());
            s1.pop();
        }

        cout << ((isFound) ? "true" : to_string(minEl) )<< endl;

    }
    return 0;
}
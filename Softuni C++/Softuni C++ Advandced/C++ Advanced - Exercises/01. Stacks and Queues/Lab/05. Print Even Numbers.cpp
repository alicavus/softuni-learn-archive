#include <iostream>
#include <sstream>
#include <queue>

using namespace std;

void printQueue(queue<int>& qq){
    queue<int> q = qq;
    while(! q.empty()){
        cout << q.front();
        if(q.back() != q.front())
            cout << ", ";
        q.pop();
    }
    cout << endl;
}

int main(){
    queue<int>q, qEven;
    {
        string input;
        getline(cin, input);

        istringstream iss(input);

        for(int n; iss >> n;)
            q.push(n);
    }

    while(!q.empty()){
        if(q.front() % 2 == 0)
            qEven.push(q.front());
        q.pop();
    }

    printQueue(qEven);

    return 0;
}
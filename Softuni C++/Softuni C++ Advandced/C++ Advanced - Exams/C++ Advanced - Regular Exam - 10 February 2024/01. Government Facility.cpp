#include <iostream>
#include <sstream>
#include <queue>
#include <stack>

using namespace std;

void printQue(queue<string>q){
    if(q.size()){
        while(q.size()){
            cout << ' ' << q.front();
            q.pop();
        }
    }
    else cout << " <empty>";
    cout << endl;
}

void printStack(stack<string>s){
    if(s.size()){
        while(s.size()){
            cout << ' ' << s.top();
            s.pop();
        }
    }
    else cout << " <empty>";
}

int main(){
    queue<string> q1, q2;
    stack<string> s3;

    for(string commands; getline(cin>>ws, commands) && commands != "5";){
        istringstream iss(commands);
        string name;
        int N;
        if(iss >> N){
            switch(N){
                case 10:
                    q1.pop();
                    break;
                case 20:
                    q2.pop();
                    break;
                case 12:
                    q2.push(q1.front());
                    q1.pop();
                    break;
                case 23:
                    s3.push(q2.front());
                    q2.pop();
                    break;
                case 31:
                    q1.push(s3.top());
                    s3.pop();
                    break;
                case 99:
                    cout << "1:";
                    printQue(q1);
                    cout << "2:";
                    printQue(q2);
                    cout << "3:";
                    printStack(s3);
                    break;
            }
        }
        else{
            iss.clear();
            string name;
            iss >> name >> N;
            queue<string>*pq = (N == 1) ? &q1 : (N == 2)? &q2 : nullptr;

            if(pq != nullptr) pq -> push(name);
        }
    }
    return 0;
}
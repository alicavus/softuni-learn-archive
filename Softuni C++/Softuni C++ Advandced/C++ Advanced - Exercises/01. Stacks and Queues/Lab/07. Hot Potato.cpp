#include <iostream>
#include <sstream>
#include <queue>

using namespace std;

void rotateQueue(queue<string> &q, unsigned &n){
    for(size_t ix=1; ix <= n; ++ix){
        if(ix != n) q.push(q.front());
        else cout << "Removed " << q.front() << endl;
        q.pop();
    }
}

int main(){
    queue<string>circle;

    {
        string input;
        getline(cin, input);
        istringstream iss(input);

        for(string name; iss>>ws>>name;)
            circle.push(name);
    }

    unsigned n;
    cin >> n;

    while(circle.size() > 1)
        rotateQueue(circle, n);
    

    cout << "Last is " << circle.front() << endl;

    return 0;
}
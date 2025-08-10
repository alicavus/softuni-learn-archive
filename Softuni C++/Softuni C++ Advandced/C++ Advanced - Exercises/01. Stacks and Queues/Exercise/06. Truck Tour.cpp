#include <iostream>
#include <sstream>
#include <queue>

using namespace std;

void rotateQueue(queue<pair<int, int>>&q){
    q.push(q.front());
    q.pop();
}

bool circleAll(queue<pair<int, int>>q){
    int gass = 0;
    while(! q.empty()){
        gass += q.front().first;
        if(gass < q.front().second) break;
        else{
            gass -= q.front().second;
            q.pop();
        }
    }
    return q.empty();
}

int main(){
    int N;
    cin >> N;
    cin.ignore();

    queue<pair<int, int>>pumps;

    {
        string input;
        for(size_t cnt = 1; cnt <= N; ++cnt){
            int first, second;
            cin >> first >> second;

            pumps.push(make_pair(first, second));
        }
    }

    size_t idx = 0;

    while(! circleAll(pumps)){
        rotateQueue(pumps);

        idx++;

        if(idx == N) idx = 0;
    }

    cout << idx << endl;

    return 0;
}
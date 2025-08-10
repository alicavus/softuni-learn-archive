#include <iostream>
#include <sstream>
#include <queue>

using namespace std;

int main(){
    queue<string>superMarketQueue;
    for(string name; getline(cin, name) && name != "End";){
        if(name == "Paid"){
            while(! superMarketQueue.empty()){
                cout << superMarketQueue.front() << endl;
                superMarketQueue.pop();
            }
            continue;
        }
        superMarketQueue.push(name);
    }
    cout << superMarketQueue.size() << " people remaining." << endl;
    return 0;
}
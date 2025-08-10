#include <iostream>
#include <sstream>
#include <stack>

using namespace std;

int main(){
    stack<unsigned>s;
    {
        string input;
        getline(cin, input);
        
        istringstream inps(input);

        for(unsigned cloth; inps >> cloth;)
            s.push(cloth);
    }

    unsigned rackCapacity;
    cin >> rackCapacity;

    unsigned racksCount = 1;

    unsigned curSum = 0;

    while(! s.empty()){
        if(curSum + s.top() <= rackCapacity){
            curSum += s.top();
            s.pop();
        }
        else{
            curSum = 0;
            racksCount++;
        }
    }

    cout << racksCount << endl;
    return 0;
}
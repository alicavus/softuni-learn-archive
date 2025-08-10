#include <iostream>
#include <sstream>
#include <vector>
#include <map>

using namespace std;

int main(){
    int N;
    cin >> N;

    map<int, int>numbers;

    while(N--){
        int n;
        cin >> n;
        numbers[n]++;
    }

    for(const pair<int, int> &n : numbers)
        if(n.second % 2 == 0){
            cout << n.first << endl;
            break;
    }

    return 0;
}
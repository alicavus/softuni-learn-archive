#include <iostream>
#include <sstream>
#include <vector>
#include <map>

using namespace std;

int main(){
    map<double, int>m;
    {
        string input;
        getline(cin, input);

        istringstream inpstr(input);

        for(double n; inpstr >> n;)
            m[n]++;
    }
    
    for(const pair<double, int> &n : m)
        cout << n.first << " -> " << n.second << endl;

    return 0;
}
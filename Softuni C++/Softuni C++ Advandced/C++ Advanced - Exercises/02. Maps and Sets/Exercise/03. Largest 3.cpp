#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <set>

using namespace std;

int main(){
    set<double>s;
    {
        string inputline;
        getline(cin, inputline);

        istringstream iss(inputline);

        for(double n; iss>>n;){
            s.insert(n);
        }
    }

    set<double>::const_reverse_iterator crit = s.rbegin();

    int cnt = 0;

    while(crit != s.rend() && ++cnt <= 3){
        cout << *crit << ' ';
        advance(crit, 1);
    }
    
    cout << endl;

    return 0;
}
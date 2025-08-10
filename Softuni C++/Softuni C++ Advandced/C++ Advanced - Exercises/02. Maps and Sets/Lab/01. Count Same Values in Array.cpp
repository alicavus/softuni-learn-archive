#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <set>

using namespace std;

int main(){
    vector<double>v;
    {
        string input;
        getline(cin, input);

        istringstream inpstr(input);

        for(double n; inpstr >> ws >> n;)
            v.push_back(n);
    }

    map<double, int>m;
    set<double>s;

    for(double &n : v)
        ++m[n];
    
    
    for(double &n : v){
        if(s.count(n)) continue;
        s.insert(n);
        cout << n << " - " << m[n] << " times" << endl;
    }
    
    return 0;
}
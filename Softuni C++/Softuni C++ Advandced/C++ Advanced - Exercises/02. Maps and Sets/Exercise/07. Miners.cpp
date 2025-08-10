#include <iostream>
#include <sstream>
#include <vector>
#include <map>

using namespace std;

int main(){
    map<string, int>m;
    vector<string>v;
    {
        string resource;
        int quantity;

        while(true){
            cin >> resource;
            if(resource == "stop") break;

            cin >> quantity;

            if(m[resource] == 0) v.push_back(resource);
            
            m[resource] += quantity;
        }
    }

    for(const string &r : v){
        cout << r << " -> " << m[r] << endl;
    }
    
    return 0;
}
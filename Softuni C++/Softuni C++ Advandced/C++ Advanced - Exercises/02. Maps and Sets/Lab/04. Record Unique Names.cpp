#include <iostream>
#include <sstream>
#include <vector>
#include <set>

using namespace std;

int main(){
    set<string>uniqueNames;
    vector<string>names;
    {
        int N;
        cin >> N;

        
        while(N--){
            string name;
            cin >> name;
            names.push_back(name);
        }
    }

    for(const string &name : names){
        if(not uniqueNames.count(name))
            cout << name << endl;
        uniqueNames.insert(name);
    }
    return 0;
}
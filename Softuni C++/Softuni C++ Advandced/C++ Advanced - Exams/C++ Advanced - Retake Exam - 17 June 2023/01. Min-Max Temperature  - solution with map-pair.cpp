#include <iostream>
#include <sstream>
#include <map>
#include <vector>

using namespace std;

int main(){
    size_t cntTowns;
    cin >> cntTowns;

    map<string, pair<double, double>>weather;

    while(weather.size() < cntTowns){
        string townName;
        double tempOne, tempTwo;
        getline(cin >> ws, townName);
        cin >> tempOne >> tempTwo;
        
        if(! weather.count(townName)){
            weather[townName].first = min(tempOne, tempTwo);
            weather[townName].second = max(tempOne, tempTwo);
        }
        else {
           weather[townName].first = min(weather[townName].first, min(tempOne, tempTwo)); 
           weather[townName].second = max(weather[townName].second, max(tempOne, tempTwo)); 
        }
    }

    for(const pair<string, pair<double, double>>&town : weather){
        cout << town.first << ' ' << town.second.first << ' ' << town.second.second << endl;
    }

    return 0;
}
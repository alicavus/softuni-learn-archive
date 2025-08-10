#include <iostream>
#include <sstream>
#include <map>
#include <vector>

using namespace std;

typedef struct {
    double minT;
    double maxT;
} townT;

int main(){
    size_t cntTowns;
    cin >> cntTowns;

    map<string, townT>weatherForecast;

    while(weatherForecast.size() < cntTowns){
        townT town;
        string townName;
        cin >> ws >> townName >> town.minT >> town.maxT;

        if(weatherForecast.count(townName)){
            weatherForecast[townName].minT = min(weatherForecast[townName].minT, town.minT);
            weatherForecast[townName].maxT = max(weatherForecast[townName].maxT, town.maxT);
        }
        else{
            weatherForecast.insert(make_pair(townName, town));
        }
    }

    for(const pair<string, townT>&town : weatherForecast){
        cout << town.first << ' ' << town.second.minT << ' ' << town.second.maxT << endl;
    }
    
    return 0;
}

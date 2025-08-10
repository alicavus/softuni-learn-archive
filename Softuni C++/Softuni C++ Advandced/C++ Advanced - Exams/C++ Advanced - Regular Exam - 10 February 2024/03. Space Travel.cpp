#include <iostream>
#include <sstream>
#include <map>
#include <vector>

using namespace std;

int main(){
    vector<string>solarSystemVect;
    map<string, int>solarSystemMap;

    int currIdx = 0;
    for(string buff; getline(cin>>ws, buff) && buff != "END";){
        solarSystemMap[buff] = currIdx++;
        solarSystemVect.push_back(buff);
    }

    int solarSystemDistances[solarSystemVect.size()][solarSystemVect.size()];
    int minDistance;
    int maxDistance;

    for(size_t rIdx = 0; rIdx < solarSystemVect.size(); rIdx++){
        for(size_t cIdx = 0; cIdx < solarSystemVect.size(); cIdx++){
            int distance;
            cin >> distance;
            solarSystemDistances[rIdx][cIdx] = distance;

            if(! distance)
                continue;

            if(!rIdx && cIdx == 1){
                minDistance = distance;
                maxDistance = distance;
            }
            else {
                minDistance = min(minDistance, distance);
                maxDistance = max(maxDistance, distance);
            }
        }
    }

    ostringstream ossMin, ossMax;

    for(size_t rIdx = 0; rIdx < solarSystemVect.size(); rIdx++){
        for(size_t cIdx = 0; cIdx < solarSystemVect.size(); cIdx++){
            if(solarSystemDistances[rIdx][cIdx] == minDistance){
                ossMin << minDistance << ": " << solarSystemVect[rIdx] << " -> " << solarSystemVect[cIdx] << endl;
            }
            if(solarSystemDistances[rIdx][cIdx] == maxDistance){
                ossMax << maxDistance << ": " << solarSystemVect[rIdx] << " -> " << solarSystemVect[cIdx] << endl;
            }
        }
    }

    cout << ossMin.str() << ossMax.str();

    int totalDistance = 0;

    for(string buff; getline(cin>>ws, buff) && buff != "END";){
        istringstream iss(buff);
        string prevObject = "";
        string currObject = "";
        int totalRowDistance = 0;
        while(iss >> currObject){
            if(prevObject.size())
                totalRowDistance += solarSystemDistances[solarSystemMap[prevObject]][solarSystemMap[currObject]];
            prevObject = currObject;
        }
        cout << totalRowDistance << endl;
        totalDistance += totalRowDistance;
    }

    cout << totalDistance << endl;

    return 0;
}
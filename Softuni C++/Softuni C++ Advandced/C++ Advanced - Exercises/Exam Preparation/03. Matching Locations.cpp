#include <iostream>
#include <sstream>
#include <vector>
#include <unordered_map>

using namespace std;

typedef struct {
    string latitude;
    string longitude;
}location;

int main(){
    vector<string>locationsVect;
    unordered_map<string, location>locationsMap;

    for(string locationInfo; getline(cin>>ws, locationInfo) && locationInfo != ".";){
        istringstream iss(locationInfo);
        string name, latitude, longitude;
        getline(iss, name, ',');
        getline(iss, latitude, ',');
        getline(iss, longitude, ',');

        locationsVect.push_back(name);
        locationsMap[name].latitude = latitude;
        locationsMap[name].longitude = longitude; 
    }

    for(string locationInfo; getline(cin>>ws, locationInfo) && locationInfo != ".";){
        if(locationsMap.count(locationInfo)){
            cout << locationInfo << ',' << locationsMap[locationInfo].latitude << ',' << locationsMap[locationInfo].longitude << endl;
            continue;
        }
        istringstream iss(locationInfo);
        string latitude, longitude;
        iss >> latitude >> longitude;

        for(const string &locName : locationsVect){
            if(locationsMap[locName].latitude == latitude and locationsMap[locName].longitude == longitude)
                cout << locName << ',' << locationsMap[locName].latitude << ',' << locationsMap[locName].longitude << endl;
        }
    }

    return 0;
}
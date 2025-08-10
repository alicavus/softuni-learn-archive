#include <iostream>
#include <sstream>
#include <vector>
#include <set>
#include <stack>
#include <map>

using namespace std;

struct stationType{
    int demand;
    int delivered;
};

int main(){
    vector<string>stationsVect;
    map<string, stationType>stationsMap;

    stack<int>packsInTruck;

    bool isOutOfStock = false;

    {
        for(string inputline; getline(cin, inputline) && inputline != "end";){
            string stationName;
            int stationDemand;

            istringstream inps(inputline);

            inps >> stationName >> stationDemand;

            stationsVect.push_back(stationName);
            stationsMap[stationName].demand = stationDemand;
        }
        
        string inputline;
        getline(cin, inputline);
        
        istringstream inps(inputline);

        for(int packsCount; inps >> packsCount;)
            packsInTruck.push(packsCount);
    }

    for(const string &stName : stationsVect){
        cout << stName << " ";

        while(stationsMap[stName].demand > stationsMap[stName].delivered){
            if(packsInTruck.empty()){
                isOutOfStock = true;
                cout << "Out of Stock!";
                break;
            }

            size_t idx = packsInTruck.size() - 1;

            int availablePacks = packsInTruck.top();

            int demand = stationsMap[stName].demand - stationsMap[stName].delivered;
            int delivered = (availablePacks >= demand)? demand : availablePacks;

            stationsMap[stName].delivered += delivered;
            packsInTruck.top() -= delivered;

            cout << idx << ":" << delivered << " ";

            if(packsInTruck.top() == 0)
                packsInTruck.pop();
        }
        cout << endl;

        if(isOutOfStock){

            int incomplete = 0;

            for(const pair<string, stationType>&p : stationsMap)
                incomplete += p.second.demand - p.second.delivered;
            
            cout << "Incomplete: " << incomplete << endl;
            break;
        }
    }
    
    if(! packsInTruck.empty()){

        int remaining = 0;
        while(! packsInTruck.empty()){
            remaining += packsInTruck.top();
            packsInTruck.pop();
        }

        cout << "Remaining packs: " << remaining << endl;
    }

    return 0;
}
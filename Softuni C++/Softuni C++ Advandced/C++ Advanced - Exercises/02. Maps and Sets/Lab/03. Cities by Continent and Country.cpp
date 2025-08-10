#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;
typedef map<string, vector<string>>countryType;

void printCountry(const countryType &country){
    for(const pair<string, vector<string>> &p : country){
        cout << "  " << p.first << " -> ";
        for(vector<string>::size_type vidx = 0; vidx < p.second.size(); ++vidx){
            cout << p.second[vidx];
            if(vidx < p.second.size() - 1) cout << ", ";
        }
        cout << endl;
    }
}

int main(){
    //countryType countries;
    map<string, countryType>continents;

    {
        int N;
        cin >> N;
        while(N--){
            string continent, country, city;
            cin >> continent >> country >> city;
            continents[continent][country].push_back(city);
            sort(continents[continent][country].begin(), continents[continent][country].end());
        }
    }
    continents;

    for(const pair<string, countryType> &continent : continents){
        cout << continent.first << ":" << endl;
        printCountry(continent.second);
    }
    return 0;
}

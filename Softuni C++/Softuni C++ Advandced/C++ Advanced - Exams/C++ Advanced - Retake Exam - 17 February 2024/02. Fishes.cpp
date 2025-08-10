#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <stack>
#include <queue>

using namespace std;

void readBag(stack<string>bag, map<string, int>&fishes){
    if(bag.size()){
        stack<string> fishesStackTwo;
        while(bag.size()){
            string fishName = bag.top();

            fishes[fishName]++;

            fishesStackTwo.push(fishName);

            bag.pop();
        }

        while(fishesStackTwo.size()){
            string fishName = fishesStackTwo.top();
            cout << fishName;
            fishesStackTwo.pop();

            if(fishesStackTwo.size())
                cout << ", ";
        }
    }
    else
        cout << "<empty>";
}

int main(){
    vector<stack<string>>bags(3, stack<string>());
    map<string, int>fishes;

    //Catching fishes
    for(string fishInfo; getline(cin >> ws, fishInfo) && fishInfo != "END";){
        int bagNo;
        istringstream iss(fishInfo);
        iss >> bagNo;
        bagNo--; // Proper address fish & bag No
        string fishName;
        getline(iss>>ws, fishName);


        //Special fish command
        if(fishName == "THROW"){
            if(bags[bagNo].size())
                bags[bagNo].pop();
        }

        else
            bags[bagNo].push(fishName);
    }

    int bagNo = 0;
    for(const stack<string>&bag : bags){
        cout << ++bagNo << ": ";
        readBag(bag, fishes);
        cout << endl;
    }

    //Sorting fishes to Restaurant's and Pate
    map<string, int>restaurant, pate;
    for(string fishName; getline(cin >> ws, fishName) && fishName != "END";){
        if(fishes.find(fishName) != fishes.end())
            restaurant[fishName] = fishes[fishName];
    }


    for(const auto &fishInfo :  fishes){
        if(! restaurant.count(fishInfo.first))
            pate[fishInfo.first] = fishInfo.second;
    }

    cout << "Restaurant:";
    if(restaurant.size()){
        for(map<string, int>::const_iterator cit = restaurant.begin(); cit != restaurant.end(); ++cit){
            cout << ' ' << cit -> first << ": " << cit -> second;
            map<string, int>::const_iterator cit2 = cit;
            if(++cit2 != restaurant.end())
                cout << ',';
        }
    }
    else
        cout << " <nothing>";
    
    cout << endl;

    cout << "Pate:";
    if(pate.size()){
        for(map<string, int>::const_iterator cit = pate.begin(); cit != pate.end(); ++cit){
            cout << ' ' << cit -> first << ": " << cit -> second;
            map<string, int>::const_iterator cit2 = cit;
            if(++cit2 != pate.end())
                cout << ',';
        }
    }
    else
        cout << " <nothing>";
    
    cout << endl;
}
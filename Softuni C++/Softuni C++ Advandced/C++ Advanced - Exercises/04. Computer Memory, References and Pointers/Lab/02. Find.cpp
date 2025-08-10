#include <iostream>
#include <sstream>
#include <unordered_map>

using namespace std;

void readInfo(unordered_map<string, string>&companyInfo){
    for(string compInfo; getline(cin, compInfo) && compInfo != "end";){
        string compName, compId;
        istringstream iss(compInfo);
        iss >> compName >> compId;

        companyInfo[compId] = compName;
    }
}

void printSearch(const unordered_map<string, string>&companyInfo, string &searchId){
    if(companyInfo.count(searchId))
        cout << companyInfo.at(searchId) << ' ' << searchId;
    else 
        cout << "[not found]";
    cout << endl;
}


int main(){
    unordered_map<string, string>companyInfo;
    readInfo(companyInfo);

    string searchId;
    cin >> searchId;

    printSearch(companyInfo, searchId);
    return 0;
}
 
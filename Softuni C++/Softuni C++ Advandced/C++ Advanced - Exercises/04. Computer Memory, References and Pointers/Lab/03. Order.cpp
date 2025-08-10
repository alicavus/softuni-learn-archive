#include <iostream>
#include <sstream>
#include <map>

using namespace std;

void readInfo(map<string, string>&companyInfo){
    for(string compInfo; getline(cin, compInfo) && compInfo != "end";){
        string compName, compId;
        istringstream iss(compInfo);
        iss >> compName >> compId;

        companyInfo[compId] = compName;
    }
}

void printCompanies(const map<string, string>&companyInfo){
    for(map<string, string>::const_iterator cit = companyInfo.begin(); cit != companyInfo.end(); ++cit){
        cout << cit -> second << ' ' << cit -> first << endl;
    }
}


int main(){
    map<string, string>companyInfo;
    readInfo(companyInfo);

    printCompanies(companyInfo);
    return 0;
}
 
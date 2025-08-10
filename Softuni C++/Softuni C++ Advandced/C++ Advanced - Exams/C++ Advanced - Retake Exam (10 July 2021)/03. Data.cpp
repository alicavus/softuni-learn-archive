#include <iostream>
#include <sstream>
#include <unordered_map>
#include <vector>

using namespace std;

int main(){
    vector<unordered_map<string, string>>entitiesVect;
    string idxFieldName;
    cin >> idxFieldName;
    for(string entityBuff; getline(cin >> ws, entityBuff) && entityBuff != "[queries]";){
        unordered_map<string, string>entityMap;
        istringstream inpstr(entityBuff);
        for(string fieldName, fieldValue; inpstr >> fieldName >> fieldValue;)
            entityMap[fieldName] = fieldValue;
        if(entityMap.size())
            entitiesVect.push_back(entityMap);
    }

    vector<string>searchResults;
    for(string searchInfoBuff, idxFieldValue, searchFieldName; getline(cin, searchInfoBuff) && searchInfoBuff != "end";){
        string currSearchResult;
        istringstream inpstr(searchInfoBuff);
        inpstr >> idxFieldValue >> searchFieldName;
        bool idxFieldFound = false;
        for(vector<unordered_map<string, string>>::const_iterator vcit = entitiesVect.begin(); vcit != entitiesVect.end(); ++vcit){
            //unordered_map<string, string>entity = *vcit;
            if(vcit -> count(idxFieldName)){
                if(vcit->at(idxFieldName) == idxFieldValue){
                    idxFieldFound = true;
                    if(vcit -> count(searchFieldName)){
                        if(currSearchResult.size())
                            currSearchResult.push_back(' ');
                        currSearchResult += vcit->at(searchFieldName);
                    }
                }  
            }
        }

        if(idxFieldFound){
            cout << (currSearchResult.size()? currSearchResult : "") << endl;
        }
        else 
            cout << "[not found]" << endl;

    }
    return 0;
}
#include <iostream>
#include <sstream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    string headersBuff;
    getline(cin, headersBuff);

    istringstream iss(headersBuff);
    map<string, vector<string>>table;
    vector<string>fields;
    for(string field; getline(iss, field, ' ');){
        fields.push_back(field);
        vector<string>column;
        table[field] = column;
    }

    for(string rowBuff; getline(cin, rowBuff) && rowBuff != "end";){
        size_t colIdx = 0;

        istringstream iss(rowBuff);

        for(string cell; getline(iss, cell, ' ');)
            table[fields[colIdx++]].push_back(cell);
    }

    string columnName;
    cin >> columnName;

    vector<string>column = table[columnName];
    map<string, size_t>values;
    size_t maxCount = 0;
    string maxValue = "";

    for(auto val : column){
        maxCount = max(++values[val], maxCount);
        if(maxCount == values[val])
            maxValue = val;
    }

    cout << maxValue << ' ' << maxCount << endl;
    return 0;
}

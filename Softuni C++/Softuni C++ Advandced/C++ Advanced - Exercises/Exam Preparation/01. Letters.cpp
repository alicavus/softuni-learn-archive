#include <iostream>
#include <sstream>
#include <vector>
#include <map>

using namespace std;

string toWord(string &input){
    string w;
    for(const char &c : input){
        if(!isalpha(c)) break;
        w += c;
    }
    return w;
}


int main(){
    string inputLine;
    getline(cin, inputLine);
    while(true){
        char c;
        cin >> c;
        if(c == '.') break;

        map<string, int>occurences;
        istringstream iss(inputLine);
        
        for(string curr; getline(iss >> ws, curr, ' ');){
            curr = toWord(curr);
            
            if(curr.find(toupper(c)) != string::npos or curr.find(tolower(c)) != string::npos)
                occurences[curr]++;    
        }

        for(const pair<string, int>&occurence : occurences){
            cout << occurence.first << ' ';
        }

        if(!occurences.size())
            cout << "---";
        
        cout << endl;
    }
    return 0;
}
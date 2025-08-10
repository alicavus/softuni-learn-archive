#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

int main(){
    vector<string>words;
    unsigned maxLineWidth;
    for(string line; getline(cin, line) && line != "###";){
        istringstream inpstr(line);
        for(string word; inpstr >> ws >> word;)
            words.push_back(move(word));
    }
    cin >> maxLineWidth;
    string currLine;
    for(vector<string>::const_iterator cit = words.begin(); cit != words.end(); ++cit){
        unsigned currWordLength = cit -> length();
        unsigned currLineLength = currLine.length();

        if(currLine.empty() && cit -> length() > maxLineWidth){
            cout << *cit << endl;
            continue;
        }

        if(currLineLength + currWordLength + 1 > maxLineWidth){
            cout << currLine << endl;
            currLine = *cit;
            continue;
        }
        currLine += (currLine.size() ? " " : "") +  *cit;
    }
    if(currLine.size())
        cout << currLine << endl;
    
    return 0;
}
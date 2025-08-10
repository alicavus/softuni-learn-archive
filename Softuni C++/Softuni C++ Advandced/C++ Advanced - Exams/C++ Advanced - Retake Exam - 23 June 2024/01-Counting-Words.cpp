#include <iostream>
#include <sstream>
#include <string>
#include <map>

using namespace std;

void readParagraph(map<string, int> &m){
    string inp;
    getline(cin, inp);
    istringstream iss(inp);
    for(string word; getline(iss>>ws, word, ' ');){
        char c = word[word.size() - 1];
        string s = "";
        s.push_back(c);
        if(string("!?,.").find(c) != string::npos){
            ++m[s];
            word.pop_back();
        }
        if(word != "") ++m[word];
    }
}

void printWords(map<string, int> &m){
    for(pair<string, int>p : m)
        cout << p.first << " -> " << p.second << endl;
}

int main(){
    map<string, int>words;
    readParagraph(words);
    printWords(words);
}
#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <set>

using namespace std;

string tolower(string s){
    for(char &c : s)
        c = tolower(c);
    
    return s;
}

int main(){
    vector<string>v, v1;
    map<string, int>m;
    set<string>s;

    {
        string input;
        getline(cin, input);

        istringstream iss(input);

        for(string word; getline(iss, word, ' ');){
            word = tolower(word);
            v.push_back(word);
            m[word]++;
        }
    }

    for(const string &word : v){
        if(s.count(word) == 0 and m[word] % 2)
            v1.push_back(word);
    
        s.insert(word);
    }

    for(vector<string>::size_type idx = 0; idx < v1.size(); ++idx){
        cout << v1[idx];
        
        if(idx != v1.size() - 1)
            cout << ", ";
    }
    
    cout << endl;
    
    return 0;
}
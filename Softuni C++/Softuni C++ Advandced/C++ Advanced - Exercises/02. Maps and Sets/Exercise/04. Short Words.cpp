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

const unsigned MAX_WORD_LENGTH = 5;

int main(){
    set<string>s;
    {
        string inputline;
        getline(cin, inputline);

        istringstream iss(inputline);

        for(string word; iss >> word;)
            if(word.size() < MAX_WORD_LENGTH){
                word = tolower(word);
                s.insert(word);
        }  
    }

    for(set<string>::const_iterator cit = s.begin(); cit != s.end(); ++cit){
        cout << *cit;

        set<string>::const_iterator cit2 = cit;
        advance(cit2, 1);

        if(cit2 != s.end()) cout << ", ";
    }
    cout << endl;

    return 0;
}
#include <iostream>
#include <sstream>
#include <stack>
#include <map>
#include <set>

using namespace std;

int main(){
    string sequenceOfParentheses;
    getline(cin, sequenceOfParentheses);

    stack<char>stck;

    map<char, char>p = {
        {']', '['},
        {')', '('},
        {'}', '{'}
    };

    set<char>openings = {'[', '(', '{'};
    set<char>closings = {'}', ']', ')'};

    bool isBalanced = true;

    for(char &c : sequenceOfParentheses){
        if(openings.count(c))
            stck.push(c);
    
        else if(closings.count(c)){
            if(stck.empty() or p[c] != stck.top()){
                isBalanced = false;
                break;
            }
            else stck.pop();
        }
    }

    if(stck.size() > 0)
        isBalanced = false;

    cout << (isBalanced ? "YES" : "NO") << endl;
    return 0;
}
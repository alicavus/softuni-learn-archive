#include <iostream>
#include <sstream>
#include <stack>
#include <map>

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

    bool isBalanced = true;

    for(char &c : sequenceOfParentheses){
        if(string("[({").find(c) != string::npos)
            stck.push(c);
    
        else if(string("}])").find(c) != string::npos){
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
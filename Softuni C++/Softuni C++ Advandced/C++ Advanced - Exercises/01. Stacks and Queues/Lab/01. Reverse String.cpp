#include <iostream>
#include <sstream>
#include <stack>

using namespace std;


int main(){
    string inputText;
    getline(cin, inputText);

    stack<char>sentence;

    for(char c : inputText)
        sentence.push(c);
    
    while(!sentence.empty()){
        cout << sentence.top();
        sentence.pop();
    }
    cout << endl;
    
    return 0;
}

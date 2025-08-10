#include <iostream>
#include <stack>
#include <string>

using namespace std;

void findSubExpressions(const string &expr) {
    stack<int> parenthesesStack;
    
    // Iterate through the expression
    for (int i = 0; i < expr.length(); ++i) {
        char ch = expr[i];
        
        if (ch == '(') {
            // Push the index of opening parenthesis onto the stack
            parenthesesStack.push(i);
        } 
        else if (ch == ')') {
            // Pop the index of the matching opening parenthesis
            int start = parenthesesStack.top();
            parenthesesStack.pop();
            
            // Print the sub-expression between '(' and ')'
            cout << expr.substr(start, i - start + 1) << endl;
        }
    }
}

int main() {
    // Read the input expression
    string expression;
    getline(cin, expression);
    
    // Call the function to find sub-expressions
    findSubExpressions(expression);
    
    return 0;
}

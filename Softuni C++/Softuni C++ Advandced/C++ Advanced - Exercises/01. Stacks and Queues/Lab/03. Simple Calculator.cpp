#include <iostream>
#include <sstream>
#include <stack>

using namespace std;

int main(){
    string exp;
    getline(cin, exp);

    istringstream iss(exp);

    stack<string>expression;
    for(string el; iss >> el;)
        expression.push(el);
    
    int res = 0;
    while(! expression.empty()){
        int n;
        char op;

        istringstream iss(expression.top());
        iss >> n;
        expression.pop();
        op = '+';
        if (!expression.empty()){
            op = expression.top()[0];
            expression.pop();
        }

        res += (op == '+')? n : -n;
    }

    cout << res <<endl;
    return 0;
}
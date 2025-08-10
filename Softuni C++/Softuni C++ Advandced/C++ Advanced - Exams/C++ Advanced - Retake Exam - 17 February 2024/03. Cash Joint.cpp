#include <iostream>
#include <sstream>
#include <map>
#include <vector>
#include <iomanip>

using namespace std;

int main(){
    map<string, double>ACCOUNTS;
    vector<string>currencies;

    for(string cmdline; getline(cin >> ws, cmdline) && cmdline != "END";){
        istringstream iss(cmdline);
        string currency;
        double amount;
        iss >> currency >> amount;
        currencies.push_back(currency);

        ACCOUNTS[currency] += amount; 
    }

    for(string cmdline; getline(cin >> ws, cmdline) && cmdline != "END";){
        istringstream iss(cmdline);
        char operation;
        iss >> operation;

        string currency;
        double amount;
        string currencyTo;
        double amountRate;

        switch(operation){
            case '+':
            case '-':
                iss >> currency >> amount;
                ACCOUNTS[currency] += (operation == '+')? amount : -amount;
                break;
            case 'X':
                iss >> currency >> amount >> currencyTo >> amountRate;
                ACCOUNTS[currency] -= amount;
                ACCOUNTS[currencyTo] += amount * amountRate;
                break;
            case 'P':
                for(const string currency : currencies) {
                    cout << currency << ':' << ' ' << fixed << setprecision(2) << ACCOUNTS[currency] << endl;
                }
                break;
        }
    }

    return 0;
}
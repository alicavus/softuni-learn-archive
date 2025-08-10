

#include <iostream>
#include <sstream>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;


int main() {
    string input;
    getline(cin, input);
    istringstream iss(input);

    unordered_set<int> separators;
    vector<vector<int>> messages;
    while (iss >> input) {
        int separator = stol(input);
        separators.insert(separator);
    }

    getline(cin, input);
    istringstream istr(input);

    vector<int> message;
    while (istr >> input) {
        int number = stol(input);
        if(separators.count(number) == 0) {
            message.push_back(number);
        } else {
            if (!message.empty()) {
                messages.push_back(message);
                message.clear();
            }
        }
    }
    if (!message.empty()) {
        messages.push_back(message);
        message.clear();
    }

    unordered_map<int, int> occurrences;
    for (auto msg : messages) {
        unordered_set<int> uniqueNumbersInMsg;
        for (int number : msg) {
            uniqueNumbersInMsg.insert(number);
        }
        for (int number : uniqueNumbersInMsg) {
            occurrences[number]++;
        }
    }

    int find;
    cin >> find;

    while (find != 0) {
        cout << occurrences[find] << endl;

        cin >> find;
    }

    return 0;
}


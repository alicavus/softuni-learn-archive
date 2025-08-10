#include <iostream>
#include <vector>
#include <unordered_set>
#include <sstream>

using namespace std;

int main() {
    // Read separators
    string separatorLine;
    getline(cin, separatorLine);
    istringstream sepStream(separatorLine);
    unordered_set<int> separators;
    int sep;
    while (sepStream >> sep) {
        separators.insert(sep);
    }

    // Read message
    string messageLine;
    getline(cin, messageLine);
    istringstream msgStream(messageLine);
    vector<int> message;
    int num;
    while (msgStream >> num) {
        message.push_back(num);
    }

    // Split message into parts and store unique values in each part
    vector<unordered_set<int>> parts;
    unordered_set<int> currentPart;
    for (int val : message) {
        if (separators.find(val) != separators.end()) {
            if (!currentPart.empty()) {
                parts.push_back(currentPart);
                currentPart.clear();
            }
        } else {
            currentPart.insert(val);
        }
    }
    if (!currentPart.empty()) {
        parts.push_back(currentPart);
    }

    // Process search values
    int searchValue;
    while (cin >> searchValue && searchValue != 0) {
        int count = 0;
        for (const auto& part : parts) {
            if (part.find(searchValue) != part.end()) {
                count++;
            }
        }
        cout << count << endl;
    }

    return 0;
}
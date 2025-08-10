#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<pair<int, int>> ranges;
    string line;

    // Read ranges
    while (getline(cin, line) && line != ".") {
        int from, to;
        sscanf(line.c_str(), "%d %d", &from, &to);
        ranges.push_back(make_pair(from, to));
    }

    // Sort ranges based on the starting value
    sort(ranges.begin(), ranges.end());

    // Read check numbers and process them
    while (getline(cin, line) && line != ".") {
        int num = stoi(line);
        bool found = false;

        // Binary search to find if the number is in any range
        int left = 0, right = ranges.size() - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (ranges[mid].first <= num && num <= ranges[mid].second) {
                found = true;
                break;
            } else if (ranges[mid].second < num) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        // Output the result
        if (found) {
            cout << "in" << endl;
        } else {
            cout << "out" << endl;
        }
    }

    return 0;
}

#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <climits>

#include "classes.h"
#include "solution.h"

using namespace std;

int main() {
    vector<Dog> dogs;
    vector<Employee> employees;

    string buffer;
    while (getline(cin, buffer) && buffer != ".") {
        string first, second, third;
        int value;
        istringstream istr(buffer);

        istr >> first >> second >> third;
        if ((bool)istr == false)
            dogs.emplace_back(first, stoi(second));
        else
            employees.emplace_back(first[0], second[0], stoi(third));
    }

    vector<Match> matches = match(dogs, employees);

    print<vector<Match>>(cout, matches, "Matched:");
    print<vector<Dog>>(cout, dogs, "Dogs without a walker:");
    print<vector<Employee>>(cout, employees, "Employees without work:");

    return 0;
}

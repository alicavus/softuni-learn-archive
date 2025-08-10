#include <iostream>
#include <sstream>
#include <vector>
#include <set>

using namespace std;

int main(){
    set<string>parkingLot;

    for(string inputline; getline(cin, inputline) && inputline != "END";){

        istringstream inpstr(inputline);

        string direction, carNo;
        inpstr >> direction >> carNo;

        if(direction == "IN,")
            parkingLot.insert(carNo);
        else if(direction == "OUT,")
            parkingLot.erase(carNo);
    }

    for(const string &carNo : parkingLot)
        cout << carNo << endl;
    
    if(parkingLot.empty())
        cout << "Parking Lot is Empty" << endl;

    return 0;
}
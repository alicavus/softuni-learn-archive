#include <iostream>
#include <sstream>

using namespace std;

bool tryToParse(const string &str, int &num){
    istringstream iss(str);
    if(iss >> num)
        return true;
    else
        return false;
}

string printRes(const string &str, const bool &res){
    string r = str;
    if(! res)
        r = "[error] " + r;
    
    return r;
}

int main(){
    string strOne, strTwo;
    cin >> strOne >> strTwo;

    int numOne, numTwo;

    bool resOne = tryToParse(strOne, numOne);
    bool resTwo = tryToParse(strTwo, numTwo);

    if(resOne && resTwo)
        cout << numOne + numTwo << endl;
    else{
        cout << printRes(strOne, resOne) << endl;
        cout << printRes(strTwo, resTwo)<< endl;
    }

    return 0;
}
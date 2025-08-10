#include <iostream>
#include <sstream>
#include <vector>
#include <set>

using namespace std;

int main(){
    int N;
    cin >> N;

    set<string>usernames;

    while(N--){
        string username;
        cin >> username;

        usernames.insert(username);
    }

    for(const string &username : usernames)
        cout << username << endl;
    
    return 0;
}
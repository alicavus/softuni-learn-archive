#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <set>

using namespace std;

int main(){
    set<int>s;
    {
        string inputline;
        getline(cin, inputline);

        istringstream iss(inputline);

        for(int n; iss >> n;)
            s.insert(n);
    }



    for(set<int>::const_iterator cit = s.begin(); cit != s.end(); ++cit){
        set<int>::const_iterator cit2 = cit;
        ++cit2;

        cout << *cit;

        if(cit2 != s.end())
            cout << " <= ";
    }

    cout << endl;

    return 0;
}
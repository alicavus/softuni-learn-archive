#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <cmath>

using namespace std;

bool isSquare(int n){
    int sqrtNInt = sqrt(n);
    double sqrtNDouble = sqrt(n);

    return (sqrtNDouble - sqrtNInt) ? false : true;
}

int main(){
    map<int, int>m;
    {
        string inputline;
        getline(cin, inputline);

        istringstream iss(inputline);

        for(int n; iss >> n;)
            if(isSquare(n))
                m[n]++;
    }

    for(map<int, int>::const_reverse_iterator crit = m.rbegin(); crit != m.rend(); ++crit){
        map<int, int>::const_reverse_iterator crit2 = crit;
        crit2++;

        for(size_t cnt = 1; cnt <= (*crit).second; cnt++){
            cout << (*crit).first;
            if(cnt < (*crit).second)
                 cout << " ";
        }

        if(crit2 != m.rend())
            cout << " ";
    }

    cout << endl;
    
    return 0;
}
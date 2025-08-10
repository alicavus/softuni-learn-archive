#include <iostream>
#include <sstream>
#include <vector>
#include <set>

using namespace std;

int main(){
    int n, m;
    cin >> n >> m;

    set<int>A, B;

    while(n--){
        int a;
        cin >> a;
        A.insert(a);
    }

    while(m--){
        int b;
        cin >> b;
        B.insert(b);
    }

    for(const int num : A)
        if(B.count(num))
            cout << num << " ";
    cout << endl;

    return 0;
}
    
#include <iostream>
#include <sstream>
#include <memory>

#define maxSize 100000
using namespace std;

int main(){
    std::unique_ptr<int[]> list = make_unique<int[]>(maxSize);

    string listBuff;
    getline(cin, listBuff);

    istringstream inpstr(listBuff);

    int idx = 0;
    for(int num; inpstr >> num;)
        list[idx++] = num;
    
    bool bFirst = true;
    for(int endIdx = idx-1, begIdx = 0; begIdx <= endIdx; begIdx++, endIdx--){
        if(! bFirst)
            cout << ' ';
        bFirst = false;

        cout << ((begIdx != endIdx) ? list[begIdx] + list[endIdx] : list[endIdx]);
    }
    cout << endl;

    return 0;
}
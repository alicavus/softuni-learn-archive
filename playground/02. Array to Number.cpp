#include <iostream>
#include <vector>

using namespace std;

int main()
{
    unsigned N;
    cin >> N;
    vector<int>arr, arrMerged;
    arr.reserve(N);
    for(size_t idx = 0; idx < N; ++idx){
        int val;
        cin >> val;
        arr.push_back(val);
    }

    arrMerged = arr;

    while(arrMerged.size() > 1){
        arrMerged.clear();
        for(int idx = 0; idx < arr.size() - 1; ++idx){
            arrMerged.push_back(arr[idx] + arr[idx + 1]);
        }
        arr = arrMerged;
    }

    

    for(const int &el : arr) cout << el << endl;
}
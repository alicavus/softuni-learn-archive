#include <iostream>
#include <sstream>
#include <map>
#include <vector>
#include <set>
#include <unordered_set>
#include <cmath>

using namespace std;

int main(){
    int arr[]{ 13, 42, 69 };
int* p = &arr[1];
++(*p);
for (const int elem : arr) {
  std::cout << elem << ' ';
}
}
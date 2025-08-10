#include <iostream>
#include <sstream>

#define maxLength 100000

int main(){
    int* p = new int[maxLength];
    int* p1 = p;
    std::string inputBuff;
    getline(std::cin, inputBuff);
    std::istringstream inpstr(inputBuff);
    *p = -1;
    for(int number; inpstr >> number;){
        if(number < 0)
            continue;
        *p1++ = number;
    }
    while(--p1 >= p )
        std::cout<< *p1 << (p != p1 ? " " : "" );
    
    if(* p == -1)
        std::cout<< "empty";
    
    std::cout << std::endl;

    delete[] p;

    return 0;
}
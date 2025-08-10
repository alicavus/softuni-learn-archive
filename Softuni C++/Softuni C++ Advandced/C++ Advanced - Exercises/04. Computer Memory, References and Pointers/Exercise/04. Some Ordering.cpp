#include <iostream>
#include <sstream>
#include <cstring>

int main(){
    std::string inputLine;
    getline(std::cin, inputLine);

    char* p = new char[inputLine.length()];

    char *pp = p;
    for(const char & c : inputLine)
        *pp++ = c;
    
    for(char *pp = p; *pp != '\0'; ++pp)
        std::cout << char(std::tolower(*pp));
    std::cout << std::endl;
    
    for(char *pp = p; *pp != '\0'; ++pp)
        std::cout << char(std::toupper(*pp));
    std::cout << std::endl;

    delete[] p;

    return 0;
}
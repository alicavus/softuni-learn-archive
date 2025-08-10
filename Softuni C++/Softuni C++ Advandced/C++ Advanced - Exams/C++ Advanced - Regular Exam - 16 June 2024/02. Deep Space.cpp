#include<iostream>
#include<map>
#include<vector>
#include<map>


using namespace std;

int main(){
    map<char, int>stars;
    size_t starsCount = 0;
    size_t planetsCount = 0;
    size_t planetoidsCount = 0;
    
    vector<string>segments;
    
    for(string segment; getline(cin>>ws, segment) && segment != "end";)
        segments.push_back(segment);
    
    string wordReplacement;
    getline(cin>>ws, wordReplacement);
    
    for(string &segment : segments){
        for(char &c : segment){
            if(isalpha(c) and isupper(c)){
                ++starsCount;
                stars[c] += 1;
            }
            else if(c >= '0' and c <= '9')
                planetsCount += c - '0';
            else if(c == '$' or c == '#')
                ++planetoidsCount;
            
            if(wordReplacement.find(c) != string::npos)
                c = '+';
        }
    }
    
    cout << "Stars: " << starsCount << endl;
    if(starsCount) for(const pair<char, int> &star : stars){
        cout << "- " << star.first << ": " << star.second << endl;
    }
    cout << "Planets: " << planetsCount << endl;
    cout << "Asteroids/comets: " << planetoidsCount << endl;

    for(const string &segment : segments)
        cout << segment << endl;
        
    return 0;
}
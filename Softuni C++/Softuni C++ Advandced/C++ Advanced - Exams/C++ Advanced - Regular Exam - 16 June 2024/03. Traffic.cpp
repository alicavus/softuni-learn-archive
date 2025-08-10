#include<iostream>
#include<sstream>
#include<vector>
#include<map>
#include<set>

using namespace std;

int main(){
    int R;
    cin >> R;

    map<char,map<char, int>> matrix;
    set<pair<char, char>>opportunities;

    for(char rowLabel = 'A'; rowLabel < 'A'+R; ++rowLabel){
        map<char, int>row;
        for(char colLabel = 'A'; colLabel < 'A'+R; ++colLabel)
            cin >> row[colLabel];

        matrix[rowLabel] = row;
    }

    //Print Header Line
    cout << " ";
    for(char c = 'A'; c < 'A'+R; ++c){
        cout << ' ' << c; 
    }
    cout << endl;

    for(char rowCh = 'A'; rowCh < 'A'+R; ++rowCh){
        cout << rowCh;

        for(char colCh = 'A'; colCh < 'A'+R; ++colCh){
            cout << ' ' << matrix[rowCh][colCh];

            if(matrix[rowCh][colCh] != matrix[colCh][rowCh]){
                pair<char, char> op1 = {rowCh, colCh};
                pair<char, char> op2 = {colCh, rowCh};

                if(opportunities.count(op1) or opportunities.count(op2))
                    continue;
                
                opportunities.insert(op1);
            }

        }
        cout << endl;
    }

    int totalOptmisations = 0;
    int maxOptimisation = 0;

    map<string, int>optimisations;

    for(const pair<char, char> opportunity : opportunities){
        char first = opportunity.first;
        char second = opportunity.second;

        //Let's print out optimisation opportunity
        cout << first << second << '(' << matrix[first][second] << ") - " <<
        second << first << '(' << matrix[second][first] << ')' << endl;

        //Add optimisation to map, so we can handle it
        int currOptimisation = abs(matrix[first][second] - matrix[second][first]);
        totalOptmisations += currOptimisation;

        ostringstream oss;
        oss << first << second << '-' << second << first;
        optimisations[oss.str()] = currOptimisation;

        maxOptimisation = max(maxOptimisation, currOptimisation);
    }

    cout << "Total opportunities: " << totalOptmisations << endl;

    cout << "Max optimization: ";
    if(optimisations.size()){
        cout << maxOptimisation <<':';
        for(const auto &optimisation : optimisations){
            if(optimisation.second == maxOptimisation)
                cout << ' ' << optimisation.first;
        }
    }
    else
        cout << "none";
    
    cout << endl;
    return 0;
}
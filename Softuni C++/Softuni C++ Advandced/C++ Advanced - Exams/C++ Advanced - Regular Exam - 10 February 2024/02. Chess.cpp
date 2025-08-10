#include <iostream>
#include <sstream>
#include <queue>
#include <stack>
#include <cstring>

using namespace std;

char invertCase(char &c){
    char cc = c;
    if(isupper(c)) cc = tolower(c);
    else if(islower(c)) cc = toupper(c);
    return cc;
}

int main(){
    char chessBoard[8][8];
    {
        for(int rowNum = 0; rowNum < 8; rowNum++)
            for(int colNum = 0; colNum < 8; colNum++)
                cin >> chessBoard[rowNum][colNum];
    }

    string chessBoardStr = "", whiteFigures = "", blackFigures = "";

    for(int rowNum = 0; rowNum < 8; rowNum++){
        for(int colNum = 0; colNum < 8; colNum++){
            chessBoardStr.push_back(invertCase(chessBoard[rowNum][colNum]));
            if(isalpha(chessBoard[rowNum][colNum])){
                if(isupper(chessBoard[rowNum][colNum]))
                    whiteFigures.push_back(chessBoard[rowNum][colNum]);
                else
                    blackFigures.push_back(chessBoard[rowNum][colNum]);
            }
        }
        chessBoardStr.push_back('\n');
    }
    
    if(whiteFigures != "")
        cout << whiteFigures;
    else
        cout << "<no white figures>";
    cout << endl;
    
    if(blackFigures != "")
        cout << blackFigures;
    else
        cout << "<no black figures>";
    cout << endl;

    cout << chessBoardStr;

    return 0;
}
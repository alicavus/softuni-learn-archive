#include <iostream>
#include <sstream>
#include <vector>
#include <set>
#include <stack>
#include <map>
#include <algorithm>

using namespace std;

struct teamType{
    int points;
    int scored;
    int received;
};

int main(){
    vector<string>teamsVect;
    map<string, teamType>teamsMap;

    int topPoints = 0;
    {
        string inputline;
        getline(cin, inputline);

        istringstream iss(inputline);

        for(string team; iss >> ws >> team;)
            teamsVect.push_back(team);
        
        for(string matchScore; getline(cin, matchScore) && matchScore != ".";){
            istringstream iss(matchScore);
            string teamOne, teamTwo;
            int goalsOne, goalsTwo;

            iss >> teamOne >> goalsOne >> teamTwo >> goalsTwo;

            teamsMap[teamOne].points += (goalsOne > goalsTwo) ? 3 : (goalsOne == goalsTwo) ? 1 : 0;
            teamsMap[teamOne].scored += goalsOne;
            teamsMap[teamOne].received += goalsTwo;

            teamsMap[teamTwo].points += (goalsOne < goalsTwo) ? 3 : (goalsOne == goalsTwo) ? 1 : 0;
            teamsMap[teamTwo].received += goalsOne;
            teamsMap[teamTwo].scored += goalsTwo;

            topPoints = max(topPoints, max(teamsMap[teamOne].points, teamsMap[teamTwo].points));
        }
    }

    string topTeams = "";

    for(const string &team : teamsVect){
        cout << team << " - " << teamsMap[team].points << " - " << teamsMap[team].scored << " - " << teamsMap[team].received << endl;
        if(teamsMap[team].points == topPoints){
            if(topTeams.empty())
                topTeams = team;
            else 
                topTeams += ", " + team;
        }
    }

    cout << "Top team(s) : " << topTeams << endl;

    return 0;
}
#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <set>

using namespace std;

void printStudent(pair<string, vector<double>>& p){
    cout << p.first << " -> ";

    double avg = 0;

    cout.setf(ios::fixed);
    cout.precision(2);

    for(double &grade : p.second){
        avg += grade;
        cout << grade << " ";
    }

    avg /= p.second.size();

    cout << "(avg: " << avg <<")" << endl;
}

int main(){
    int N;
    cin >> N;
    map<string, vector<double>> grades;
    {
        for(size_t gradeIdx = 0; gradeIdx < N; ++gradeIdx){
            string studentName;
            double studentGrade;
            cin >> studentName >> studentGrade;
            grades[studentName].push_back(studentGrade);
        }
    }

    for(pair<string, vector<double>>student : grades)
        printStudent(student);


    return 0;
}
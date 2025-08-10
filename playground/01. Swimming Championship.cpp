#include <iostream>

using namespace std;

int main()
{
    int daysOfChampionship, pointsNeeded, swimmersCount;
    cin >> daysOfChampionship >> pointsNeeded >> swimmersCount;

    double hotelPricePerPerson, participationFeePerPerson;
    cin >> hotelPricePerPerson >> participationFeePerPerson;

    double totalPoints{0}, extraPoints{0};

    for(int day = 1; day <= daysOfChampionship; ++day)
    {
        double pointsForTheDay;
        cin >> pointsForTheDay;

        totalPoints += pointsForTheDay + extraPoints;
        extraPoints = pointsForTheDay * 0.05;
    }

    double totalExpences = daysOfChampionship * swimmersCount * hotelPricePerPerson;
    totalExpences += swimmersCount * participationFeePerPerson;

    cout.setf(ios::fixed);
    cout.precision(2);

    if(totalPoints >= pointsNeeded){
        cout << "Money left to pay: " << 0.75 * totalExpences << " BGN." << endl;
        cout << "The championship was successful!" << endl;
    }
    else {
        cout << "Money left to pay: " << 0.9 * totalExpences << " BGN." << endl;
        cout << "The championship was not successful." << endl;
    }

}

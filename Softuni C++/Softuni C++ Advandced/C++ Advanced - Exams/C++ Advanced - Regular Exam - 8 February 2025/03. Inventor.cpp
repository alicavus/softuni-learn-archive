#include <iostream>
#include <sstream>
#include <map>
#include <vector>
#include <set>
#include <cmath>

using namespace std;

int main(){
    size_t numberOfCities;
    cin >> numberOfCities;

    map<string, double>citiesPrices;

    while(citiesPrices.size() < numberOfCities){
        string cityName;
        getline(cin >> ws, cityName);
        double pricePerProduct, quantityOfProducts, totalPrice{0};
        cin >> pricePerProduct >> quantityOfProducts;
        citiesPrices[cityName] += quantityOfProducts * pricePerProduct;
    }

    for(const pair<string, double> &cityData : citiesPrices)
        cout << cityData.first << ' ' << cityData.second << endl;
    
    return 0;
}
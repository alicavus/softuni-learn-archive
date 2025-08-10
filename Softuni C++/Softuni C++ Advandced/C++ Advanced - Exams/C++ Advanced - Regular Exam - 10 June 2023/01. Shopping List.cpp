#include <iostream>
#include <sstream>
#include <unordered_map>
#include <vector>
#include <set>

using namespace std;

typedef struct{
    string name;
    double price;
    size_t count;
    double finalPrice;
} productType;

int main(){
    size_t numberOfItems;
    cin >> numberOfItems;
    unordered_map<string, double> productsMap;
    vector<string>productsVect(numberOfItems);
    set<double, greater<double>>productsPrices;

    double totalPrice = 0;

    for(size_t idxOfItem = 0; idxOfItem < numberOfItems; ++idxOfItem){
        string productName;
        double productPrice, productFinalPrice;
        size_t productCount;
        cin >> productName >> productPrice >> productCount;
        productFinalPrice = productCount * productPrice;

        productsMap[productName] = productFinalPrice;
        productsVect[idxOfItem] = productName;
        
        totalPrice += productFinalPrice;
        
        if (! productsPrices.count(productFinalPrice))
            productsPrices.insert(productFinalPrice);
    }

    cout << "The total sum is: " << totalPrice << " lv." << endl;

    for(double finalPrice : productsPrices)
        for(const string productName : productsVect)
            if(productsMap[productName] == finalPrice)
                cout << productName << ' ' << finalPrice << endl;
                
    return 0;
}
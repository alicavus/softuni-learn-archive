#include <iostream>
#include <sstream>
#include <queue>

using namespace std;

void proccessOrders(queue<int>&orders, int &quantityFood){
    int totalOrders = 0;
    string notEnoughFood = "";
    if(orders.empty()) return;

    int biggestOrder = orders.front();

    while(not orders.empty()){
        biggestOrder = max(biggestOrder, orders.front());
        
        totalOrders += orders.front();

        if(quantityFood >= orders.front() and notEnoughFood == "")
            quantityFood -= orders.front();
    
        else
            notEnoughFood += " " + to_string(orders.front());
        
        orders.pop();
    }

    cout << biggestOrder << endl;

    if(notEnoughFood == "")
        cout << "Orders complete" << endl;
    else 
        cout << "Orders left:" << notEnoughFood << endl;
}

int main(){
    int quantityFood;
    cin >> quantityFood;

    queue<int>orders;
    {
        string input;
        cin.ignore();
        getline(cin, input);

        istringstream iss(input);
        
        for(int orderAmount; iss >> ws >> orderAmount;)
            orders.push(orderAmount);
    }
    
    proccessOrders(orders, quantityFood);

    return 0;
}
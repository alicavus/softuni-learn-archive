// 02.Calculation
#include <iostream>
#include <memory>

struct Building{};

int main(){

for (int i = 0; i < 3; ++i) {
    std::unique_ptr<Building>buildingOne(new Building());
    std::unique_ptr<Building>buildingTwo(new Building());
  }
}
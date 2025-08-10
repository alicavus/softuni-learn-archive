#ifndef CAR_H
#define CAR_H


class Car{
    const std::string Brand;
    const std::string Model;
    const int Year;

    public:

    Car(std::string BrandName, std::string ModelName, int YearNum) 
        : Brand(BrandName), Model(ModelName), Year(YearNum)
    {}


    std::string GetBrand() const {
        return this -> Brand;
    }

    std::string GetModel() const {
        return this -> Model;
    }

    int GetYear() const {
        return this -> Year;
    }



};
#endif // !CAR_H
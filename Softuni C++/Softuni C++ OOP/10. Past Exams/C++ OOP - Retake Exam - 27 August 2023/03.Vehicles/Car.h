#ifndef CAR_H_
#define CAR_H_

#include <cstddef>

class Car{
    protected:
    int _curSpeed{0};
    int _maxSpeed;
    int _fuel;
    int _distance{0};

    public:
    Car(int maxSpeed, int fuel): _maxSpeed(maxSpeed), _fuel(fuel){}

    bool isCarRunning() const{
        return _fuel > 0;
    }

    int getDistance() const{
        return _distance;
    }

    int getFuel() const{
        return _fuel;
    }

    int getSpeed() const{
        return _curSpeed;
    }


    void advance(){
        _distance += _curSpeed;
    }

    virtual void increaseSpeed(int speedIncrease, int fuelConsumtion){
        _curSpeed += speedIncrease;
        if(_curSpeed > _maxSpeed)
            _curSpeed = _maxSpeed;
        
        _fuel -= fuelConsumtion;

        if(_fuel < 0){
            _curSpeed = 0;
            _fuel = 0;
        }
    }
    virtual void decreaseSpeed(int speedDecrease){
        _curSpeed -= speedDecrease;
        if(_curSpeed < 0)
            _curSpeed = 0;
    }
    virtual ~Car() = default;

};

#endif
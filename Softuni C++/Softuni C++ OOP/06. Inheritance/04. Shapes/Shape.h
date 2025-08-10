#pragma once

#include "Vector2D.h"

class Shape{
    Vector2D center;

    protected:
    double area=0;

    public:
    Shape() : center(0, 0){};
    Shape(Vector2D c) : center(c) {};

    const Vector2D& getCenter() const{
        return center;
    }

    const double getArea() const{
        return area;
    }

};
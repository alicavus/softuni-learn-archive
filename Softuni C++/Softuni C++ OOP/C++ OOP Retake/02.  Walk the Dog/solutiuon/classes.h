#ifndef CLASSES_H
#define CLASSES_H

#include <string>
#include <ostream>

class Dog {

    public:

        Dog(const std::string & name, int power) : name(name), power(power) {}

        friend std::ostream & operator << (std::ostream & ostr, const Dog &);

        int getPower(void) const { return power; }

    private:
        std::string name;
        int power;
};

class Employee {

    public:

        Employee(char first, char second, int strength) : first(first), second(second), strength(strength) {}

        friend std::ostream & operator << (std::ostream & ostr, const Employee &);

        int getStrength(void) const { return strength; }

    private:
        char first, second;
        int strength;

};

class Match {

    const Dog dog;
    const Employee employee;

    public:

        Match(const Dog & dog, const Employee & employee) : dog(dog), employee(employee) {}

        friend std::ostream & operator << (std::ostream & ostr, const Match &);

};

#endif
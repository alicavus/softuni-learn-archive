#ifndef CLASSES_H
#define CLASSES_H

#include <string>

class Person {

    std::string firstName, secondName;

    public:

        Person(const std::string & firstName, const std::string & secondName) : firstName(firstName), secondName(secondName) {}
        virtual ~Person() = default;

        std::string getId() { return Person::generateId(firstName, secondName); }

        operator std::string() const { return firstName + " " + secondName; }

        static std::string generateId(const std::string & firstName, const std::string & secondName) {
            return firstName + secondName;
        }

};

struct Participation {

    virtual ~Participation() = default;

    virtual void registerParticipation(const Person *) = 0;
    virtual std::string getInfo() const = 0;

};

#endif
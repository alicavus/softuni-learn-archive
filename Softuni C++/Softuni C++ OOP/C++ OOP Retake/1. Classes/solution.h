#pragma once

#include <iostream>
#include <sstream>
#include <vector>

class Teacher : public Person, public Participation{
    public:
    Teacher(const std::string & firstName, const std::string & secondName)
    : Person(firstName,secondName){}

    virtual void registerParticipation(const Person *) override{}

    virtual std::string getInfo() const override {return "";}
};

class Student : public Person, public Participation{
    public:
    Student(const std::string & firstName, const std::string & secondName)
    : Person(firstName,secondName){}

    virtual void registerParticipation(const Person *) override{}

    virtual std::string getInfo() const override {return "";}
};

void outputPersons(std::string& header, std::vector<const Participation *> p){
    for(const auto& pp : p){
        
    }
}
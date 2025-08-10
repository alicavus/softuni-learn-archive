#ifndef COMPANY_H
#define COMPANY_H

#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <utility>
#include <memory>

using namespace std;

class Company{
    int id;
    std::string name;
    std::vector<std::pair<char, char> > employees;

    public:
    Company();
    Company(int id, std::string name, std::vector<std::pair<char, char> > employees);

    virtual ~Company(){};
    
    virtual bool isSuper(void) const { return false; }

    int getId() const;
    std::string getName() const;
    std::vector<std::pair<char, char> > getEmployees() const;
    std::string getInfo() const;


    friend std::istream& operator>>(std::istream& istr, Company& c);
    friend std::ostream& operator<<(std::ostream& ostr, const Company& c);
    friend bool isSuperCompany(Company *c);
};

#endif // ! COMPANY_H
#ifndef SOLUTION_H_
#define SOLUTION_H_

#include <iostream>
#include <sstream>
#include <vector>
#include <memory>
#include "BaseStudent.h"

using namespace std;

class Student : public BaseStudent{
    public:
    Student() : BaseStudent(){}

    virtual void init(istream& inpstr) override{
        inpstr >> BaseStudent::name >> BaseStudent::grade;
    }
};

bool readStudent(vector<shared_ptr<Student>>& data, string& buffer){
    Student s;
    istringstream inpstr(buffer);
    s.init(inpstr);

    if(inpstr)
        data.push_back(make_shared<Student>(s));
    return (bool) inpstr;
}

std::vector<size_t> processStudents(vector<shared_ptr<Student>>& data){
    std::vector<size_t> gradesCounts(10, 0);
    for(const auto& s : data)
        gradesCounts[(size_t) s->getGrade() / 10]++;
    return gradesCounts;
}

#endif //! SOLUTION_H_
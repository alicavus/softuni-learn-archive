#ifndef SOLUTION_H
#define SOLUTION_H

#include <iostream>
#include <sstream>
#include <vector>
#include <memory>
#include "BaseStudent.h"

using namespace std;

class Student : public BaseStudent{
    public:
    Student() : BaseStudent(){}
    Student(std::string studentName, size_t studentGrade) : BaseStudent(){
        BaseStudent::name = studentName;
        BaseStudent::grade = studentGrade;
    }

    void init(std::istream & inpstr) override{
        std::string studentName;
        size_t studentGrade;
        if(inpstr >> studentName >> studentGrade){
            name = studentName;
            grade = studentGrade;
        }
    }
};

bool readStudent(vector<shared_ptr<Student>>& data, std::string buffer){
    std::istringstream istr(buffer);
    Student s;
    s.init(istr);
    if(istr)
        data.push_back(std::make_shared<Student>(s));
    
    return (bool) istr;
}

std::vector<size_t> processStudents(vector<shared_ptr<Student>>& data){
    std::vector<size_t> v(10, 0);
    for(std::shared_ptr<Student>& shS : data){
        double g = shS->getGrade() * 0.1;
        v[int(g)] += 1;
    }
    return v;
}

#endif //!SOLUTION_H
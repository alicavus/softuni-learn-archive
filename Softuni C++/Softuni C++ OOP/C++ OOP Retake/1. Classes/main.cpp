#include "classes.h"
#include "solution.h"

#include <memory>
#include <map>
#include <vector>

class Persons {

        std::map<std::string, std::unique_ptr<Person>> persons;

    public:

        Person * findPerson(const std::string & firstName, const std::string & secondName) {

            std::string id = generateId(firstName, secondName);

            auto it = persons.find(id);
            if (it != persons.end())
                return it->second.get();

            return nullptr;
        }

        void registerPerson(Person * p) {
            std::string id = p->getId();

            persons[id] = std::unique_ptr<Person>(p);
        }

        static std::string generateId(const std::string & firstName, const std::string & secondName) {
            return Person::generateId(firstName, secondName);
        }

};

int main() {

    Persons data;

    std::vector<const Participation *> students;
    std::vector<const Participation *> teachers;

    std::string line;
    while(std::getline(std::cin, line) && line != ".") {

        std::istringstream istr(line);

        std::string teacherName, teacherFamily;
        istr >> teacherName >> teacherFamily;
        Teacher * t = dynamic_cast<Teacher *>(data.findPerson(teacherName, teacherFamily));

        if (t == nullptr) {
            t = new Teacher(teacherName, teacherFamily);
            data.registerPerson(t);
            teachers.push_back(t);
        }

        while(true) {
            std::string studentName, studentFamily;
            istr >> studentName >> studentFamily;

            if (!istr)
                // end of current line
                break;

            Student * s = dynamic_cast<Student *>(data.findPerson(studentName, studentFamily));

            if (s == nullptr) {
                s = new Student(studentName, studentFamily);
                students.push_back(s);
                data.registerPerson(s);
            }

            s->registerParticipation(t);
            t->registerParticipation(s);
        }
    }

    outputPersons("Teachers: ", teachers);
    outputPersons("Students: ", students);

    return 0;
}
#ifndef SERIALIZE_H
#define SERIALIZE_H

#include "Company.h"
#include <sstream>
#include <vector>

class SerializedCompany : public Company{
    public:
    void serialize(std::vector<byte>&data) const{
        serializeId(data);
        serializeName(data);
        serializeEmployees(data);
    }

    void serializeId(std::vector<byte>&data) const{
        data.push_back((byte)getId());
    }

    void serializeName(std::vector<byte>&data) const{
        const std::string& name = getName();
        for(const char& c : name)
            data.push_back(c);
        data.push_back(0);
    }

    void serializeEmployees(std::vector<byte>&data) const{
        const std::vector<std::pair<char, char>> & employees = getEmployees();
        data.push_back((byte)employees.size());
        for(const std::pair<char, char> & emploee : employees ){
            data.push_back(emploee.first);
            data.push_back(emploee.second);
        }
    }
};

byte* serializeToMemory(const std::string& data, size_t& bytesWritten){
    std::vector<byte>result(1, 0);
    std::istringstream inpstr(data);

    SerializedCompany serializedCompany;
    while(inpstr >> serializedCompany){
        result[0]++;
        serializedCompany.serialize(result);
    }

    bytesWritten = result.size();
    byte* output = new byte[bytesWritten];
    std::copy(result.begin(), result.end(), output);

    return output;
}

#endif // ! SERIALIZE_H
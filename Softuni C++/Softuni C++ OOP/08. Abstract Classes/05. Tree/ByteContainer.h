#ifndef ByteContainer_h
#define ByteContainer_h

#include <string>

class ByteContainer {

    std::string contents;

    public:

    ByteContainer(const std::string & contents) :contents(contents) {};
    virtual ~ByteContainer() {};

    const std::string & getBytes(void) const {
        return contents;
    };

};




#endif
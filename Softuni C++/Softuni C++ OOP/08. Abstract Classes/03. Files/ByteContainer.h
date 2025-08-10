#ifndef BYTECONTAINER_H
#define BYTECONTAINER_H

class ByteContainer{
    std::string contents;

    public:
    ByteContainer(const std::string & contents): contents(contents) {};

    virtual ~ByteContainer() {};

    const std::string & getBytes(void) const {
        return contents;
    }

};

#endif //!BYTECONTAINER_H
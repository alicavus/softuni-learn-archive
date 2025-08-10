#ifndef FILE_H
#define FILE_H

#include "ByteContainer.h"
#include "FileSystemObject.h"

class File: public ByteContainer, public FileSystemObject{
    public:
    File(std::string filename, const std::string& contents)
    : ByteContainer(contents), FileSystemObject(filename){};

    virtual size_t getSize() const {
        return getBytes().size();
    }

};

#endif //!FILE_H
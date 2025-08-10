#ifndef VIRTUALBOOK_H
#define VIRTUALBOOK_H

#include "VirtualPage.h"
#include <iostream>

class VirtualBook{
    std::vector<VirtualPage> _data;

    public:
    VirtualBook(): _data(){}

    void addPage(VirtualPage page){
        _data.push_back(page);
    }
    void printContent() const{
        for(const VirtualPage& vp : _data)
            vp.printContent();
    }
    void removeLastPage(){
        if(_data.size())
            _data.pop_back();
    }
    void removeAllPages(){
        _data.clear();
    }
};

#endif //!VIRTUALBOOK_H
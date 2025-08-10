#ifndef VIRTUALBOOK_H_
#define VIRTUALBOOK_H_

#include "VirtualPage.h"
#include <vector>

class VirtualBook{
    std::vector<VirtualPage> _data;

    public:
    VirtualBook(): _data(){};

    void addPage(VirtualPage& page){
        _data.push_back(page);
    }

    void removeLastPage(){
        if(_data.size())
            _data.pop_back();
    }

    void removeAllPages(){
        _data.clear();
    }

    void printContent(){
        for(auto& _page : _data)
            _page.printContent();
    }
};

#endif //!VIRTUALBOOK_H_
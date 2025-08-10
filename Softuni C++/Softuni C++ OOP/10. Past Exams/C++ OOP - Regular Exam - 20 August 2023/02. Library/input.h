#ifndef INPUT_H_
#define INPUT_H_

#include <string>
#include <map>
#include <iostream>
#include <sstream>

template<typename T>
void read(std::map<size_t, T>& collection, std::istream& istr){
    std::string buf;
    size_t idx;
    while(getline(istr>>ws, buf)){
        if(buf == "end")
            break;
        
        std::istringstream inpstr(buf);
        inpstr >> idx;
        collection[idx] = T(idx, istr);
    }
}

template<typename T>
void print(T& item, std::ostream& ostr){
    ostr << "book " << item.getId() << " \"" << item.getTitle() << "\" by \"" << item.getAuthor() << "\" is \"";
    if(item.getBorrower().size())
        ostr << "borrowed by " << item.getBorrower();
    else
        ostr << "available";
    ostr << "\"" << std::endl;
}

template<typename T>
void borrow(T& item, std::string borrower = ""){
    item.setBorrowed(borrower);
    print(item, std::cout);
}

template<typename T>
void print(const T&& container, std::ostream& ostr){
    ostr << "-----" << std::endl << "total books: " << container-> size() << std::endl;

    for(const auto& p : (*container)){
        print(p.second, ostr);
    }
}


#endif //! INPUT_H_
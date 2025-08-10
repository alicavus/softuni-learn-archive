#ifndef STORE_H_
#define STORE_H_

#include "Console.h"
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>

template<class T>
class Operate{
    friend class Store;

    public:
    static void remove(std::vector<T>& _data){
        if(_data.size()){
            std::cout << "Removing: " << _data.back() << std::endl;
            _data.pop_back();
        }
    }

    static void sort(std::vector<T>& _data, std::function<bool(const T& right, const T& left)> func){
        std::sort(_data.begin(), _data.end(), func);
    }

    static void sortByPrice(std::vector<T>& _data){
        auto func = [](T right, T left){
            return right.getPrice() > left.getPrice();
        };
        sort(_data, func);
    }

    static void sortByQuality(std::vector<T>& _data){
        auto func = [](T right, T left){
            return right.getQuality() > left.getQuality();
        };
        sort(_data, func);
    }

    static void print(std::ostream& ostr, std::vector<T>& _data){
        for(const T& d : _data)
            ostr << d << std::endl;
    }
};

class Xbox : public Console{
    public:
    Xbox(int price, int quality) : Console(price, quality){}

    friend std::ostream& operator<<(std::ostream& ostr, const Xbox& x){
        ostr << "Xbox with price: " << x.getPrice() << ", quality: " << x.getQuality();
        return ostr;
    }
};

class PlayStation : public Console{
    int _generation;
    public:
    PlayStation(int price, int quality, int generation) : Console(price, quality), _generation(generation){}

    int getGeneration() const{
        return _generation;
    }

    friend std::ostream& operator<<(std::ostream& ostr, const PlayStation& x){
        ostr << "PS with generation " << x.getGeneration() << ", price: " << x.getPrice() << ", quality: " << x.getQuality();
        return ostr;
    }
};

class Store{
    std::vector<Xbox> _xbox;
    std::vector<PlayStation>_ps;

    public:
    void addPs(int price, int quality, int generation){
        std::cout << "Adding: PS with generation " << generation << ", price: " << price << ", quality: " << quality << std::endl;
        _ps.push_back(PlayStation(price, quality, generation));
    }

    void addXbox(int price, int quality) {
        std::cout << "Adding: Xbox with price: " << price << ", quality: " << quality << std::endl;
        _xbox.push_back(Xbox(price, quality));
    }

    void remove(ConsoleType consoleType){
        if(consoleType == ConsoleType::PS){
            Operate<PlayStation>::remove(_ps);
        }
        else if(consoleType == ConsoleType::XBOX){
            Operate<Xbox>::remove(_xbox);
        }
    }

    void sortByPrice(ConsoleType consoleType){
        std::string cType;
        if(consoleType == ConsoleType::PS){
            cType = "PS";
            Operate<PlayStation>::sortByPrice(_ps);
        }
        else if(consoleType == ConsoleType::XBOX){
            cType = "Xbox";
            Operate<Xbox>::sortByPrice(_xbox);
        }
        std::cout << "Sorting all " << cType << " by price" << std::endl;
    }

    void sortByQuality(ConsoleType consoleType){
        std::string cType;
        if(consoleType == ConsoleType::PS){
            cType = "PS";
            Operate<PlayStation>::sortByQuality(_ps);
        }
        else if(consoleType == ConsoleType::XBOX){
            cType = "Xbox";
            Operate<Xbox>::sortByQuality(_xbox);
        }
        std::cout << "Sorting all " << cType << " by quality" << std::endl;
    }

    void print(ConsoleType consoleType){
        std::string cType;
        std::ostringstream out;
        if(consoleType == ConsoleType::PS){
            cType = "PS";
            Operate<PlayStation>::print(out, _ps);
        }
        else if(consoleType == ConsoleType::XBOX){
            cType = "Xbox";
            Operate<Xbox>::print(out, _xbox);
        }
        std::cout << "Printing all " << cType << " data" << std::endl << out.str();
    }
};

#endif
#pragma once
#include <sstream>
#include <vector>

template<typename T>
class TypedStream{
    protected:
        std::istringstream stream;
    public:
        TypedStream(const std::string& input): stream(input){};

        virtual ~TypedStream()=default;

        virtual TypedStream<T> & operator>>(T & i) =0;

        operator bool(){
            return (bool) stream;
        }

        std::vector<T> readToEnd() {
            
            std::vector<T> result;

            T curr;

            while (*this>>curr)
                result.push_back(curr);
            
            return result;
        }
};
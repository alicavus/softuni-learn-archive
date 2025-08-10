#ifndef FIELD_H_
#define FIELD_H_

#include <iostream>
#include <vector>
#include "Defines.h"

class Field{
    FieldData f;

    public:
    Field(){}
    void populateField(const FieldData &fieldData){
        f = fieldData;
    }
    FieldData& getFieldData(){
        return f;
    }

};
#endif //! FIELD_H_
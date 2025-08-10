#ifndef RESOURCE_H
#define RESOURCE_H

#include "ResourceType.h"

namespace SoftUni{
    class Resource{
        int id;
        ResourceType resourceType;
        std::string linkURL;

        public:
        Resource(){}

        ResourceType getType() const{
            return this -> resourceType;
        }

        int getId() const{
            return this -> id;
        }

        std::string getLink() const{
            return this -> linkURL;
        }

        void setId(int idNum){
            this -> id = idNum;
        }

        void setResourceType(std::string rType){
            this -> resourceType = (rType == "Presentation")? ResourceType::PRESENTATION 
            : (rType == "Demo")? ResourceType::DEMO : (rType == "Video") ? ResourceType::VIDEO 
            : static_cast<ResourceType>(890);
        }

        void setLink(std::string& linkURL){
            this -> linkURL = linkURL;
        }

        friend bool operator<(const Resource& r1, const Resource& r2){
            return r1.getId() < r2.getId();
        }
    };
}

/*
bool operator<(const SoftUni::Resource r1, const SoftUni::Resource r2){
    return r1.getId() < r2.getId();
}
*/

std::ostream& operator<<(std::ostream& ostr, const SoftUni::Resource& r){
    ostr << r.getId() << ' ' << r.getType() << ' ' << r.getLink();
    return ostr;
}

std::istream& operator>>(std::istream& istr, SoftUni::Resource& r){
    int resourceId;
    std::string resourceType, resourceLink;
    istr >> resourceId >> resourceType >> resourceLink;
    r.setId(resourceId);
    r.setResourceType(resourceType);
    r.setLink(resourceLink);
    return istr;
}

#endif // !RESOURCE_H
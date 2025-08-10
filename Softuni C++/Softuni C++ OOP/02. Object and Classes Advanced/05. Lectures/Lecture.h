#ifndef LECTURE_H
#define LECTURE_H

#include <vector>

#include <algorithm>

namespace SoftUni{
    typedef std::vector<Resource>LectureType;
    class Lecture{
        LectureType lectureContainer;
        public:
        Lecture(){}

        Resource* begin(){
            if(lectureContainer.size() == 0)
                return nullptr;            
            return &lectureContainer[0];
        }

        Resource* end(){
            if(lectureContainer.size() == 0)
                return nullptr;
            return &lectureContainer[lectureContainer.size()];
        }

        int operator[](ResourceType rType){
            int num =  0;
            for(Resource& r : lectureContainer)
                if(r.getType() == rType)
                    num++;

            return num;
        }

        friend Lecture& operator<<(Lecture& lecture, Resource& r){
            bool isFound = false;
            for(Resource& resource : lecture.lectureContainer){
                
                if(resource.getId() == r.getId()){
                    resource = r;
                    isFound = true;
                    break;
                }
            }
            if(! isFound)
                lecture.lectureContainer.push_back(r);
            
            std::sort(lecture.lectureContainer.begin(), lecture.lectureContainer.end());
            return lecture;
        }
    };
}

std::vector<SoftUni::ResourceType>& operator<<(std::vector<SoftUni::ResourceType>& rTypeVect, SoftUni::Lecture& lect){
    for (const SoftUni::Resource& r : lect){
        if(std::find(rTypeVect.begin(), rTypeVect.end(), r.getType()) == rTypeVect.end())
            rTypeVect.push_back(r.getType());
    }
    std::sort(rTypeVect.begin(), rTypeVect.end());
    return rTypeVect;
}


#endif // !LECTURE_H